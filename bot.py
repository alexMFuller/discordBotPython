import sys
import discord
from discord.ext import commands
import os
from decouple import config


API_KEY = config('TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix="!", case_insensitive=True)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith('worm'):
        await message.channel.send('bird')
        return


@bot.command(name='hello', description="Greet the user!")
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.name}!")

client.run(API_KEY)
