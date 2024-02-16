import discord
from discord.ext import commands, tasks
import os
import requests

bot = commands.Bot(command_prefix='>',
                   intents=discord.Intents.all(),
                   help_command=None)

@bot.event
async def on_ready():
  url.start()
  print("bot on discord!")

@tasks.loop(seconds=60)
async def url():
  url = "https://5b8aab49-48c5-496b-a3e0-bea69f6efdb3-00-25ryifd5j4q09.kirk.replit.dev/"
  try:
    response = requests.get(url)
    if response.status_code == 200:
      print("Website accessed successfully.")
  except requests.exceptions.RequestException as e:
    print(f"Error accessing website: {e}")

import keep_alive
keep_alive.keep_alive

bot.run(os.environ['TOKEN'])
