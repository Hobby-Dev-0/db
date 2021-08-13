# ExtremeProUserbot - UserBot
# Copyright (C) 2021 TeamExtremeProUserbot
#
# This file is a part of < https://github.com/TeamExtremeProUserbot/ExtremeProUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamExtremeProUserbot/ExtremeProUserbot/blob/main/LICENSE/>.

from .. import ExtremedB


def is_clean_added(chat):
    k = ExtremedB.get("CLEANCHAT")
    if k:
        if str(chat) in k:
            return True
        return
    return


def add_clean(chat):
    if not is_clean_added(chat):
        k = ExtremedB.get("CLEANCHAT")
        if k:
            return ExtremedB.set("CLEANCHAT", k + " " + str(chat))
        return ExtremedB.set("CLEANCHAT", str(chat))
    return


def rem_clean(chat):
    if is_clean_added(chat):
        k = ExtremedB.get("CLEANCHAT")
        ExtremedB.set("CLEANCHAT", k.replace(str(chat), ""))
        return True
    return
