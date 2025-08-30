#(©) TKSFamily 

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = environ.get("TG_BOT_TOKEN", "8246275392:AAEyZ68SQYdhx6JfbSMZ2GyHtSdQ3jeEFPA")

#Your API ID from my.telegram.org
APP_ID = int(environ.get("APP_ID", "23574009"))

#Your API Hash from my.telegram.org
API_HASH = environ.get("API_HASH", "17e1e468e29fe266622955410bcc48f2")

#Your db channel Id
CHANNEL_ID = int(environ.get("CHANNEL_ID", "-1002905615542"))

#OWNER ID
OWNER_ID = int(environ.get("OWNER_ID", "7726252322"))

#Port
PORT = environ.get("PORT", "8080")

#Database 
DB_URI = environ.get("DATABASE_URL", "mongodb+srv://tksfamilytg:hQx57pZYGBRobU1a@cluster0.qpefhjm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = environ.get("DATABASE_NAME", "tksfamilytg")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(environ.get("FORCE_SUB_CHANNEL", "-1003077079889"))
JOIN_REQUEST_ENABLE = environ.get("JOIN_REQUEST_ENABLED", None)

TG_BOT_WORKERS = int(environ.get("TG_BOT_WORKERS", "4"))

#start message
START_PIC = environ.get("START_PIC","https://lh3.googleusercontent.com/d/1LAZUxFPWOFxuiMqLO2bLEhTc05y6Y1fZ")
START_MSG = environ.get("START_MESSAGE", "Hello {first}\n\nI can store private files in Specified Channel and other users can access it from special link.")
try:
    ADMINS=[]
    for x in (environ.get("ADMINS", "7726252322").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if environ.get('PROTECT_CONTENT', "False") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "0"))
AUTO_DELETE_MSG = environ.get("AUTO_DELETE_MSG", "This file will be automatically deleted in {time} seconds. Please ensure you have saved any necessary content before this time.")
AUTO_DEL_SUCCESS_MSG = environ.get("AUTO_DEL_SUCCESS_MSG", "Your file has been successfully deleted. Thank you for using our service. ✅")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(7726252322)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
