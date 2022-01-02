import discord
import os
import random 
from discord.ext import commands
from keep_alive import keep_alive
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import json

client = commands.Bot(command_prefix = '^')

Cheer = [
  "Cheer up!",
  "Hang in there!",
  "You are a great person / bot!",
  "You can get everything in life you want if you will just help enough other people get what they want.",
  "Keep going. Don't gave up!",
  "Inspiration does exist, but it must find you working.",
  "Don't settle for average.",
  "Show up, show up, show up, and after a while the muse shows up, too.",
  "Don't bunt.",
  "Whenever you need to call, I'm here!",
  "I wish I could be there right now!",
  "You're still in my thoughts!",
  "Your family is lucky to have you through all this!",
  "Maybe I can't be there, but there's definitely something I can do!", 
  "Hey, get well soon!",
  "You're doing a great job with a major responsibility!",
]

embed_1 = (
    ' `^hi`, `^hey`, `^hello` (Intro)\n'
    ' `^rules`\n'
    ' `^invite`\n'
    ' `^helpp`\n'
    ' `^inspire`\n'
    ' `^randome`\n'
    ' `^vote`\n'
    ' `^cheer`\n'
    ' `^ban` <mention someone> (No need type < or >)\n'
    ' `^kick`<mention someone>\n'
    ' `^unban`<Username#UserNumber>\n'
    '---------------\n'
    '  **If you need any help that is not in this list join this server**\n'
    '  **https://discord.gg/SmVpmZEtVX:)**\n'
    )

emoji = ['😀','😃','😄','😁','😆','😅','😂','🤣','🥲','😊','😇','🙂','🙃','😉','😌','😍','🥰','😘','😗','😙','😚','😋','😛','😝','😜','🤪','🤨']

embed_2 = ("**Link** = https://discord.com/api/oauth2/authorize?client_id=902116218050318337&permissions=8&scope=bot\n--------------------\n**I would appriciate if you invite the bot to your server!**")

rules_ = ("\n**1. Follow Discord's TOS**\n"
">    https://discordapp.com/terms\n"
">    https://discordapp.com/guidelines\n"
"**2. Be respectful with all members**\n"
">    Be respectful to others , No death threats, sexism, hate speech, racism (NO N WORD, this includes soft N)\n"
">    No doxxing, swatting, witch hunting\n"
"**3. No Advertising**\n"
">    Includes DM Advertising. We do not allow advertising here of any kind.\n"
"**4. No NSFW content**\n"
">    Anything involving gore or sexual content is not allowed.\n"
">    NSFW = Not Safe for Work\n"
"**5. No spamming in text or VC**\n"
">   Do not spam msgs, soundboards, voice changers, or earrape in any channel.\n"
"**6. Do not discuss about sensitive topics**\n"
">    This isn't a debating server, keep sensitive topics out of here so we don't have a ton of nasty arguments.\n"
"**7. No malicious content**\n"
">    No grabify links, viruses, crash videos, links to viruses, or token grabbers. These will result in an automated ban.\n"
"**8. No Self Bots**\n"
">    Includes all kinds of selfbots: Nitro snipers, selfbots like nighty, auto changing statuses\n"
"**9. Do not DM the staff team** \n"
">    Please open a ticket instead in\n"
"**10. Profile Picture / Banner Rules**\n"
">    No NSFW allowed\n"
">    No racism\n"
">    No brightly flashing pictures to induce an epileptic attack\n"
"**11. Emoji Rules**\n"
">    No NSFW allowed\n"
">    No racism\n"
">    No brightly flashing pictures to induce an epileptic attack\n"
"**12. Use English only**\n"
">    We cannot easily moderate chats in different languages, sorry. English only.\n")

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - by " + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('^helpp'))
  print("Zen-Bot#9261 is ready to use.")
  print("--------------------")

@client.command()
async def inspire (ctx):
  quote = get_quote()
  await ctx.send(quote)

@client.command()
async def rules (ctx):
  await ctx.send(ctx.author.mention + (' ') + ctx.author.name + rules_) 

@client.command()
async def hi (ctx):
  await ctx.send(ctx.author.mention + (' Hello, I am Zen-Bot. Discord Bot which is made for fun. Nice to meet you! Text `^helpp` if you need any help.' )) 

@client.command()
async def hey (ctx):
  await ctx.send(ctx.author.mention + (' Hello, I am Zen-Bot. Discord Bot which is made for fun. Nice to meet you! Text `^help` if you need help.' )) 

@client.command()
async def hello (ctx):
  await ctx.send(ctx.author.mention + (' Hello, I am Zen-Bot. Discord Bot which is made for fun. Nice to meet you! Text `^help` if you need help.' )) 

@client.command()
async def helpp(ctx):
  embed = discord.Embed(title='Bot Commands', url='https://google.com', description=embed_1, color=0x4dff4d)
  embed.set_author(name="Jamie G", url="https://jamie-g.w3spaces.com/", icon_url="https://jamie-g.w3spaces.com/avatar_hat.jpg")
  await ctx.send(embed=embed)

@client.command()
async def randome(ctx):
    random_emoji = random.choice(emoji)
    await ctx.send(random_emoji)

@client.command()
async def invite(ctx):
  embed = discord.Embed(title='Bot Invitation', url='https://google.com', description=embed_2, color=0x4dff4d)
  embed.set_author(name="Jamie G", url="https://jamie-g.w3spaces.com/", icon_url="https://jamie-g.w3spaces.com/avatar_hat.jpg")
  await ctx.send(embed=embed)

@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
	await member.kick(reason=reason)
	await ctx.send(f'User {member} has been kicked!')

@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("You don't have permission to kick people!")

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
	await member.ban(reason=reason)
	await ctx.send(f'User {member} has been banned!')

@ban.error
async def ban_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
	  await ctx.send("You don't have permission to ban people!")

@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.name, user.discriminator) == (member_name, member_discriminator):
			await ctx.guild.unban(user)
			await ctx.send(f'User {user.mention} has been unbanned!')
			return

@client.command()
async def cheer(ctx):
  randomcheer = random.choice(Cheer)
  await ctx.send(ctx.author.mention + (" ") + randomcheer)

keep_alive()
client.run(os.getenv('Hi'))
