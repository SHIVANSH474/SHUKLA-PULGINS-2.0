import os
import time
from pyrogram import Client
from platform import python_version
from Hellbot.core.config import API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN, STRING_SESSION

import heroku3
from pyrogram import __version__ as pyrogram_version

from .core import LOGS, Config

spam_chats = []
SUDO_USER = SUDO_USERS
SUDO_USERS.append(OWNER_ID)

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Hellbot/plugins"),
    in_memory=True,
)

client = Client(
    name="rj",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    session_string=STRING_SESSION,
    plugins=dict(root="Hellbot/plugins")
)



from pyrogram import Client
from config2 import API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN, STRING_SESSION

spam_chats = []
SUDO_USER = SUDO_USERS
SUDO_USERS.append(OWNER_ID)

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Hellbot/plugins"),
    in_memory=True,
)

client = Client(
    name="rj",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    session_string=STRING_SESSION,
    plugins=dict(root="Hellbot/plugins")
)




START_TIME = time.time()


__version__ = {
    "hellbot": "3.0",
    "pyrogram": pyrogram_version,
    "python": python_version(),
}


try:
    if Config.HEROKU_APIKEY is not None and Config.HEROKU_APPNAME is not None:
        HEROKU_APP = heroku3.from_key(Config.HEROKU_APIKEY).apps()[
            Config.HEROKU_APPNAME
        ]
    else:
        HEROKU_APP = None
except Exception as e:
    LOGS.error(f"Heroku Api - {e}")
    HEROKU_APP = None


if Config.API_HASH is None:
    LOGS.error("Please set your API_HASH !")
    quit(1)

if Config.API_ID == 0:
    LOGS.error("Please set your API_ID !")
    quit(1)

if Config.BOT_TOKEN is None:
    LOGS.error("Please set your BOT_TOKEN !")
    quit(1)

if Config.DATABASE_URL is None:
    LOGS.error("Please set your DATABASE_URL !")
    quit(1)

if Config.LOGGER_ID == 0:
    LOGS.error("Please set your LOGGER_ID !")
    quit(1)

if Config.OWNER_ID == 0:
    LOGS.error("Please set your OWNER_ID !")
    quit(1)

if not os.path.isdir(Config.DWL_DIR):
    os.makedirs(Config.DWL_DIR)

if not os.path.isdir(Config.TEMP_DIR):
    os.makedirs(Config.TEMP_DIR)
