import discord
import json
from discord.ext import commands


class moderation(commands.Cog):
    def __init__(self, bot):

        self.bot = bot

    def is_me(self, ctx):
        return ctx.message.author.id == 742055931193458739

    @commands.command(help="sets new prefix for server",
                      brief="change server prefix")
    @commands.has_permissions(administrator=True)
    async def newprefix(self, ctx, newprefix):
        with open('prefix.json', 'r') as f:
            prefixes = json.load(f)
		

        prefixes[str(ctx.guild.id)] = newprefix

        with open('prefix.json', 'w') as f:
            json.dump(prefixes, f, indent=4)
        await ctx.send(f'command prefix changed to : {newprefix}')

    @newprefix.error
    async def newpre_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.send('specify a new prefix')

    @commands.command(
        aliases=['purge'],
        help="clears a specified number of messages in current channel",
        brief="purge the sinners")
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, range=5):
        await ctx.channel.purge(limit=range)
        await ctx.channel.send(f'{range} message(s)have been purged')

    @commands.command(help="kicks specified member from server )",
                      brief="kick a member")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reas=None):
        await member.kick(reason=reas)
        await ctx.channel.send(f'{member.mention} has been kicked')

    @commands.command(help="ban specified member from server )",
                      brief="ban a member")
    @commands.has_permissions(kick_members=True)
    async def ban(self, ctx, member: discord.Member, *, reas=None):
        await member.ban(reason=reas)
        await ctx.channel.send(f'{member.mention} has been banned')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('mention someone to kick')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('mention someone to ban')

    @commands.command(help="deletes current channel",
                      breif="deletes current channel")
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, ctx, ch_name):
        guild = ctx.message.guild
        channel_name = discord.utils.get(guild.channels, name=ch_name)

        await channel_name.delete()

    @nuke.error
    async def nuke_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("you don't have perms for that")


def setup(bot):
    bot.add_cog(moderation(bot))
