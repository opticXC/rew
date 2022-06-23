import discord
import random
from discord.ext import commands


class text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hello", help="hello", brief="HEllo!!")
    async def hello(self, ctx):
        await ctx.send("Hello!!!")

    @commands.command(name="echo",
                      help="abuses the bot till it speaks what you want it to",
                      brief="repeats anything followed by the command")
    async def echo(self, ctx, *, arg):
        await ctx.send(arg)

    @commands.command(
        aliases=['8b', '8ball'],
        help=
        "makes a sacrifice to the blood god to find the answer to any question",
        brief="8ball")
    async def eightball(self, ctx, *, ask):
        responses = [
            'As I see it, yes', 'Ask again later', 'Better not tell you now',
            'Cannot predict now', 'Concentrate and ask again',
            'Don’t count on it', 'It is certain', 'It is decidedly so',
            'Most likely', 'My reply is no', 'My sources say no',
            'Outlook not so good', 'Outlook good', 'Reply hazy, try again',
            'Signs point to yes', 'Very doubtful', 'Without a doubt', 'Yes',
            'Yes – definitely', 'You may rely on it'
        ]
        await ctx.send(f' Question: {ask} \nAnswer:{random.choice(responses)}')

    @commands.command(name="owo",
                      help="OWO!!!!!!!!!!!!!!!!!!!!!!",
                      brief="OWO!!!!!!!!!")
    async def owo(self, ctx):
        await ctx.channel.send("⍬⍹⍬!!!")

    @commands.command(name="nuzzle",
                      help="UWU nuzzles you ",
                      brief="nuzzles you ")
    async def nuzzle(self, ctx):
        await ctx.channel.send("uwu! *nuzzles you*")

    @echo.error
    async def echo_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('please specify something to echo')

    @eightball.error
    async def ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('ask something you stupid bitch')


def setup(bot):
    bot.add_cog(text(bot))
