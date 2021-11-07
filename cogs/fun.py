import os
import random
from io import BytesIO

import discord
from discord.ext import commands
import pytz
from PIL import Image, ImageSequence
import requests

from constants import TIMEZONE


tz = pytz.timezone(TIMEZONE)

class Fun(commands.Cog, name="fun"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def highfive(self, ctx, target: discord.Member = None):
        response = requests.get("https://api.waifu.pics/sfw/highfive")
        embed = discord.Embed(title=f"- {ctx.author.name.lower()} high fives {target.display_name.lower()}", color=0x36b8c9)
        embed.set_image(url=response.json()["url"])
        await ctx.send(embed=embed)
    
    @commands.command()
    async def bonk(self, ctx, target: discord.Member = None):
        response = requests.get("https://api.waifu.pics/sfw/bonk")
        embed = discord.Embed(title=f"- {ctx.author.name.lower()} bonks {target.display_name.lower()}", color=0x8e36c9)
        embed.set_image(url=response.json()["url"])
        await ctx.send(embed=embed)
    
    @commands.command()
    async def slap(self, ctx, target: discord.Member = None):
        response = requests.get("https://api.waifu.pics/sfw/slap")
        embed = discord.Embed(title=f"- {ctx.author.name.lower()} slaps {target.display_name.lower()}", color=0xc93636)
        embed.set_image(url=response.json()["url"])
        await ctx.send(embed=embed)
    
    @commands.command()
    async def hug(self, ctx, target: discord.Member = None):
        if random.randrange(0, 2) == 0:
            response = requests.get("https://api.waifu.pics/sfw/glomp")
        else:
            response = requests.get("https://api.waifu.pics/sfw/hug")
        embed = discord.Embed(title=f"- {ctx.author.name.lower()} hugs {target.display_name.lower()}", color=0xc93684)
        embed.set_image(url=response.json()["url"])
        await ctx.send(embed=embed)
    
    @commands.command()
    async def wave(self, ctx, target: discord.Member = None):
        response = requests.get("https://api.waifu.pics/sfw/wave")
        embed = discord.Embed(title=f"- {ctx.author.name.lower()} waves at {target.display_name.lower()}", color=0x38c936)
        embed.set_image(url=response.json()["url"])
        await ctx.send(embed=embed)

        

        

def setup(bot):
    bot.add_cog(Fun(bot))