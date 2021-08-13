# ExtremeProUserbot - UserBot
# Copyright (C) 2021 TeamExtremeProUserbot
#
# This file is a part of < https://github.com/TeamExtremeProUserbot/ExtremeProUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamExtremeProUserbot/ExtremeProUserbot/blob/main/LICENSE/>.

import ast

from .. import ExtremedB


def get_chats():
    n = []
    cha = ExtremedB.get("FORCESUB")
    if not cha:
        cha = "{}"
    n.append(ast.literal_eval(cha))
    return n[0]


def add_forcesub(chat_id, chattojoin):
    omk = get_chats()
    omk.update({str(chat_id): str(chattojoin)})
    ExtremedB.set("FORCESUB", str(omk))
    return True


def get_forcesetting(chat_id):
    omk = get_chats()
    if str(chat_id) in omk.keys():
        return omk[str(chat_id)]
    else:
        return None


def rem_forcesub(chat_id):
    omk = get_chats()
    if str(chat_id) in omk.keys():
        try:
            del omk[str(chat_id)]
            ExtremedB.set("FORCESUB", str(omk))
            return True
        except KeyError:
            return False
    else:
        return None
