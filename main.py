import discord
from time import sleep
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command()
async def echo(ctx, arg):
	msg = await ctx.send(arg)
	sleep(1)
	await msg.edit(content = 'Изменил')

@bot.command()
async def rr(ctx):
	await ctx.send(content = 'https://youtu.be/dQw4w9WgXcQ?list=PLneRaqXoYlV10RUsU6uP-6cicVmwr0g2O')

bot.run(settings['token'])