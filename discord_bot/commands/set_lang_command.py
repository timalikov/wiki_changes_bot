from db.dto import UserLangDTO
import discord
from discord import app_commands
from discord.ext import commands

from .command_choices import language_options


class SetLangCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
            name="set_default_lang", 
            description="Set a default language"
        )
    @app_commands.choices(language=language_options)
    async def set_lang(
        self, 
        interaction: discord.Interaction,
        language: app_commands.Choice[str]
    ):
        user_lang_dto = UserLangDTO()
        await user_lang_dto.set_lang(user_id=interaction.user.id, lang=language.value)

        await interaction.response.send_message(f"Successfully changed default language to: {language.name}")
        