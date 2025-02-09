from config import DISCORD_BOT_TOKEN
import discord
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

def run_bot():
    bot.run(DISCORD_BOT_TOKEN)