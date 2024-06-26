import discord
from discord.ext import commands
from discord import Interaction
from keep_alive import keep_alive


client = commands.Bot(command_prefix=".",intents= discord.Intents.all()) 


@client.event
async def on_ready():
    await client.tree.sync()
    await client.change_presence(activity=discord.activity.Game(name="Discord"),status=discord.Status.idle)
    print(f"{client.user.name} is ready.")

@client.command()
async def hello(ctx):
    await ctx.send("hai")



@client.tree.command()
async def ping(interaction : Interaction):
    bot_latency=round(client.latency*1000)
    await interaction.response.send_message(f"{bot_latency}ms")


keep_alive()
client.run("MTI0MDY0MzQ4MzMwMDI3MDE1Mw.GFNChU.mN5GfUBhVPq_qTTX1VJF0DKXxL6bZzG_voZodI")
