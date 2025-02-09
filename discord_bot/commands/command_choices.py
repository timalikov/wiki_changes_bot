from typing import List
import discord
from discord import app_commands
from discord_bot.enums.language_enum import Languages
    
language_names = {
    Languages.UNIMPORTANT: "Unimportant",
    Languages.RU: "Russian",
    Languages.EN: "English",
    Languages.ES: "Spanish",
    Languages.FR: "French",
    Languages.DE: "German",
    Languages.IT: "Italian",
    Languages.PT: "Portuguese",
    Languages.ZH: "Chinese",
    Languages.JA: "Japanese",
    Languages.KO: "Korean",
    Languages.AR: "Arabic",
    Languages.TR: "Turkish",
}

language_options = [
    app_commands.Choice(name=lang_name, value=lang_enum.value)
    for lang_enum, lang_name in language_names.items()
]