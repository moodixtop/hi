import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

# Bot configuration
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix='.v ', intents=intents)

# Load cogs
async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py') and filename != '__init__.py':
            await bot.load_extension(f'cogs.{filename[:-3]}')
            print(f'✅ Loaded cog: {filename}')

@bot.event
async def on_ready():
    print(f'✅ Bot logged in as {bot.user}')
    print(f'✅ Bot ID: {bot.user.id}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='.v help'))

async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv('DISCORD_TOKEN'))

if __name__ == '__main__':
    asyncio.run(main())