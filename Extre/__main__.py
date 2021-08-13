# ExtremeProUserbot - UserBot
# Copyright (C) 2021 TeamExtremeProUserbot
#
# This file is a part of < https://github.com/TeamExtremeProUserbot/ExtremeProUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamExtremeProUserbot/ExtremeProUserbot/blob/main/LICENSE/>.

import asyncio
import os
import time
import traceback
import urllib
from pathlib import Path
from random import randint
from urllib.request import urlretrieve

import telethon.utils
from pytz import timezone
from telethon import TelegramClient
from telethon import __version__ as vers
from telethon.errors.rpcerrorlist import (
    AccessTokenExpiredError,
    ApiIdInvalidError,
    AuthKeyDuplicatedError,
    ChannelsTooMuchError,
    PhoneNumberInvalidError,
)
from telethon.tl.custom import Button
from telethon.tl.functions.channels import (
    CreateChannelRequest,
    EditAdminRequest,
    EditPhotoRequest,
    JoinChannelRequest,
)
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.types import (
    ChatAdminRights,
    InputChatUploadedPhoto,
    InputMessagesFilterDocument,
)

from . import *
from .dB import DEVLIST
from .dB.database import Var
from .functions.all import updater
from .utils import load_assistant, load_plugins, load_pmbot
from .version import __version__ as ver

x = ["resources/auths", "resources/downloads", "addons"]
for x in x:
    if not os.path.isdir(x):
        os.mkdir(x)

if ExtremedB.get("CUSTOM_THUMBNAIL"):
    urlretrieve(ExtremedB.get("CUSTOM_THUMBNAIL"), "resources/extras/extremepro.jpg")

if ExtremedB.get("GDRIVE_TOKEN"):
    with open("resources/auths/auth_token.txt", "w") as t_file:
        t_file.write(ExtremedB.get("GDRIVE_TOKEN"))

if ExtremedB.get("MEGA_MAIL") and ExtremedB.get("MEGA_PASS"):
    with open(".megarc", "w") as mega:
        mega.write(
            f'[Login]\nUsername = {ExtremedB.get("MEGA_MAIL")}\nPassword = {ExtremedB.get("MEGA_PASS")}'
        )

if ExtremedB.get("TIMEZONE"):
    try:
        timezone(ExtremedB.get("TIMEZONE"))
        os.environ["TZ"] = timezone(ExtremedB.get("TIMEZONE"))
        time.tzset()
    except BaseException:
        LOGS.info(
            "Incorrect Timezone ,\nCheck Available Timezone From Here https://telegra.ph/ExtremeProUserbot-06-18-2\nSo Time is Default UTC"
        )
        os.environ["TZ"] = "UTC"
        time.tzset()


async def autobot():
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


if not ExtremedB.get("BOT_TOKEN"):
    extremepro_bot.loop.run_until_complete(autobot())


async def istart(ult):
    await extremepro_bot.start(ult)
    extremepro_bot.me = await extremepro_bot.get_me()
    extremepro_bot.uid = telethon.utils.get_peer_id(extremepro_bot.me)
    extremepro_bot.first_name = extremepro_bot.me.first_name
    if not extremepro_bot.me.bot:
        ExtremedB.set("OWNER_ID", extremepro_bot.uid)


