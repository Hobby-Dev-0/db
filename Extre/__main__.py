# MADE BY AMAN PANDEY FOR Extre USERBOT DONT KANG. OTHERWISE GET READY FOR COPYRIGHT STRIKE
from Extre import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from Extre import *
from Extre.dB.database import * 
from Extre.utils import load_module
from Extre.utils import start_assistant
from Extre import LOAD_PLUG, BOTLOG_CHATID, LOGS
from Extre import extremepro_bot
from pathlib import Path
import asyncio
import telethon.utils

from .var import Var

async def autobot():
    from .var import Var
    await extremepro_bot.start()
    if Var.BOT_TOKEN:
        ExtremedB.set("BOT_TOKEN", str(Var.BOT_TOKEN))
        return
    if ExtremedB.get("BOT_TOKEN"):
        return
    LOGS.info("MAKING A TELEGRAM BOT FOR YOU AT @BotFather , Please Kindly Wait")
    who = await extremepro_bot.get_me()
    name = who.first_name + "'s Assistant Bot"
    if who.username:
        username = who.username + "_bot"
    else:
        username = "extremepro_" + (str(who.id))[5:] + "_bot"
    bf = "Botfather"
    await extremepro_bot(UnblockRequest(bf))
    await extremepro_bot.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await extremepro_bot.send_message(bf, "/start")
    await asyncio.sleep(1)
    await extremepro_bot.send_message(bf, "/newbot")
    await asyncio.sleep(1)
    isdone = (await extremepro_bot.get_messages(bf, limit=1))[0].text
    if isdone.startswith("That I cannot do."):
        LOGS.info(
            "Please make a Bot from @BotFather and add it's token in BOT_TOKEN, as an env var and restart me."
        )
        exit(1)
    await extremepro_bot.send_message(bf, name)
    await asyncio.sleep(1)
    isdone = (await extremepro_bot.get_messages(bf, limit=1))[0].text
    if not isdone.startswith("Good."):
        await extremepro_bot.send_message(bf, "My Assistant Bot")
        await asyncio.sleep(1)
        isdone = (await extremepro_bot.get_messages(bf, limit=1))[0].text
        if not isdone.startswith("Good."):
            LOGS.info(
                "Please make a Bot from @BotFather and add it's token in BOT_TOKEN, as an env var and restart me."
            )
            exit(1)
    await extremepro_bot.send_message(bf, username)
    await asyncio.sleep(1)
    isdone = (await extremepro_bot.get_messages(bf, limit=1))[0].text
    await extremepro_bot.send_read_acknowledge("botfather")
    if isdone.startswith("Sorry,"):
        ran = randint(1, 100)
        username = "extremepro_" + (str(who.id))[6:] + str(ran) + "_bot"
        await extremepro_bot.send_message(bf, username)
        await asyncio.sleep(1)
        nowdone = (await extremepro_bot.get_messages(bf, limit=1))[0].text
        if nowdone.startswith("Done!"):
            token = nowdone.split("`")[1]
            ExtremedB.set("BOT_TOKEN", token)
            await extremepro_bot.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await extremepro_bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await extremepro_bot.send_message(bf, "Search")
            LOGS.info(f"DONE YOUR TELEGRAM BOT IS CREATED SUCCESSFULLY @{username}")
        else:
            LOGS.info(
                f"Please Delete Some Of your Telegram bots at @Botfather or Set Var BOT_TOKEN with token of a bot"
            )
            exit(1)
    elif isdone.startswith("Done!"):
        token = isdone.split("`")[1]
        ExtremedB.set("BOT_TOKEN", token)
        await extremepro_bot.send_message(bf, "/setinline")
        await asyncio.sleep(1)
        await extremepro_bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await extremepro_bot.send_message(bf, "Search")
        LOGS.info(f"DONE YOUR TELEGRAM BOT IS CREATED SUCCESSFULLY @{username}")
    else:
        LOGS.info(
            f"Please Delete Some Of your Telegram bots at @Botfather or Set Var BOT_TOKEN with token of a bot"
        )
        exit(1)


if not ExtremedB.get("BTOKEN"):
    extremepro_bot.loop.run_until_complete(autobot())

                   
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Connecting To Scratch Server")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Connected To Scratch Server")
    else:
        bot.start()

iampro = os.environ.get("BOT_TOKEN", None)        

if len(argv) not in (1, 3, 4):
    client.disconnect()
else:
    client.tgbot = None
    if iampro is not None:
        print("Connecting To Client 2")
        # ForTheGreatrerGood of beautification
        client.tgbot = TelegramClient(
            "ANDENCENTO",
            api_id=CLIENT_API,
            api_hash=CLIENT_API_HASH
        ).start(bot_token=iampro)
        client.loop.run_until_complete(add_bot(iampro))
        print("Connected To Client 2")
    else:
        print ("Failed to connect client 2")


import glob
path = 'assistant/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))
# ForTheGreatrerGood
      
import glob

path = 'plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))



print("ExtremeProUserbot Deployed And Working Fine For Assistance Join @EXTREMEPRO_USERBOT")



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
    extremepro_bot.run_until_disconnected()
