# ExtremeProUserbot - UserBot
# Copyright (C) 2021 TeamExtremeProUserbot
#
# This file is a part of < https://github.com/TeamExtremeProUserbot/ExtremeProUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamExtremeProUserbot/ExtremeProUserbot/blob/main/LICENSE/>.


from .. import ExtremedB

try:
    eval(ExtremedB.get("BOTCHAT"))
except BaseException:
    ExtremedB.set("BOTCHAT", "{}")


def add_stuff(msg_id, user_id):
    ok = eval(ExtremedB.get("BOTCHAT"))
    ok.update({msg_id: user_id})
    ExtremedB.set("BOTCHAT", str(ok))


def get_who(msg_id):
    ok = eval(ExtremedB.get("BOTCHAT"))
    try:
        user = ok.get(msg_id)
        return user
    except BaseException:
        return
