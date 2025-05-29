import os, discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

client = commands.Bot(command_prefix='=', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Succes: Yuira is connected to Discord")
    
@client.command()
async def ping(ctx):
    await ctx.send("Nya!")

client.run(os.getenv("TOKEN"))
