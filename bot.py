import discord
from discord.ext import commands
from discord.ui import Button
import random
import json
import os
import time
import random
from dotenv import load_dotenv
load_dotenv()


with open('./setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()
bot = commands.Bot(intents=intents, command_prefix='.')
MAX_GUESS = 10
flag = True
ans_list = []
guess_list = []


@bot.event  # 開機
async def on_ready():
    print(">>", bot.user, "is online <<")
    game = discord.Game('匿名發文:)')
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command()  # 指令 - ping(延遲確認)
async def ping(ctx):
    """
    輸入這個指令可以讓您確認機器人是否在線！
    也可以知道您與機器人的延遲。
    """
    lag = int(bot.latency*1000)
    await ctx.send(f"pong! {lag}(ms)")
    # await ctx.send("%s %d%s" % ("pong! " + str(int(bot.latency*1000)) + "(ms)"))

@commands.has_permissions(administrator=True)
@bot.command()  # 指令 - say(複誦)
async def say(ctx, *, msg):
    """
    機器人會代替你說話
    """
    if "@everyone" in msg or "@here" in msg:
        await ctx.message.delete()
        await ctx.send("字串內包含非法文字")
    else:
        await ctx.message.delete()
        await ctx.send(msg)

@bot.command()
async def clear(ctx, num: int):
    """
    [管理員專用]
    可以批量刪除訊息
    """
    await ctx.channel.purge(limit=num + 1)

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


bot.run(os.getenv('TOKEN'))
