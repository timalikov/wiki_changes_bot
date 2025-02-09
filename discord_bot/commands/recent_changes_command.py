from datetime import datetime
from config import LANGUAGE_NAMES
import discord
from discord import app_commands
from discord.ext import commands

from db.dto import RecentChangesDTO, UserLangDTO
from discord_bot.commands.utils import get_user_language
from enums.language_enum import Languages
from .command_choices import language_options


class RecentChangesCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(
        name="recent",
        description="Get most recent changes"
        )
    @app_commands.choices(language=language_options)
    async def recent_changes(
        self,
        interaction: discord.Interaction,
        language: app_commands.Choice[str]
    ):
        recent_changes_dto = RecentChangesDTO()
        user_lang_dto = UserLangDTO()

        lang = await get_user_language(user_lang_dto=user_lang_dto, interaction=interaction, language=language)
        recent_changes_data: dict = await recent_changes_dto.get_recent_changes(lang=lang)

        message_embed = discord.Embed(
            title = f"The most recent changes \nFor language: {LANGUAGE_NAMES[Languages(lang)] if lang else "ALL"}",
            color = discord.Color.blue()
        )

        for data in recent_changes_data:
            message_embed.add_field(
                name=datetime.fromtimestamp(data['timestamp']).strftime("%Y-%m-%d %H:%M:%S"),
                value=f"Title: {data['title']}\nURL: {data['title_url']}\nUser: {data['user_name']}",
                inline=False
            )
        
        await interaction.response.send_message(embed=message_embed)

    