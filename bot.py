import discord
from discord.ext import commands
import time


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = 'x', intents=intents)
client.remove_command('help')


TOKEN = 'OTQxNTI5NzU0MzM3NzA1OTg1.YgXR6g.S3qhrpW1OOWPgH5Z63RAybMKXp0'

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Azrael'))
    print("sheesh")




@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.message.delete()
    await ctx.send(f'azrael bot has kicked {member}')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.message.delete()
    await ctx.send(f'Azrael bot has banned {member}')

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.message.delete()
            await ctx.send(f'Unbanned {user.mention} ez')
            return
@client.command()
async def help(ctx):
    embed=discord.Embed(title="Created by daddy loris and daddy vac")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/916495446766149752/916524295700758548/image0.jpg?width=485&height=464")
    embed.add_field(name="ㅤ", value="<3• **BAN** | xBan [user]\n<3• **UNBAN** | xUnban [user]\n<3• **KICK** | xUnban [user]\n", inline=False)
    embed.set_footer(text=f"Requested By {ctx.message.author.name}")
    #embed.add_field(name="ㅤ", value="| $Unban [user]", inline=False)
    #embed.add_field(name="ㅤ", value="| $kick [user]", inline=False)

    await ctx.message.delete()
    await ctx.send(embed=embed)






client.run('OTQxNTI5NzU0MzM3NzA1OTg1.YgXR6g.S3qhrpW1OOWPgH5Z63RAybMKXp0')
