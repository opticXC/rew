import discord
from discord.ext import commands


class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['create_role'])
    @commands.has_permissions(manage_roles=True)
    async def newrole(self, ctx, *, role):
        guild = ctx.guild
        await guild.create_role(name=role)
        await ctx.channel.send(f'created role {role}')

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, member: discord.Member, *, grole):
        user = member
        giverole = grole
        role = discord.utils.get(user.guild.roles, name=giverole)
        await user.add_roles(role)
        await ctx.send(
            f'{user} was given the role {role} by {ctx.message.author}')


def setup(bot):
    bot.add_cog(roles(bot))