async def autopilot():
    await extremepro_bot.start()
    if Var.LOG_CHANNEL and str(Var.LOG_CHANNEL).startswith("-100"):
        ExtremedB.set("LOG_CHANNEL", str(Var.LOG_CHANNEL))
    k = []  # To Refresh private ids
    async for x in extremepro_bot.iter_dialogs():
        k.append(x.id)
    if ExtremedB.get("LOG_CHANNEL"):
        try:
            await extremepro_bot.get_entity(int(ExtremedB.get("LOG_CHANNEL")))
            return
        except BaseException:
            ExtremedB.delete("LOG_CHANNEL")
    try:
        r = await extremepro_bot(
            CreateChannelRequest(
                title="My ExtremeProUserbot Logs",
                about="My ExtremeProUserbot Log Group\n\n Join @TeamExtremeProUserbot",
                megagroup=True,
            ),
        )
    except ChannelsTooMuchError:
        LOGS.info(
            "You Are On Too Many Channels & Groups , Leave some And Restart The Bot"
        )
        exit(1)
    except BaseException:
        LOGS.info(
            "Something Went Wrong , Create A Group and set its id on config var LOG_CHANNEL."
        )
        exit(1)
    chat_id = r.chats[0].id
    if not str(chat_id).startswith("-100"):
        ExtremedB.set("LOG_CHANNEL", "-100" + str(chat_id))
    else:
        ExtremedB.set("LOG_CHANNEL", str(chat_id))
    rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        anonymous=False,
        manage_call=True,
    )
    await extremepro_bot(EditAdminRequest(chat_id, asst.me.username, rights, "Assistant"))
    pfpa = await extremepro_bot.download_profile_photo(chat_id)
    if not pfpa:
        urllib.request.urlretrieve(
            "https://telegra.ph/file/c70894d968a5823d04f0e.png", "channelphoto.png"
        )
        ll = await extremepro_bot.upload_file("channelphoto.png")
        await extremepro_bot(EditPhotoRequest(chat_id, InputChatUploadedPhoto(ll)))
        os.remove("channelphoto.png")
    else:
        os.remove(pfpa)


extremepro_bot.asst = None


async def bot_info(asst):
    await asst.start()
    asst.me = await asst.get_me()
    return asst.me


LOGS.info("Initialising...")
LOGS.info(f"ExtremeProUserbot Version - {ver}")
LOGS.info(f"Telethon Version - {vers}")
LOGS.info("ExtremeProUserbot Version - 0.0.1")


# log in
BOT_TOKEN = ExtremedB.get("BOT_TOKEN")
LOGS.info("Starting ExtremeProUserbot...")
try:
    extremepro_bot.asst = TelegramClient(
        "asst-session", api_id=Var.APP_ID, api_hash=Var.API_HASH
    ).start(bot_token=BOT_TOKEN)
    asst = extremepro_bot.asst
    extremepro_bot.loop.run_until_complete(istart(asst))
    extremepro_bot.loop.run_until_complete(bot_info(asst))
    LOGS.info("Done, startup completed")
    LOGS.info("UserBot - Started")
except AuthKeyDuplicatedError or PhoneNumberInvalidError or EOFError:
    LOGS.info("Session String expired. Please create a new one! ExtremeProUserbot is stopping...")
    exit(1)
except ApiIdInvalidError:
    LOGS.info("Your API ID/API HASH combination is invalid. Kindly recheck.")
    exit(1)
except AccessTokenExpiredError:
    ExtremedB.delete("BOT_TOKEN")
    LOGS.info(
        "BOT_TOKEN expired , So Quitted The Process, Restart Again To create A new Bot. Or Set BOT_TOKEN env In Vars"
    )
    exit(1)
except BaseException:
    LOGS.info("Error: " + str(traceback.print_exc()))
    exit(1)


if str(extremepro_bot.uid) not in DEVLIST:
    chat = eval(ExtremedB.get("BLACKLIST_CHATS"))
    if -1001327032795 not in chat:
        chat.append(-1001327032795)
        ExtremedB.set("BLACKLIST_CHATS", str(chat))

extremepro_bot.loop.run_until_complete(autopilot())

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




