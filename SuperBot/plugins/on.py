# Thanks to @Shivam_Patel Bro
# Thanks to Sipak .. 
# Idea by @Shivam_Patel 
# Made by @Shivam_Patel & @ProgrammingError ....TEAM DC
# Kang with credits else gay...
# inline alive
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from SuperBot.utils import admin_cmd
from SuperBot import ALIVE_NAME, Lastupdate
from . import dcdef
from SuperBot import bot as borg
from telethon.tl.custom import Button
from telethon.tl.types import ChannelParticipantsAdmins
global ok
ok = borg.uid

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SuperBot"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO" , None)

TG_BOT_USER_NAME_BF_HER = os.environ.get("TG_BOT_USER_NAME_BF_HER", None)
if TG_BOT_USER_NAME_BF_HER is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await borg.get_me()
        uptime = await dcdef.get_readable_time((time.time() - Lastupdate))
        dc_text=(f"**โงโง ๐๐ช๐ฅ๐๐ง๐ฝ๐ค๐ฉ ๐๐จ ๐๐ฅ ๐๐ฃ๐ ๐๐ช๐ฃ๐ฃ๐๐ฃ๐ ๐๐ช๐๐๐๐จ๐จ๐๐ช๐ก๐ก๐ฎ โงโง**\n\n**๐จ๐๐ ๐๐๐ ๐บ๐๐๐๐๐๐ ๐๐๐ ๐ซ๐๐๐๐ฉ๐๐๐๐ ๐๐๐ ๐ญ๐๐๐๐๐๐๐๐๐๐ ๐ท๐๐๐๐๐๐๐, ๐๐ ๐๐๐๐ ๐๐๐๐๐๐ ๐๐.**\n\nโ ๐ผ๐๐๐ ๐ด๐๐๐ข๐ก ๐๐ฆ ๐๐ฆ๐ ๐ก๐๐ โ\n\nโฅ **Tแดสแดแดสแดษด Vแดส๊ฑษชแดษด :** `{version.__version__}`\nโฅ **Sแดแดแดแดสแด Cสแดษดษดแดส :** [Jแดษชษด](https://t.me/SuperBot_SupportChat)\nโฅ **Cแดแดสสษชษขสแด Bส :** [๐๐ฎ๐ฉ๐๐ซ๐๐จ๐ญ](https://github.com/MadBoy-X/SuperBot)\n\nโฅ **Uแดแดษชแดแด :** `{uptime}`\n\nโฅ **Mส Mแดsแดแดส :** [{DEFAULTUSER}](tg://user?id={ok})\n")
        if query.startswith("alive") and event.query.user_id == me.id:
            buttons = [
                [
                    Button.url("Repo", "https://github.com/MadBoy-X/SuperBot"),
                    Button.url("Deploy", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FMadBoy-X%2FSuperBot-Deploy&template=https%3A%2F%2Fgithub.com%2FMadBoy-X%2FSuperBot-Deploy")],
                    [Button.url("String", "https://replit.com/@madboy482/SuperBot#main.py"),
                    Button.url("Support", "https://t.me/SuperBot_SupportChat"),
                ]
            ]
            if ALIVE_PHOTTO and ALIVE_PHOTTO.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALIVE_PHOTTO,
                    text=dc_text,
                    buttons=buttons,
                    link_preview=False
                )
            elif ALIVE_PHOTTO:
                result = builder.document(
                    ALIVE_PHOTTO,
                    title="SuperBot",
                    text=dc_text,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="SuperBot",
                    text=dc_text,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)
