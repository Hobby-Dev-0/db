# ExtremeProUserbot - UserBot
# Copyright (C) 2021 TeamExtremeProUserbot
#
# This file is a part of < https://github.com/TeamExtremeProUserbot/ExtremeProUserbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamExtremeProUserbot/ExtremeProUserbot/blob/main/LICENSE/>.


from .. import ExtremedB

try:
    eval(ExtremedB.get("ASST_CMDS"))
except BaseException:
    ExtremedB.set("ASST_CMDS", "{}")


def add_cmd(cmd, msg, media):
    ok = eval(ExtremedB.get("ASST_CMDS"))
    ok.update({cmd: {"msg": msg, "media": media}})
    return ExtremedB.set("ASST_CMDS", str(ok))


def rem_cmd(cmd):
    ok = eval(ExtremedB.get("ASST_CMDS"))
    if ok.get(cmd):
        ok.pop(cmd)
        return ExtremedB.set("ASST_CMDS", str(ok))
    return


def cmd_reply(cmd):
    ok = eval(ExtremedB.get("ASST_CMDS"))
    if ok.get(cmd):
        okk = ok[cmd]
        return okk["msg"], okk["media"]
    return


def list_cmds():
    ok = eval(ExtremedB.get("ASST_CMDS"))
    if ok.keys():
        return ok.keys()
    return
