# ExtremeProUserbot - UserBot
# Copyright (C) 2021 TeamExtremeProUserbot
#
# This file is a part of < https://github.com/TeamExtremeProUserbot/ExtremeProUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamExtremeProUserbot/ExtremeProUserbot/blob/main/LICENSE/>.

from .. import ExtremedB

try:
    eval(ExtremedB.get("WELCOME"))
except BaseException:
    ExtremedB.set("WELCOME", "{}")

try:
    eval(ExtremedB.get("GOODBYE"))
except BaseException:
    ExtremedB.set("GOODBYE", "{}")


def add_welcome(chat, msg, media):
    ok = eval(ExtremedB.get("WELCOME"))
    ok.update({chat: {"welcome": msg, "media": media}})
    return ExtremedB.set("WELCOME", str(ok))


def get_welcome(chat):
    ok = eval(ExtremedB.get("WELCOME"))
    wl = ok.get(chat)
    if wl:
        return wl
    return


def delete_welcome(chat):
    ok = eval(ExtremedB.get("WELCOME"))
    wl = ok.get(chat)
    if wl:
        ok.pop(chat)
        return ExtremedB.set("WELCOME", str(ok))
    return


def add_goodbye(chat, msg, media):
    ok = eval(ExtremedB.get("GOODBYE"))
    ok.update({chat: {"goodbye": msg, "media": media}})
    return ExtremedB.set("GOODBYE", str(ok))


def get_goodbye(chat):
    ok = eval(ExtremedB.get("GOODBYE"))
    wl = ok.get(chat)
    if wl:
        return wl
    return


def delete_goodbye(chat):
    ok = eval(ExtremedB.get("GOODBYE"))
    wl = ok.get(chat)
    if wl:
        ok.pop(chat)
        return ExtremedB.set("GOODBYE", str(ok))
    return
