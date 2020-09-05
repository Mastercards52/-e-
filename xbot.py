import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="2")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Xerium"))
    print("bot is ready")

@bot.event
async def on_member_join (member):
    print(f'{member} has joined a server.')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@bot.command()
async def say(ctx,*,arg):
    if (not ctx.author.guild_permissions.manage_messages):
        return await ctx.send("vous n'avez pas la permissions pour faire cela !")
    await ctx.message.delete()
    await ctx.send(arg)

@bot.command()
async def clear(ctx, amount : int=None):
    if amount is None:
        return await ctx.send("Il faut un montant apres le clear!")
    await ctx.channel.purge(limit=amount)
@bot.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    if (not ctx.author.guild_permissions.manage_messages):
        return await ctx.send("vous n'avez pas la permission pour faire cela !")
    await member.kick(reason=reason)
    await ctx.send(f'{member} a été expulsé(e) du serveur')
@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    if (not ctx.author.guild_permissions.manage_messages):
        return await ctx.send("vous n'avez pas la permission pour faire cela !")
    await member.ban(reason=reason)
    await ctx.send(f'{member} a été banni(e) du serveur')
@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{member} a été débanni(e) du serveur')
            return
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send("tu as chargé le cogs!")
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send("tu as déchargé le cogs!")
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run("NzUwMzI5OTgxMzA5MDI2Mzc0.X049QA.4wE-JaSE6d_CZBcFuCMbV240lF8")
