from pyrogram import Client, filters
from info import FILE_STORE_CHANNEL
from database.ia_filterdb import save_file

media_filter = filters.document | filters.video | filters.audio


@Client.on_message(filters.chat(FILE_STORE_CHANNEL) & media_filter)
async def media(bot, message):
    """Media Handler"""
    for file_type in ("document", "video", "audio"):
        media = getattr(message, file_type, None)
        if media is not None:
            break
    else:
        return

    media.file_type = file_type
    media.caption = message.caption
    await save_file(media)