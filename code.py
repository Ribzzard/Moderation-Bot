import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix="?")

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  

    if bannedwords != None:
      for blacklistedword in bannedwords:
        if message.content.lower() == blacklistedword:
          await message.delete()
          await message.channel.send(f"{message.author.mention} watch your language!",delete_after=5.0)
    await bot.process_commands(message)

    


#BAN

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, Member : discord.Member, *, reason=None):
	if reason == None:
		 reason = f"{Member} banned by {ctx.author}"
	if ctx.author.top_role < Member.top_role:
	  await ctx.send("Your role is not high enough to ban that user.")
	if ctx.author.top_role > Member.top_role:
		await ctx.guild.ban(Member, reason=reason)
		await ctx.send(f"{Member} banned by {ctx.author.mention}.")


#KICK
    
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, Member : discord.Member, *, reason=None):
	if reason == None:
		 reason = f"{Member} kicked by {ctx.author}"
	if ctx.author.top_role < Member.top_role:
	  await ctx.send("Your role is not high enough to kick that user.")
	if ctx.author.top_role > Member.top_role:
		await ctx.guild.ban(Member, reason=reason)
		await ctx.send(f"{Member} kicked by {ctx.author.mention}.")
 

#BOTINFO
@bot.command()
async def botinfo(ctx):
  
  botinfoembed = discord.Embed(title="Bot Information" , description="Everything about this bot",color=0x52ebf7)
  botinfoembed.add_field(name="About me",value="I am an open-source moderation bot.",inline=False)
  botinfoembed.add_field(name="Prefix",value="My prefix is '?' ",inline=False)
  botinfoembed.add_field(name="Developer",value="Developed by Ribzzard#1338",inline=False)
  botinfoembed.add_field(name="Source for anyone interested",value="<GITHUB SOURCE>",inline=False)
  
  await ctx.send(embed=botinfoembed)


#RULES

async def rules(ctx):
  rulesembed = discord.Embed(title="Rules", description = "This server's rules",color = 0x00ff0)
  rulesembed.add_field(name="Rule 1",value=" Treat everyone with respect. Absolutely no harassment, racism, or hate speech will be tolerated.",inline=False)
  rulesembed.add_field(name="Rule 2",value="No spam or self-promotion (server invites, advertisements, etc) without permission from a staff member. This includes DMing fellow members.",inline=False)
  rulesembed.add_field(name="Rule 3",value="Do not mini-mod. (moderating other users in any way)",inline=False)
  rulesembed.add_field(name="Rule 4",value="No NSFW or obscense content in any way or any form.",inline=False)
  rulesembed.add_field(name="Rule 5",value="Do not spam or type in all-caps or ping continuosly",inline=False)
  rulesembed.add_field(name="Rule 6",value="Sending viruses and malware will result in a ban and getting you reported.",inline=False)
  rulesembed.add_field(name="Rule 7",value="Listen to moderators and do not cause drama",inline=False)
  rulesembed.add_field(name="Rule 8",value="If you see anything against the rules or something that makes you feel unsafe, let the satff know. We want this server to be a welcoming space!",inline=False)
  await ctx.send(embed=rulesembed)


@bot.command()
@commands.has_permissions(administrator=True)
async def addbannedword(ctx,word):
  if word.lower() in bannedwords:
    await ctx.message.delete()
    await ctx.send("This word is already banned.",delete_after = 5.0)
  else:
    bannedwords.append(word.lower())
    await ctx.message.delete()
    await ctx.send("Word added to banned words.",delete_after = 5.0)

@bot.command()
@commands.has_permissions(administrator=True)
async def removebannedword(ctx,word):
  if word.lower() in bannedwords:
    bannedwords.remove(word.lower())
    await ctx.message.delete()
    await ctx.send("Word removed from banned words.",delete_after=5.0)
  else:
    await ctx.message.delet()
    await ctx.send("This word is not in the banned words.",delete_after=5.0)


bannedwords = []

  
bot.run(os.getenv('TOKEN'))
