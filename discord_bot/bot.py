import asyncio
from typing import List
from config import DISCORD_BOT_TOKEN
import discord
from discord.ext import commands

from discord_bot.commands import SetLangCommand, RecentChangesCommand, StatsCommand

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

    bot_commands: List[commands.Cog] = [
        SetLangCommand,
        RecentChangesCommand,
        StatsCommand
    ]
    await asyncio.gather(*(bot.add_cog(cog(bot)) for cog in bot_commands))
    await bot.tree.sync()

def run_bot():
    bot.run(DISCORD_BOT_TOKEN)