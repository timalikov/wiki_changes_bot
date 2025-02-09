import discord
from datetime import datetime
from discord.ext import commands
from discord import app_commands

from db.dto import UserLangDTO, RecentChangesDTO
from enums.language_enum import Languages
from .command_choices import language_options
from discord_bot.commands.utils import get_user_language
from config import LANGUAGE_NAMES


class StatsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="stats",
        description="Get info about changes on a specific date. Format: YYYY-MM-DD"
    )
    @app_commands.choices(language=language_options)
    async def stats(
        self,
        interaction: discord.Interaction,
        language: app_commands.Choice[str],
        date: str
    ):
        recent_changes_dto = RecentChangesDTO()
        user_lang_dto = UserLangDTO()
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            await interaction.response.send_message("Invalid date format! Use: YYYY-MM-DD")
            return
        
        lang = await get_user_language(user_lang_dto=user_lang_dto, interaction=interaction, language=language)
        count = await recent_changes_dto.get_changes_count_by_date(date=date_obj, lang=lang)

        message_embed = discord.Embed(
            title="Change Stats",
            description=f"Number of all changes that occured on date {date} for {LANGUAGE_NAMES[Languages(lang)] if lang else "ALL"} language\nIS **{count}**"
        )
        
        await interaction.response.send_message(embed=message_embed)