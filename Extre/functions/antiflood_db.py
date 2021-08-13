# ExtremeProUserbot - UserBot
# Copyright (C) 2021 TeamExtremeProUserbot
#
# This file is a part of < https://github.com/TeamExtremeProUserbot/ExtremeProUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamExtremeProUserbot/ExtremeProUserbot/blob/main/LICENSE/>.

import ast

from .. import ExtremedB


def get_flood():
    n = []
    if ExtremedB.get("ANTIFLOOD"):
        n.append(ast.literal_eval(ExtremedB.get("ANTIFLOOD")))
        return n[0]
    else:
        return {}


def set_flood(chat_id, limit):
    omk = get_flood()
    omk[int(chat_id)] = int(limit)
    ExtremedB.set("ANTIFLOOD", str(omk))
    return True


def get_flood_limit(chat_id):
    omk = get_flood()
    if int(chat_id) in omk.keys():
        return omk[int(chat_id)]
    else:
        return None


def rem_flood(chat_id):
    omk = get_flood()
    if int(chat_id) in omk.keys():
        try:
            del omk[int(chat_id)]
            ExtremedB.set("ANTIFLOOD", str(omk))
            return True
        except KeyError:
            return False
    else:
        return None
