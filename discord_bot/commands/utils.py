import discord
from discord import app_commands


async def get_user_language(user_lang_dto, interaction: discord.Interaction, language: app_commands.Choice[str]) -> str:
    """
    Helper function to determine language.
    - If the user selects a language, use it
    - If 'Unimportant' or no language is selected, fetch the user's default language from the database
    - If the user has no saved language, then show all records without filtering (None returned)
    """
    if language and language.value != "Unimportant":
        return language.value
    
    return await user_lang_dto.get_user_lang(user_id=interaction.user.id)
    
    
