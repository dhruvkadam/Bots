import random
import discord
from discord.ext import commands

custom = commands.Bot(command_prefix = '!')


 
tags =["anish ke saath sex karta hai  ","upar vishwesh neeche ","fuck yourself ","You deep-throat ","tere gaand me ungli ","tatto ka shawkeen ","mutthal ","hasthmaithoon "]




@custom.command()
async def name(ctx,arg):

    f= str(random.choice(tags)) + arg
    await ctx.send(f)

custom.run('Nzg0ODU1NzEyODY1NTgzMTA1.X8vX1w.npye336Cu2dY7frxYImn69x6fls')