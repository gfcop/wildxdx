## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAiSDwHhGq3PvhHjKHpnVxSPiSz3wGmVZ9faQbITp3y8I-KYh7zyFCB-mp9frEEv6ud5GUKwjHop_BxnwZLwBDOY1QoJ6LIi0rgGwXsXAXun6whYIaZWCg_b_CO4TcCWGgVEr7wWwxPUGc2abj7QowlE8MITE3fQTuim4e6uhxtNPMKodcSsXsNCYuo7g1cSJdsmli9FWcqX2uOJ4CcfvS3G-LSfVehlO7v6mLHy6YErkkKIlVjrj8u3JT7I36zxptOpFmO-18r9vtU1nOMdqT6o7IjSXvIastOHRVDcFJlPOzIUxnmHMJJ7uTrkNt0J27wq0ERJQVZQSZuE5O9JH7bAAAAAVIiPLkA")
BOT_TOKEN = getenv("BOT_TOKEN", "5400035200:AAGRUFJBmpAr-X-nAJq2peQ7k_M5EtGFkgw")
BOT_NAME = getenv("BOT_NAME","𝑾𝒊𝑳𝑫 ꭙ")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "aakash")
ALIVE_NAME = getenv("ALIVE_NAME", "wild")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "owner_gfc")
BOT_USERNAME = getenv("BOT_USERNAME", "wildx_robot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MUSIC ASSISTANT2")
GROUP_SUPPORT = getenv("GROUP_SUPPORT","GFC_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL","wildupdates")
SUDO_USERS = list(map(int, getenv("SUDO_USERS","5540577046").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "540000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