async def customize():
    try:
        chat_id = int(ExtremedB.get("LOG_CHANNEL"))
        xx = await extremepro_bot.get_entity(asst.me.username)
        if xx.photo is None:
            LOGS.info("Customising Ur Assistant Bot in @BOTFATHER")
            UL = f"@{asst.me.username}"
            if (extremepro_bot.me.username) is None:
                sir = extremepro_bot.me.first_name
            else:
                sir = f"@{extremepro_bot.me.username}"
            await extremepro_bot.send_message(
                chat_id, "Auto Customisation Started on @botfather"
            )
            await asyncio.sleep(1)
            await extremepro_bot.send_message("botfather", "/cancel")
            await asyncio.sleep(1)
            await extremepro_bot.send_message("botfather", "/start")
            await asyncio.sleep(1)
            await extremepro_bot.send_message("botfather", "/setuserpic")
            await asyncio.sleep(1)
            await extremepro_bot.send_message("botfather", UL)
            await asyncio.sleep(1)
            await extremepro_bot.send_file(
                "botfather", "resources/extras/extremepro_assistant.jpg"
            )
            await asyncio.sleep(2)
            await extremepro_bot.send_message("botfather", "/setabouttext")
            await asyncio.sleep(1)
            await extremepro_bot.send_message("botfather", UL)
            await asyncio.sleep(1)
            await extremepro_bot.send_message(
                "botfather", f"✨ Hello ✨!! I'm Assistant Bot of {sir}"
            )
            await asyncio.sleep(2)
            await extremepro_bot.send_message("botfather", "/setdescription")
            await asyncio.sleep(1)
            await extremepro_bot.send_message("botfather", UL)
            await asyncio.sleep(1)
            await extremepro_bot.send_message(
                "botfather",
                f"✨ PowerFul ExtremeProUserbot Assistant Bot ✨\n✨ Master ~ {sir} ✨\n\n✨ Powered By ~ @TeamExtremeProUserbot ✨",
            )
            await asyncio.sleep(2)
            await extremepro_bot.send_message(
                chat_id, "**Auto Customisation** Done at @BotFather"
            )
            LOGS.info("Customisation Done")
    except Exception as e:
        LOGS.warning(str(e))


# some stuffs
async def ready():
    chat_id = int(ExtremedB.get("LOG_CHANNEL"))
    MSG = f"**ExtremeProUserbot has been deployed!**\n➖➖➖➖➖➖➖➖➖\n**UserMode**: [{extremepro_bot.me.first_name}](tg://user?id={extremepro_bot.me.id})\n**Assistant**: @{asst.me.username}\n➖➖➖➖➖➖➖➖➖\n**Support**: @TeamExtremeProUserbot\n➖➖➖➖➖➖➖➖➖"
    BTTS = [Button.inline("Help", "open")]
    updava = await updater()
    try:
        if updava:
            BTTS = [
                [Button.inline("Update Available", "updtavail")],
                [Button.inline("Help", "open")],
            ]
        await extremepro_bot.asst.send_message(chat_id, MSG, buttons=BTTS)
    except BaseException:
        try:
            await extremepro_bot.send_message(chat_id, MSG)
        except Exception as ef:
            LOGS.info(ef)
    try:
        # To Let Them know About New Updates and Changes
        await extremepro_bot(JoinChannelRequest("@Andencento"))
    except BaseException:
        pass


ws = f"WEBSOCKET_URL=http://localhost:6969"
lg = f"LOG_CHANNEL={ExtremedB.get('LOG_CHANNEL')}"
bt = f"BOT_TOKEN={ExtremedB.get('BOT_TOKEN')}"
try:
    with open(".env", "r") as x:
        m = x.read()
    if "WEBSOCKET_URL" not in m:
        with open(".env", "a+") as t:
            t.write("\n" + ws)
    if "LOG_CHANNEL" not in m:
        with open(".env", "a+") as t:
            t.write("\n" + lg)
    if "BOT_TOKEN" not in m:
        with open(".env", "a+") as t:
            t.write("\n" + bt)
except BaseException:
    with open(".env", "w") as t:
        t.write(ws + "\n" + lg + "\n" + bt)


extremepro_bot.loop.run_until_complete(customize())

LOGS.info(
    """
                ----------------------------------------------------------------------
                    ExtremeProUserbot has been deployed! Visit @TheExtremeProUserbot for updates!!
                ----------------------------------------------------------------------
"""
)


extremepro_bot.run_until_disconnected()
