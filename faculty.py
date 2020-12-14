import random
import discord
from discord.ext import commands

custom = commands.Bot(command_prefix = '!')


 
tags =[Random abuse list]




@custom.command()
async def name(ctx,arg):

    f= str(random.choice(tags)) + arg
    await ctx.send(f)

custom.run('Token')
