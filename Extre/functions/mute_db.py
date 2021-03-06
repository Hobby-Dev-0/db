# ExtremeProUserbot - UserBot
# Copyright (C) 2021 TeamExtremeProUserbot
#
# This file is a part of < https://github.com/TeamExtremeProUserbot/ExtremeProUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamExtremeProUserbot/ExtremeProUserbot/blob/main/LICENSE/>.

from .. import ExtremedB


def str_to_list(text):  # Returns List
    return text.split(" ")


def list_to_str(list):  # Returns String
    str = ""
    for x in list:
        str += f"{x} "
    return str.strip()


def get_muted():  # Returns List
    pmperm = ExtremedB.get("MUTE")
    if pmperm is None or pmperm == "":
        return [""]
    else:
        return str_to_list(pmperm)


def is_muted(id):  # Take int or str with numbers only , Returns Boolean
    pmperm = get_muted()
    if str(id) in pmperm:
        return True
    else:
        return False


def mute(id):  # Take int or str with numbers only , Returns Boolean
    id = str(id)
    try:
        pmperm = get_muted()
        pmperm.append(id)
        ExtremedB.set("MUTE", list_to_str(pmperm))
        return True
    except Exception as e:
        print(f"ExtremeProUserbot LOG : // functions/pmpermit_db/approve_user : {e}")
        return False


def unmute(id):  # Take int or str with numbers only , Returns Boolean
    id = str(id)
    try:
        pmperm = get_muted()
        pmperm.remove(id)
        ExtremedB.set("MUTE", list_to_str(pmperm))
        return True
    except Exception:
        return False
