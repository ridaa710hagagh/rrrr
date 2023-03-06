from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "8432225")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "0f9137fec6f48a236a56ae3e32d23ee1")#لا تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "5539489267:AAF2MUDACU-t80FmoJKCZz_-Rc7_R3h8v1k")
SESSION_NAME = getenv("SESSION_NAME", "AgDELQ0NizCK6NvtpcRgzxm1wJIL0VV2Ar_PMA3OY2PQGzRqlR7dJTCoPh-rcjPgGeK-ZKCc3-iqRA9lItk9LqGHx-CCvWyu9Kbhs8YjqiavoAvBTfycjiV4M86ws5MkwLe8sXHFjqiOqBmYawXt971QchvZd8Np_0VJocY7pA637TOMXlsIjK-7a6pVUnCc_o1zqos4yZe85ibEt4QUCG9b02w7RtLtzxY8YGl0dwWWe8p5d0pKiXlsVJx8iFaHg_bnpSL4B50dTy0qnGtcZEvhq614clEZR-_E5UdNXVrFnTRQglzsoKO7FHLdxEmFpJyAfZPRe6zD2aCAFWDxibY-bVfFWwA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "R4005") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "ࢪﺿـاۅي اެبن الـدورة🇮🇶.") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "MUSICFIINBOT") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "x02x2") # @ هنا ضغ يوزر كروبك بدون 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "x02x2") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1254750804").split()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1254750804 1793004308").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://prnt.sc/tUqp2b-SmE12")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
