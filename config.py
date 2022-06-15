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
BOT_NAME = getenv("BOT_NAME", "𝐌𝐔𝐒𝐈𝐂 𝐘𝐀𝐌𝐀𝐒𝐇『〆』")
API_ID = int(getenv("API_ID", "11625641"))
API_HASH = getenv("API_HASH", "284d34d43030ea0dfd35736a3e16a1d3")
OWNER_NAME = getenv("OWNER_NAME", "وكح؟『〆』")
OWNER_USERNAME = getenv("OWNER_USERNAME", "aaaqqq")
ALIVE_NAME = getenv("ALIVE_NAME", "وكح؟『〆』")
BOT_USERNAME = getenv("BOT_USERNAME", "B_4_HBOT")
OWNER_ID = getenv("OWNER_ID", "5338950085")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "H_B_B4")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "uuuuxw")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "uuuuxw")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5338950085").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
