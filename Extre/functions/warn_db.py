# ExtremeProUserbot - UserBot
# Copyright (C) 2021 TeamExtremeProUserbot
#
# This file is a part of < https://github.com/TeamExtremeProUserbot/ExtremeProUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamExtremeProUserbot/ExtremeProUserbot/blob/main/LICENSE/>.

from .. import ExtremedB

try:
    eval(ExtremedB.get("WARNS"))
except BaseException:
    ExtremedB.set("WARNS", "{}")


def add_warn(chat, user, count, reason):
    x = eval(ExtremedB.get("WARNS"))
    try:
        x[chat].update({user: [count, reason]})
    except BaseException:
        x.update({chat: {user: [count, reason]}})
    return ExtremedB.set("WARNS", str(x))


def warns(chat, user):
    x = eval(ExtremedB.get("WARNS"))
    try:
        count, reason = x[chat][user][0], x[chat][user][1]
        return count, reason
    except BaseException:
        return 0, None


def reset_warn(chat, user):
    x = eval(ExtremedB.get("WARNS"))
    try:
        x[chat].pop(user)
        return ExtremedB.set("WARNS", str(x))
    except BaseException:
        return
