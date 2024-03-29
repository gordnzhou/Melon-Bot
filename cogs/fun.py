import os
import random
from io import BytesIO

import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord_slash.context import SlashContext
from discord_slash.utils.manage_commands import create_option
from PIL import Image, ImageSequence
import requests

from utils.displays import build_embed


class Fun(commands.Cog, name="fun"):
    def __init__(self, bot):
        self.bot = bot
    
    @cog_ext.cog_slash(
        name="highfive",
        description="High five a user in this server.",
        options=[
            create_option(name="user", description="The target user.", option_type=6, required=True),
        ])
    async def _highfive(self, ctx: SlashContext, user: discord.User):
        response = requests.get("https://api.waifu.pics/sfw/highfive")
        await ctx.reply(embed=build_embed(
            title=f"- **{ctx.author.name} high fives {user.display_name}**",
            img_url=response.json()["url"]
        ))

    @cog_ext.cog_slash(
        name="bonk",
        description="Bonk a user in this server.",
        options=[
            create_option(name="user", description="The target user.", option_type=6, required=True),
        ])
    async def _bonk(self, ctx: SlashContext, user: discord.User):
        response = requests.get("https://api.waifu.pics/sfw/bonk")
        await ctx.reply(embed=build_embed(
            title=f"- **{ctx.author.name} bonks {user.display_name}**",
            img_url=response.json()["url"]
        ))
    
    @cog_ext.cog_slash(
        name="slap",
        description="Slap a user in this server.",
        options=[
            create_option(name="user", description="The target user.", option_type=6, required=True),
        ])
    async def _slap(self, ctx: SlashContext, user: discord.User):
        response = requests.get("https://api.waifu.pics/sfw/slap")
        await ctx.reply(embed=build_embed(
            title=f"- **{ctx.author.name} slaps {user.display_name}**",
            img_url=response.json()["url"]
        ))
    
    @cog_ext.cog_slash(
        name="hug",
        description="Hug a user in this server.",
        options=[
            create_option(name="user", description="The target user.", option_type=6, required=True),
        ])
    async def _hug(self, ctx: SlashContext, user: discord.User):
        responses = [requests.get("https://api.waifu.pics/sfw/glomp"), requests.get("https://api.waifu.pics/sfw/hug")]
        response = responses[random.randrange(0, 2)]
        await ctx.reply(embed=build_embed(
            title=f"- **{ctx.author.name} hugs {user.display_name}**",
            img_url=response.json()["url"]
        ))
    
    @cog_ext.cog_slash(
        name="wave",
        description="Wave to a user in this server.",
        options=[
            create_option(name="user", description="The target user.", option_type=6, required=True),
        ])
    async def _wave(self, ctx: SlashContext, user: discord.User):
        response = requests.get("https://api.waifu.pics/sfw/wave")
        await ctx.reply(embed=build_embed(
            title=f"- **{ctx.author.name} waves at {user.display_name}**",
            img_url=response.json()["url"]
        ))

    @cog_ext.cog_slash(
        name="ohmy",
        description="Creates a custom GIF that depicts the target user's profile image.",
        options=[
            create_option(name="user", description="The target user.", option_type=6, required=True),
        ])
    async def _ohmy(self, ctx: SlashContext, user: discord.User):
        await ctx.defer()
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        final_path = f'temp/ohmygif{user.id}.gif'
        animated_gif = Image.open("media/ohmygoodness.gif")
        img = Image.open(data).convert("RGBA").resize((220, 220), Image.ANTIALIAS)

        frames = []  # adds user profile img to every frame
        for frame in ImageSequence.Iterator(animated_gif):
            frame = frame.copy()
            final_img = Image.new('RGBA', animated_gif.size, (0, 0, 0, 0))
            final_img.paste(frame, (0,0))
            final_img.paste(img, (270,195), mask=img)
            frames.append(final_img)
        frames[0].save(final_path, save_all=True, append_images=frames[1:]) 

        await ctx.reply(file=discord.File(final_path))
        os.remove(final_path)

def setup(bot):
    bot.add_cog(Fun(bot))
