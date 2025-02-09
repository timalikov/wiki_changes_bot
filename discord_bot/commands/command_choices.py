from config import LANGUAGE_NAMES
from discord import app_commands
    

language_options = [
    app_commands.Choice(name=lang_name, value=lang_enum.value)
    for lang_enum, lang_name in LANGUAGE_NAMES.items()
]