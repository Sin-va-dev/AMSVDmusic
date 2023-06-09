import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "23298188" ))
API_HASH = getenv("API_HASH", "49869a9d2c46007cc1c1e002e8f8ef2b")

BOT_TOKEN = getenv("BOT_TOKEN", "6270407253:AAFz7PrWww7X_aeYuTvbyKIRW3VSL6gbvHM")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://svdtelegram1996:NNlH20lGwB955RbZ@cluster0.bg21zff.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001743709729"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "SVdtestmuSic")

OWNER_ID = list(map(int, getenv("OWNER_ID", "655594746").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/Sin-va-dev/AMSVDmusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", "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")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SVDsupportchannel")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/SVD_support_group")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "999"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "19609edb1b9f4ed7be0c8c1342039362")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "409e31d3ddd64af08cfcc3b0f064fcbe")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "1"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("SESSION_NAME", "AQBRUKPj6qH_JJu0-7hqyyF1clTJW7YOJRvJqtH6A6-iHpcBJGpE2h60yBP8ylegmVKeeQGuFo9PdmAyZ1APjqvJmWIlBAZ67OJZTGN0DMiRMi6P6_y4mcBq0JbpVLtMoCox3qLt-MKnbc2fxxYKiDUo8HHnIjgrzn9J24i3946DZHvRruGZyGJP9P2pzKBL8APYQQIMvEJdnh5AJ0y7QihosSKZyAinSTFvBQkkjAKCeYfKFhz29_4O1oQ9iCcHOKIPy_bvr2R-M0Wm06E_PINVjIWZbyS2Z7q3g6COVNwnQVuum9lMFV9U0HDdgDUq1qWSbGlvQDXh_DJjWeS0e6_qAAAAAWm6r8kA")
STRING2 = getenv("SESSION_NAME2", None)
STRING3 = getenv("SESSION_NAME3", None)
STRING4 = getenv("SESSION_NAME4", None)
STRING5 = getenv("SESSION_NAME5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/9dbcb3cf35dc596443320.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/9349a004446e5e94abd6b.jpg",
)

PLAYLIST_IMG_URL = "https://telegra.ph/file/86f81220c410743f1e1b1.jpg"

GLOBAL_IMG_URL = "https://telegra.ph/file/86f81220c410743f1e1b1.jpg"

STATS_IMG_URL = "https://telegra.ph/file/9dbcb3cf35dc596443320.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/9349a004446e5e94abd6b.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/9dbcb3cf35dc596443320.jpg"
