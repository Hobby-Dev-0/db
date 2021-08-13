# ExtremeProUserbot - UserBot
# Copyright (C) 2021 TeamExtremeProUserbot
#
# This file is a part of < https://github.com/TeamExtremeProUserbot/ExtremeProUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamExtremeProUserbot/ExtremeProUserbot/blob/main/LICENSE/>.

from .. import ExtremedB

try:
    eval(ExtremedB.get("ECHO"))
except BaseException:
    ExtremedB.set("ECHO", "{}")


def add_echo(chat, user):
    x = eval(ExtremedB.get("ECHO"))
    try:
        k = x[chat]
        if user not in k:
            k.append(user)
        x.update({chat: k})
    except BaseException:
        x.update({chat: [user]})
    return ExtremedB.set("ECHO", str(x))


def rem_echo(chat, user):
    x = eval(ExtremedB.get("ECHO"))
    try:
        k = x[chat]
        if user in k:
            k.remove(user)
        x.update({chat: k})
    except BaseException:
        pass
    return ExtremedB.set("ECHO", str(x))


def check_echo(chat, user):
    x = eval(ExtremedB.get("ECHO"))
    try:
        k = x[chat]
        if user in k:
            return True
        return
    except BaseException:
        return


def list_echo(chat):
    x = eval(ExtremedB.get("ECHO"))
    try:
        k = x[chat]
        return k
    except BaseException:
        return
