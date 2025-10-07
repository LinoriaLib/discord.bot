from server import keep_alive
import os

keep_alive()

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("❌ TOKEN not found in environment variables!")

import bot
bot.bot.run(TOKEN)