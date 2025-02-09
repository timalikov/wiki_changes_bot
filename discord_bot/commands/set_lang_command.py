import discord
from discord import app_commands
from imaplib import Commands

from discord_bot.commands.command_choices import language_options


class SetLangCommand(Commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
            name="setLang", 
            description="Set a default language"
        )
    @app_commands.choices(language=language_options)
    async def set_lang(
        self, 
        interaction: discord.Interaction,
        language: app_commands.Choice[str]
    ):
        pass
        