import discord
from discord.ext import commands
import random


class randoms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="NOICE", brief="NOICE")
    async def noice(self, ctx):
        await ctx.channel.send("<:noice:822373741732298752>")

    @commands.command(help="ZA WARUDO!!!", brief="ZA WARUDO!!!")
    async def timestop(self, ctx):
        embed = discord.Embed()
        embed.set_image(
            url=
            'https://cdn.discordapp.com/attachments/821380330262102096/821380379638366208/tenor_1.gif'
        )
        await ctx.send(embed=embed)

    @commands.command(help="its walter what more do you wanna know?",
                      brief="walter")
    async def walter(self, ctx):
        embed = discord.Embed()
        embed.set_image(
            url=
            'https://media.discordapp.net/attachments/821380330262102096/824227155462193202/795638996877049876.png'
        )
        await ctx.send(embed=embed)

    @commands.command(help="use if somebody commits cringe",
                      brief=" is that cring i see")
    async def cringe(self, ctx):
        embed = discord.Embed()
        embed.set_image(
            url=
            'https://media.discordapp.net/attachments/821380330262102096/824227230782849044/image0.gif'
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(randoms(bot))
