# ExtremeProUserbot - UserBot
# Copyright (C) 2021 TeamExtremeProUserbot
#
# This file is a part of < https://github.com/TeamExtremeProUserbot/ExtremeProUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamExtremeProUserbot/ExtremeProUserbot/blob/main/LICENSE/>.

from .. import ExtremedB


def ls(list):
    z = 0
    xx = ""
    for x in list:
        z += 1
        if z == len(list):
            xx += x
        else:
            xx += f"{x}|||"
    return xx


def get_reply(word):
    masala = ExtremedB.get("SNIP")
    if not masala:
        return
    x = masala.split("|||")
    for i in x:
        x = i.split("$|")
        if str(x[0]) == str(word):
            return eval(x[1])
    return None


def list_snip():
    fl = ExtremedB.get("SNIP")
    if not fl:
        return None
    rt = fl.split("|||")
    tata = ""
    tar = 0
    for on in rt:
        er = on.split("$|")
        tata += f"👉 `${er[0]}`\n"
        tar += 1
    if tar == 0:
        return None
    return tata


def get_snips():
    if ExtremedB.get("SNIP"):
        return True
    else:
        return


def add_snip(word, msg, media):
    try:
        rr = str({"msg": msg, "media": media})
        the_thing = f"{word}$|{rr}"
        rt = ExtremedB.get("SNIP")
        if not rt:
            ExtremedB.set("SNIP", the_thing)
        else:
            xx = rt.split("|||")
            for y in xx:
                yy = y.split("$|")
                if str(yy[0]) == str(word):
                    xx.remove(y)
                    if the_thing not in xx:
                        xx.append(the_thing)
                else:
                    if the_thing not in xx:
                        xx.append(the_thing)
            ExtremedB.set("SNIP", ls(xx))
        return True
    except Exception as e:
        print(e)
        return False


def rem_snip(word):
    masala = ExtremedB.get("SNIP")
    if not masala:
        return
    yx = masala.split("|||")
    for i in yx:
        x = i.split("$|")
        if str(x[0]) == str(word):
            yx.remove(i)
    return ExtremedB.set("SNIP", ls(yx))
