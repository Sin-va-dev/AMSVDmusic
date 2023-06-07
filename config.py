import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("12163360"))
API_HASH = getenv("02862f9111364754b0d4625f6695ba06")

BOT_TOKEN = getenv("5671435658:AAEcQprlPqto5g-NrsUabBWC85GYGptbTkU")

MONGO_DB_URI = getenv("MONGO_DB_URI", mongodb+srv://NCsingle:BEST1122334455@cluster0.fee7qv7.mongodb.net/?retryWrites=true&w=majority)
LOG_GROUP_ID = int(getenv("-984459977"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "SVdtestmuSic")

OWNER_ID = list(map(int, getenv("OWNER_ID", "655594746").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://telegra.ph/file/712d384e549f37e74f4a8.mp4")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

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

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION1", AQC5mSAAWLfo9UsOfiIdtaxrYOHk1UHJRKl0G38A5GwyJsF80c0NDc7Q_krQV94ozVwPQmJZqMAoKSlQglt5_Q_PW70vKT1MnGYSt_m6eltlTuaVNDDQZaEIQN3XVtbQrnIlmXSa4HEwtn9WqtjeVuSr-6jhfrtU4uuAxLAV_XX8t4sScg8y7R1k7QZIDBG6NlZMkCEEozrClxFlfAd3ZHn8pWYeylmdWYdniM7EhAE1jGU7YP6FEmzSL90AnPoI0mz45_pmR90VJhixTf36FStZ426GrMeY7i_PQPePM4brEG9vEfFBvpuqwpGMXgs61UfvQLOC9IaJaYhqt3Gxj9rKV0YXLQAAAAFIAxACAA)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

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
