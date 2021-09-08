import discord
from discord.ext import commands, tasks
from discord import FFmpegPCMAudio
from discord.utils import get


#istall FFmpegPCMAudio https://www.ffmpeg.org/download.html
#to avoid problems the mp3s have to be in the same folder as the script

#Bot commands prefix
bot=commands.Bot(command_prefix = "/")

#Check Bot status
@bot.event
async def on_ready():		#status													#Message
	await bot.change_presence(status=discord.Status.idle ,activity=discord.Game("version 1.1.2"))
	print("bot:ok")

#Show list of the names of mp3 files
@bot.command()
async def bt(ctx):
	await ctx.send("/b : Name0, Name1, Name2") #Names of the files, whitout ".mp3"


#Activate Sound
@bot.command()
async def b(ctx, name):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("you are not on the voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio(name+".mp3")
    player = voice.play(source) 

bot.run("Token")


#Example

# /bt show:  "/b : Hello, Goodbye, Nice, Hi"

#/b Hello: play "Hello.mp3"