import discord
import os
import json

from dotenv import load_dotenv
from contrun import contr
from discord.ext import commands


load_dotenv()
client = os.environ['CLIENT']


def get_prefix(bot, messages):
    with open('prefix.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(messages.guild.id)]


bot = commands.Bot(command_prefix=get_prefix)


def is_me(ctx):
    return ctx.message.author.id == 742055931193458739


@bot.event
async def on_ready():
    for filename in os.listdir("./cogs"):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
    print(f'{bot.user} has connected')
    activity = discord.Game(name=f"with 0X00012b3", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)


@bot.event
async def on_guild_join(guild):
    with open('prefix.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '-'

    with open('prefix.json', 'w') as f:
        json.dump(prefixes, f, indent=4)


@bot.event
async def on_guild_remove(guild):
    with open('prefix.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefix.json', 'w') as f:
        json.dump(prefixes, f, indent=4)



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('that isnt even a command you dumbfuck')


@bot.command(name="ping",
             help="shows ping in milliseconds",
             brief="shows ping")
async def ping(ctx):
    await ctx.send(f'pong! {round(bot.latency *1000)}ms')


@bot.command()
async def whois(ctx, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(),
                          timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(
        name="Created Account On:",
        value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(
        name="Joined Server On:",
        value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:",
                    value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)


@bot.command(name='invite',
            description='Create an invite link',
            help='creates an instant invite valid for 5 minutes',
            brief="instant invite for current channel"
            )
async def invite(ctx):

    invite = await ctx.channel.create_invite(max_age = 300)
    await ctx.send(invite)



contr()
bot.run(client)
