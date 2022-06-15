## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQBzwILHLPeBgBDKXtUbQFcAWmJqLC3oPCN_z8U5NZ1FDyxa981sSFW9gEz5hwA1r4fQrqyPPUbYLLlY3ktjbtjACq9fZMHkPMeE-ClaQLb9NGEfFFixOhall6zpV84QENu4FHmdXsSVNA5ZNik5x3bnYU_QxbNvmkN_sDQvIADIXdBUd55BWa224L0UV9pm_GXI4dmZGeWUOtp3FMidkvIH57yClADiVqzij3nCenA2_ydYa1gIQ3bfULToeEuvEpmhCqVJXOSwPcgQoq0TvdEyHcbk7-_fgO4IqlDlEAvbGUhN_8msEPUpFoa5bClV7kerZtKywy9nvaiTpe87gPPRAAAAAUAHvQIA")
BOT_TOKEN = getenv("BOT_TOKEN", "5434640519:AAFSbmKO4Wyyv9BMbbL5IBkKVp-cPdArcW8")
BOT_NAME = getenv("BOT_NAME", "𝐌𝐔𝐒𝐈𝐂 𝐘𝐀𝐌𝐀𝐒𝐇")
API_ID = int(getenv("API_ID", "11625641"))
API_HASH = getenv("API_HASH", "284d34d43030ea0dfd35736a3e16a1d3")
OWNER_NAME = getenv("OWNER_NAME", "𝐌𝐔𝐒𝐈𝐂 𝐘𝐀𝐌𝐀𝐒𝐇")
OWNER_USERNAME = getenv("OWNER_USERNAME", "aaaqqq")
ALIVE_NAME = getenv("ALIVE_NAME", "𝐌𝐔𝐒𝐈𝐂 𝐘𝐀𝐌𝐀𝐒𝐇")
BOT_USERNAME = getenv("BOT_USERNAME", "B_4_HBOT")
OWNER_ID = getenv("OWNER_ID", "5338950085")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "H_B_B4")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "aaaqqq")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "H_B_4")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5338950085").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/1103527d5d6d9c9df7358.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/1103527d5d6d9c9df7358.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/9b9edec5b36dd30b826fe.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/0e1e455300053e87408ca.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/a961ae6b2bac6e39c723a.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/74457783123eddb619f6a.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/455a707c25a3de6629097.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/a312d072b125a67cee66e.jpg")
