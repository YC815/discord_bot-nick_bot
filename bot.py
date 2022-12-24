from dotenv import load_dotenv
import os
from datetime import datetime
import discord
from discord.ext import commands
import pycord
import json
load_dotenv()
intents = discord.Intents.all()
bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


# @bot.slash_command()
# async def ping(ctx):
#     """
#     可以查看機器人的延遲
#     """
#     lag = int(bot.latency*1000)
#     await ctx.respond(f"pong! {lag}(ms)")


# @bot.slash_command()  # 指令 - say(複誦)
# async def say(ctx, *, msg):
#     """
#     [管理員專用]
#     機器人會代替你說話
#     @msg: 機器人要代替你說的話
#     """
#     await ctx.respond(msg)


# @bot.slash_command()
# async def help(ctx):
#     """
#     獲取幫助
#     """
#     embed = discord.Embed(
#         title="獲取指令幫助", description="查看酒吧管理員的服務內容", color=0x18d6fb)
#     embed.add_field(name="help", value="可以查看此指令", inline=False)
#     embed.add_field(name="ping", value="可以查看您與酒吧管理員之間的延遲", inline=False)
#     # embed.add_field(name="say", value="[管理員專用]", inline=False)
#     await ctx.respond(embed=embed)


@bot.event
async def on_message(message):
    if message.channel.type == discord.ChannelType.private:
        msg = message.content
        channel = bot.get_channel(int(1051043085666242610))
        with open('nick_msg_count.json', 'r') as openfile:
            cj = json.load(openfile)
        title = "nick-" + str(cj["count"])
        await channel.create_thread(name=title, content=str(msg))
        cj["count"] += 1
        with open('nick_msg_count.json', 'w') as outfile:
            json.dump(cj, outfile)


# @bot.event
# async def on_message(message):
#     if message.channel.type == discord.ChannelType.private:
#         msg = message.content
#         time = datetime.today().strftime('%Y-%m-%d')
#         title = "nick-" + str(time)
#         channel = bot.get_channel(int(1051043085666242610))
#         await channel.create_thread(name=title, content=str(msg))

bot.run(os.getenv('TOKEN'))
