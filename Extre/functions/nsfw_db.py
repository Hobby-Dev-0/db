# ExtremeProUserbot - UserBot
# Copyright (C) 2021 TeamExtremeProUserbot
#
# This file is a part of < https://github.com/TeamExtremeProUserbot/ExtremeProUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamExtremeProUserbot/ExtremeProUserbot/blob/main/LICENSE/>.


from .. import ExtremedB

try:
    eval(ExtremedB.get("NSFW"))
except BaseException:
    ExtremedB.set("NSFW", "{}")
try:
    eval(ExtremedB.get("PROFANITY"))
except BaseException:
    ExtremedB.set("PROFANITY", "{}")


def nsfw_chat(chat, action):
    x = eval(ExtremedB.get("NSFW"))
    x.update({chat: action})
    return ExtremedB.set("NSFW", str(x))


def rem_nsfw(chat):
    x = eval(ExtremedB.get("NSFW"))
    if x.get(chat):
        x.pop(chat)
        return ExtremedB.set("NSFW", str(x))
    return


def is_nsfw(chat):
    x = eval(ExtremedB.get("NSFW"))
    if x.get(chat):
        return x[chat]
    return


def profan_chat(chat, action):
    x = eval(ExtremedB.get("PROFANITY"))
    x.update({chat: action})
    return ExtremedB.set("PROFANITY", str(x))


def rem_profan(chat):
    x = eval(ExtremedB.get("PROFANITY"))
    if x.get(chat):
        x.pop(chat)
        return ExtremedB.set("PROFANITY", str(x))
    return


def is_profan(chat):
    x = eval(ExtremedB.get("PROFANITY"))
    if x.get(chat):
        return x[chat]
    return
