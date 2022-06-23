import json
from sys import prefix
import discord
import random
import aiohttp
from discord.ext import commands


class reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.command(help= "Show images from any subreddit \n -sbr *subreddit* (!!!!CASESENSITIVE!!!!)  ",
                    brief = "show images from any subreddit")
    async def sbr(self,ctx, sbr):
        embed = discord.Embed()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    f'https://www.reddit.com/r/{sbr}/new.json?sort=hot') as r:
                res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]
                            ['data']['url'])
            await ctx.send(embed=embed)
        

    @commands.command(help="shows memes from r/dankmemes ",
                      brief="shows memes from r/dankmemes ")
    async def meme(self, ctx):
        embed = discord.Embed()

        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    'https://www.reddit.com/r/memes/new.json?sort=hot') as r:
                res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]
                            ['data']['url'])
            await ctx.send(embed=embed)

    @commands.command(help="shows memes from r/dankmemes ",
                      brief="shows memes from r/dankmemes ")
    async def dankmeme(self, ctx):
        embed = discord.Embed()

        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    'https://www.reddit.com/r/dankmemes/new.json?sort=hot'
            ) as r:
                res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]
                            ['data']['url'])
            await ctx.send(embed=embed)

    @commands.command(help=" shows an image from r/aww", brief="r/aww")
    async def aww(self, ctx):
        embed = discord.Embed()

        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    'https://www.reddit.com/r/aww/new.json?sort=hot') as r:
                res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]
                            ['data']['url'])
            await ctx.send(embed=embed)

    @commands.command(aliases=['eb', 'eyebleach'],
                      help="shows an image from r/eyebleach",
                      brief="r/eyebleach")
    async def bleach(self, ctx):
        embed = discord.Embed()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    'https://www.reddit.com/r/Eyebleach/new.json?sort=hot'
            ) as r:
                res = await r.json()
        embed.set_image(
            url=res['data']['children'][random.randint(0, 25)]['data']['url'])
        await ctx.send(embed=embed)

    @commands.command(help="shows posts from r/howistwitterfree ",
                      brief=" how is twitter free")
    async def tf(self, ctx):
        embed = discord.Embed()

        async with aiohttp.ClientSession() as cs:

            async with cs.get(
                    'https://www.reddit.com/r/howistwitterfree/new.json?sort=hot'
            ) as r:
                res = await r.json()
        embed.set_image(
            url=res['data']['children'][random.randint(0, 25)]['data']['url'])
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(reddit(bot))
