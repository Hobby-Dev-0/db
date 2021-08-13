from .. import ExtremedB


def add_black_chat(chat_id):
    chat = eval(ExtremedB.get("BLACKLIST_CHATS"))
    if chat_id not in chat:
        chat.append(chat_id)
        ExtremedB.set("BLACKLIST_CHATS", str(chat))


def rem_black_chat(chat_id):
    chat = eval(ExtremedB.get("BLACKLIST_CHATS"))
    if chat_id in chat:
        chat.remove(chat_id)
        ExtremedB.set("BLACKLIST_CHATS", str(chat))
