from os import getenv

API_ID = int(getenv("API_ID", "29908998"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
STRING_SESSION = getenv("STRING_SESSION", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5392070730").split()))
ALIVE_PIC = getenv("ALIVE_PIC", "https://te.legra.ph/file/e25a563619c653328830d.jpg")
REPO_URL = getenv("REPO_URL", "https://github.com/badmunda98/PBXPLUGINS_2.0")
BRANCH = getenv("BRANCH", "main")
