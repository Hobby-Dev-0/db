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


def are_all_num(list):  # Takes List , Returns Boolean
    flag = True
    for item in list:
        if not item.isdigit():
            flag = False
            break
    return flag


def get_source_channels():  # Returns List
    channels = ExtremedB.get("CH_SOURCE")
    if channels is None or channels == "":
        return [""]
    else:
        return str_to_list(channels)


def get_no_source_channels():  # Returns List
    channels = ExtremedB.get("CH_SOURCE")
    if channels is None or channels == "":
        return 0
    else:
        a = channels.split(" ")
    return len(a)


def is_source_channel_added(id):
    channels = get_source_channels()
    if str(id) in channels:
        return True
    else:
        return False


def add_source_channel(id):  # Take int or str with numbers only , Returns Boolean
    id = str(id)
    try:
        channels = get_source_channels()
        channels.append(id)
        ExtremedB.set("CH_SOURCE", list_to_str(channels))
        return True
    except Exception as e:
        print(f"ExtremeProUserbot LOG : // functions/broadcast_db/add_channel : {e}")
        return False


def rem_source_channel(id):
    try:
        channels = get_source_channels()
        channels.remove(str(id))
        ExtremedB.set("CH_SOURCE", list_to_str(channels))
        return True
    except Exception:
        return False


#########################


def get_destinations():  # Returns List
    channels = ExtremedB.get("CH_DESTINATION")
    if channels is None or channels == "":
        return [""]
    else:
        return str_to_list(channels)


def get_no_destinations():  # Returns List
    channels = ExtremedB.get("CH_DESTINATION")
    if channels is None or channels == "":
        return 0
    else:
        a = channels.split(" ")
    return len(a)


def is_destination_added(id):
    channels = get_destinations()
    if str(id) in channels:
        return True
    else:
        return False


def add_destination(id):  # Take int or str with numbers only , Returns Boolean
    id = str(id)
    try:
        channels = get_destinations()
        channels.append(id)
        ExtremedB.set("CH_DESTINATION", list_to_str(channels))
        return True
    except Exception as e:
        print(f"ExtremeProUserbot LOG : // functions/broadcast_db/add_channel : {e}")
        return False


def rem_destination(id):
    try:
        channels = get_destinations()
        channels.remove(str(id))
        ExtremedB.set("CH_DESTINATION", list_to_str(channels))
        return True
    except Exception as e:
        print(f"ExtremeProUserbot LOG : // functions/broadcast_db/rem_channel : {e}")
        return False
