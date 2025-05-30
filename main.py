import os, discord
from dotenv import load_dotenv
from discord.ext import commands
import random

load_dotenv()

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Succes: Yuira is connected to Discord")

#Test Bot    
@client.command()
async def nya(ctx):
    await ctx.send("Nya!")

#pertanyaan random bot    
@client.command()
async def yuira(ctx, *, question):
    with open("responses.txt", "r") as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)
        
    await ctx.send(response)

client.run(os.getenv("TOKEN"))
