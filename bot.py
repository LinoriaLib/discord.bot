import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load .env file if running locally
load_dotenv()

# Set up intents and bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connected as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

@bot.tree.command(name="ping", description="Shows the bot's latency")
async def ping(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    await interaction.response.send_message(f"pingtest {latency}ms")

# Run bot with TOKEN from .env or Replit secret
if __name__ == "__main__":
    TOKEN = os.getenv("TOKEN")
    if not TOKEN:
        raise ValueError("❌ TOKEN not found in environment variables!")
    bot.run(TOKEN)