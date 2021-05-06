import discord
import os
import asyncio
import time

from random import choice
from discord.ext import commands

description = '''Albert bot description goes here'''
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='/al ', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} #{bot.user.id} !')

@bot.command(name="pick")
async def pick_human_member(ctx):
    guild = discord.utils.get(bot.guilds, name='Cafyy')
    chosen = pick_human(guild.members)

    await ctx.send(f"Je choisis {chosen.name}")

@bot.command(name="countdown")
async def countdown(ctx, timeout):
    print("Starting countdown of... " + timeout + "s")
    countdown = Countdown(int(timeout))
    await countdown.start()
    await ctx.send("Hop hop hop, c'est fini !")

def run():
    bot.run(os.environ.get('BOT_TOKEN'))

def pick_human(members):
    humans = list(filter(lambda m: not m.bot, members))
    if not humans:
        return None

    return choice(humans)
class Countdown:

    def __init__(self, timeout):
        self.timeout = timeout
        self.finished = False

    async def start(self):
        await asyncio.sleep(self.timeout)
        self.finished = True



