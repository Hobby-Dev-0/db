# ExtremeProUserbot - UserBot
# Copyright (C) 2021 TeamExtremeProUserbot
#
# This file is a part of < https://github.com/TeamExtremeProUserbot/ExtremeProUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamExtremeProUserbot/ExtremeProUserbot/blob/main/LICENSE/>.

from .. import ExtremedB, extremepro_bot


def str_to_list(text):  # Returns List
    return text.split(" ")


def list_to_str(list):  # Returns String
    str = ""
    for x in list:
        str += f"{x} "
    return str.strip()


def are_all_nums(list):  # Takes List , Returns Boolean
    flag = True
    for item in list:
        if not item.isdigit():
            flag = False
            break
    return flag


def get_sudos():  # Returns List
    sudos = ExtremedB.get("SUDOS")
    if sudos is None or sudos == "":
        return [""]
    else:
        return str_to_list(sudos)


def is_sudo(id):  # Take int or str with numbers only , Returns Boolean
    if not str(id).isdigit():
        return False
    sudos = get_sudos()
    if str(id) in sudos:
        return True
    else:
        return False


def add_sudo(id):  # Take int or str with numbers only , Returns Boolean
    id = str(id)
    if not id.isdigit():
        return False
    try:
        sudos = get_sudos()
        sudos.append(id)
        ExtremedB.set("SUDOS", list_to_str(sudos))
        return True
    except Exception as e:
        print(f"ExtremeProUserbot LOG : // functions/sudos/add_sudo : {e}")
        return False


def del_sudo(id):  # Take int or str with numbers only , Returns Boolean
    id = str(id)
    if not id.isdigit():
        return False
    try:
        sudos = get_sudos()
        sudos.remove(id)
        ExtremedB.set("SUDOS", list_to_str(sudos))
        return True
    except Exception as e:
        print(f"ExtremeProUserbot LOG : // functions/sudos/del_sudo : {e}")
        return False


def is_fullsudo(id):
    if id == extremepro_bot.uid:
        return True
    id = str(id)
    x = ExtremedB.get("FULLSUDO")
    if x:
        if id in x:
            return True
        return
    return
