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


def get_logger():  # Returns List
    pmperm = ExtremedB.get("LOGUSERS")
    if pmperm is None or pmperm == "":
        return [""]
    else:
        return str_to_list(pmperm)


def is_logger(id):  # Take int or str with numbers only , Returns Boolean
    if not str(id).isdigit():
        return False
    pmperm = get_logger()
    if str(id) in pmperm:
        return True
    else:
        return False


def log_user(id):  # Take int or str with numbers only , Returns Boolean
    id = str(id)
    if not id.isdigit():
        return False
    try:
        pmperm = get_logger()
        pmperm.append(id)
        ExtremedB.set("LOGUSERS", list_to_str(pmperm))
        return True
    except Exception as e:
        print(f"ExtremeProUserbot LOG : // functions/logusers_db/log_user : {e}")
        return False


def nolog_user(id):  # Take int or str with numbers only , Returns Boolean
    id = str(id)
    if not id.isdigit():
        return False
    try:
        pmperm = get_logger()
        pmperm.remove(id)
        ExtremedB.set("LOGUSERS", list_to_str(pmperm))
        return True
    except Exception as e:
        print(f"ExtremeProUserbot LOG : // functions/loguser_db/nolog_user : {e}")
        return False
