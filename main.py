import discord
from discord import app_commands
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN=os.getenv("DISCORD_TOKEN")

class Morshu(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix= "$",
            intents=intents

        )
        self.tree = app_commands.CommandTree(self)



    async def setup_hook(self):
        await self.tree.sync()
    
    async def on_ready(self):
        print(f"Lamp oil, Ropes, Bombs? You want it?")

bot = Morshu()

bot.run(TOKEN)

hello