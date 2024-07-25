import re
from os import environ,getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '9747098'))
API_HASH = environ.get('API_HASH', '15384775587d976eccc8b367e92a96a3')
BOT_TOKEN = environ.get('BOT_TOKEN', "6163005421:AAGyIa3RVaIKr0TS-tHX2uTWsVIU2EHjNmI")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/43e0adadfddcbe2050397.jpg https://graph.org/file/159914185633e17726813.jpg https://graph.org/file/ef214c10d9428c432fbe2.jpg https://graph.org/file/7d0e15a2b757817aac9b8.jpg https://graph.org/file/d0e10dce8eb13e01a82f6.jpg https://graph.org/file/72e16afee07708488c024.jpg https://graph.org/file/5487252a7a691280e27c6.jpg https://graph.org/file/2999245bd29c4ac69cc8d.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/8cd764fbdf3ccd34abe22.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://t.me/How_To_Download_URL/93")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/86b7b7e2aa7e38f328902.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/54339913c153df35e5a54.jpg'))
CODE = (environ.get('CODE', 'https://graph.org/file/f06e8bec01d553d934945.jpg'))

#stream link shortner
STREAM_SITE = (environ.get('STREAM_SITE', 'publicearn.com'))
STREAM_API = (environ.get('STREAM_API', '9672acfd41f4778f06adb1c63d6a241f0c546954'))
STREAMHTO = (environ.get('STREAMHTO', 'https://t.me/How_To_Download_URL/94'))

#REFERAL
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '15')) # number of referal count
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '1month')
# add premium logs channel id
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', ''))

# Admins, Channels & Users
USERNAME = environ.get("USERNAME", "https://t.me/SpySpidey")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1287471711 1351421131').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002009528150').split()] #Channel id for auto indexing ( make sure bot is admin )
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
auth_channel = environ.get('AUTH_CHANNEL', '-1002140715188') #Channel / Group Id for force sub ( make sure bot is admin )
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1001882517877') # support group id ( make sure bot is admin )
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1001882517877') # request channel id ( make sure bot is admin )
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True)) # True if you want no results messages in Log Channel

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Cinipaiyanbot: Cinipaiyanbot@cluster0.3kxfxdw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#Shortner Variables
VERIFY = bool(environ.get('VERIFY', False)) # Verification On ( True ) / Off ( False )
HOWTOVERIFY = environ.get('HOWTOVERIFY', 'https://t.me/How_To_Download_URL/94') # How to open tutorial link for verification
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'publicearn.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '9672acfd41f4778f06adb1c63d6a241f0c546954')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))

# Others
WCHNL = environ.get('WCHNL', 'https://chat.whatsapp.com/LqoARA6LJGK2xkKNowiXfN')
WRM = environ.get('WRM', 'https://t.me/cinepaiyan_Movies')
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+5x_HhwVsIgs3ZTk1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/cinepaiyan_Movies')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/How_To_Download_URL/94') # Tutorial video link for opening shortlink website 
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', 'Hello Nanbha and Nanbis ❤️')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002041629720')) #Log channel id ( make sure bot is admin )
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/Discussioncinepaiyan') #Support group link ( make sure bot is admin )
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "True")), True)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["Tamil", "Tam", "Telugu", "Tel", "Kannada", "kan", "Malayalam", "Mal", "Hindi", "Hin", "English", "Eng", "Korean", "Kor", "Japanese", "Jap", "Chinese", "Chi", "Dual", "Multi"]
YEARS = ["1900", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]
SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]
EPISODES = ["E01", "E02", "E03", "E04", "E05", "E06", "E07", "E08", "E09", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E19", "E20", "E21", "E22", "E23", "E24", "E25", "E26", "E27", "E28", "E29", "E30", "E31", "E32", "E33", "E34", "E35", "E36", "E37", "E38", "E39", "E40"]
QUALITIES = ["240p", "360p", "480p", "720p", "1080p", "1440p", "2160p", "4K", "HQ", "HD","HQPreDVD","PreDVD"]

# Online Stream and Download
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME', 'mraklinkzz-4a13061a9826')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "https://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'LazyPrincess'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME', 'mraklinkzz-4a13061a9826'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',True))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
