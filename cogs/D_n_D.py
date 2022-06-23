import discord
import random
from discord.ext import commands

#6 sided die emoji start
die1 = "<:die1:834850199703912510>"
die2 = "<:die2:834850200823791666>"
die3 = "<:die3:834850200693768202>"
die4 = "<:die4:834850202446987285>"
die5 = "<:die5:834850204339011604>"
die6 = "<:die6:834850205185605722>"
#6 sided die emoji end

class D_n_D(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(
                aliases=['d6', 'roll6'],
                help="rolls a classic 6 sided dice",
                breif="rolls a classic 6 sided dice"
                )
    async def dice(self, ctx):
        Dice = [ die1, die2, die3, die4, die5, die6]
        out = random.choice(Dice)
        await ctx.send(f"{ctx.author.name} rolled a die \nOutcomes: {out} ")

    @commands.command(aliases=['roll2'],
                help="rolls a pair of  6 sided dice"
                )
    async def d2(self, ctx):
        Dice = [ die1, die2, die3, die4, die5, die6]
        out = random.choice(Dice)
        out1 = random.choice(Dice)
        await ctx.send(f"{ctx.author.name} rolled two dice \nOutcomes: {out} {out1} ")

    @commands.command(aliases=['roll4']
                    ,help="rolls a 4 sided dice")
    async def d4(self, ctx):
        Dice = [ die1, die2, die3, die4

        ]
        out = random.choice(Dice)
        await ctx.channel.send(f"{ctx.author.name} rolled a 4 sided dice \nOutcome: {out} ")



def setup(bot):
    bot.add_cog(D_n_D(bot))