# ExtremeProUserbot - UserBot
# Copyright (C) 2021 TeamExtremeProUserbot
#
# This file is a part of < https://github.com/TeamExtremeProUserbot/ExtremeProUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamExtremeProUserbot/ExtremeProUserbot/blob/main/LICENSE/>.

from .. import ExtremedB


def str_to_list(text):
    return text.split(" ")


def list_to_str(list):
    str = ""
    for x in list:
        str += f"{x} "
    return str.strip()


def gbanned_user():
    gbun = ExtremedB.get("GBAN")
    if gbun is None or gbun == "":
        return [""]
    else:
        return str_to_list(gbun)


def is_gbanned(id):
    id = str(id)
    if not id.isdigit():
        return False
    gbun = gbanned_user()
    if str(id) in gbun:
        return True
    else:
        return False


def gban(id):
    id = str(id)
    if not id.isdigit():
        return False
    try:
        gbun = gbanned_user()
        gbun.append(id)
        ExtremedB.set("GBAN", list_to_str(gbun))
        return True
    except BaseException:
        return False


def ungban(id):
    id = str(id)
    if not id.isdigit():
        return False
    try:
        gbun = gbanned_user()
        gbun.remove(id)
        ExtremedB.set("GBAN", list_to_str(gbun))
        return True
    except Exception:
        return False


def get_gban_reason(uid):
    return ExtremedB.get(f"GBAN_REASON_{uid}")


def delete_gban_reason(uid):
    ExtremedB.delete(f"GBAN_REASON_{uid}")


def add_gban_reason(uid, reason):
    ExtremedB.set(f"GBAN_REASON_{uid}", reason)


def gmuted_user():
    gmute = ExtremedB.get("GMUTE")
    if gmute is None or gmute == "":
        return [""]
    else:
        return str_to_list(gmute)


def is_gmuted(id):
    id = str(id)
    if not id.isdigit():
        return False
    gmute = gmuted_user()
    if str(id) in gmute:
        return True
    else:
        return False


def gmute(id):
    id = str(id)
    if not id.isdigit():
        return False
    try:
        gmute = gmuted_user()
        gmute.append(id)
        ExtremedB.set("GMUTE", list_to_str(gmute))
        return True
    except BaseException:
        return False


def ungmute(id):
    id = str(id)
    if not id.isdigit():
        return False
    try:
        gmute = gmuted_user()
        gmute.remove(id)
        ExtremedB.set("GMUTE", list_to_str(gmute))
        return True
    except Exception:
        return False
