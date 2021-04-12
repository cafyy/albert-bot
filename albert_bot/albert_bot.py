import discord
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

    humans = list(filter(lambda m: not m.bot, guild.members))
    chosen = choice(humans)

    await ctx.send(f"Je choisis {chosen.name}")

def run():
    bot.run(BOT_TOKEN)
