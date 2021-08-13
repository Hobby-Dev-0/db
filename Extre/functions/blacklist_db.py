# ExtremeProUserbot - UserBot
# Copyright (C) 2021 TeamExtremeProUserbot
#
# This file is a part of < https://github.com/TeamExtremeProUserbot/ExtremeProUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamExtremeProUserbot/ExtremeProUserbot/blob/main/LICENSE/>.

from .. import ExtremedB


def lss(list):
    z = 0
    xx = ""
    for x in list:
        z += 1
        if z == len(list):
            xx += x
        else:
            xx += f"{x}$|"
    return xx


def get_blacklist(chat):
    fl = ExtremedB.get("BLACKLISTS")
    if not fl:
        return None
    y = eval(fl)
    if y.get(chat):
        return y.get(chat)
    return


def list_blacklist(chat):
    fl = ExtremedB.get("BLACKLISTS")
    if not fl:
        return None
    y = eval(fl)
    if y.get(chat):
        allword = (y.get(chat)).split("$|")
        g = ""
        for z in allword:
            g += f"👉`{z}`\n"
        if g:
            return g
    return


def add_blacklist(chat, word):
    try:
        ok = str({chat: word})
        rt = ExtremedB.get("BLACKLISTS")
        if not rt:
            ExtremedB.set("BLACKLISTS", ok)
        else:
            y = eval(rt)
            if y.get(chat):
                allword = (y.get(chat)).split("$|")
                for z in allword:
                    if word != z:
                        allword.append(word)
                aword = lss(allword)
                y.pop(chat)
                y.update({chat: aword})
            else:
                y.update({chat: word})
            ExtremedB.set("BLACKLISTS", str(y))
            return True
    except Exception as e:
        print(e)
        return False


def rem_blacklist(chat, word):
    masala = ExtremedB.get("BLACKLISTS")
    if not masala:
        return
    y = eval(masala)
    if y.get(chat):
        allword = (y.get(chat)).split("$|")
        for z in allword:
            if word == z:
                allword.remove(word)
        aword = lss(allword)
        y.pop(chat)
        y.update({chat: aword})
    return ExtremedB.set("BLACKLISTS", str(y))
