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
                   
async def add_bot(bot_token):
    await client.start(bot_token)
    client.me = await client.get_me() 
    client.uid = telethon.utils.get_peer_id(client.me)




# log in
BOT_TOKEN = ExtremedB.get("BOT_TOKEN")
LOGS.info("Starting ExtremeProUserbot...")
try:
    extremepro_bot.asst = TelegramClient(
        "asst-session", api_id=Var.API_ID, api_hash=Var.API_HASH
    ).start(bot_token=BOT_TOKEN)
    asst = extremepro_bot.asst
    LOGS.info("Done, startup completed")
    LOGS.info("UserBot - Started")
except ApiIdInvalidError:
    LOGS.info("Your API ID/API HASH combination is invalid. Kindly recheck.")
    exit(1)
    
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
      

# for userbot
files = sorted(os.listdir("plugins"))
for plugin_name in files:
    try:
        if plugin_name.endswith(".py"):
            load_plugins(plugin_name[:-3])
            if not plugin_name.startswith("__") or plugin_name.startswith("_"):
                LOGS.info(f"ExtremeProUserbot - Official -  Installed - {plugin_name}")
    except Exception:
        LOGS.info(f"ExtremeProUserbot - Official - ERROR - {plugin_name}")
        LOGS.info(str(traceback.print_exc()))



print("ExtremeProUserbot Deployed And Working Fine For Assistance Join @EXTREMEPRO_USERBOT")



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    client.run_until_disconnected()
    extremepro_bot.run_until_disconnected()
