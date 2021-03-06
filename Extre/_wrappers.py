import asyncio
import functools

from Extre.sudo import sudoers

# edit/reply & delete


async def eod(event, text=None, **args):
    args["func"] = lambda e: e.via_bot_id is None
    time = args.get("time", 5)
    link_preview = args.get("link_preview", False)
    parse_mode = args.get("parse_mode", "md")
    if str(event.sender_id) in sudoers():
        replied = await event.get_reply_message()
        if replied:
            edt = await replied.reply(
                text, link_preview=link_preview, parse_mode=parse_mode
            )
        else:
            edt = await event.reply(
                text, link_preview=link_preview, parse_mode=parse_mode
            )
    else:
        edt = await event.edit(text, link_preview=link_preview, parse_mode=parse_mode)
    if time:
        await asyncio.sleep(time)
        return await ult.delete()
    return edt


# sudo


def sudo():
    def decorator(function):
        @functools.wraps(function)
        async def wrapper(event):
            if event.out or str(event.sender_id) in sudoers():
                await function(event)
            else:
                pass

        return wrapper

    return decorator


# edit or reply


async def eor(event, text, **omk):
    link_preview = omk.get("link_preview", False)
    parse_mode = omk.get("parse_mode", "md")
    time = omk.get("time", None)
    if str(event.sender_id) in sudoers():
        reply_to = await event.get_reply_message()
        if reply_to:
            ok = await reply_to.reply(
                text, link_preview=link_preview, parse_mode=parse_mode
            )
        else:
            ok = await event.reply(
                text, link_preview=link_preview, parse_mode=parse_mode
            )
    else:
        ok = await event.edit(text, link_preview=link_preview, parse_mode=parse_mode)
    if time:
        await asyncio.sleep(time)
        return await ok.delete()
    return ok
