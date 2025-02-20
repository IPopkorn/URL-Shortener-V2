import os

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", "26164342"))
API_HASH = os.environ.get("API_HASH", "1e6f9af98ffe06f3281a0b537ebf5c39")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5947988639:AAFD7N0C8V8jMe6oh8iPSfl_3KP9BzdQR5s")
DROPLINK_API = os.environ.get("DROPLINK_API")
MDISK_API = os.environ.get("QqTaWUfW4gRZiwHu4cdg")
ADMINS = list(int(i.strip()) for i in os.environ.get("ADMINS").split(",")) if os.environ.get("ADMINS") else []
DATABASE_NAME = os.environ.get("DATABASE_NAME", "UrlShortner")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Raju143:Raju143@cluster0.rn7g4nh.mongodb.net/?retryWrites=true&w=majority"

")
WEBSITE = os.environ.get('WEBSITE')

#  Optionnal variables
INCLUDE_DOMAIN = list(i.strip() for i in os.environ.get("INCLUDE_DOMAIN").split(",")) if os.environ.get("INCLUDE_DOMAIN") else []
EXCLUDE_DOMAIN = list(i.strip() for i in os.environ.get("EXCLUDE_DOMAIN").split(",")) if os.environ.get("EXCLUDE_DOMAIN") else []
CHANNELS = is_enabled((os.environ.get('CHANNELS', "True")), True)
CHANNEL_ID = list(int(i.strip()) for i in os.environ.get("CHANNEL_ID").split(" ")) if os.environ.get("CHANNEL_ID") else []
FORWARD_MESSAGE = is_enabled((os.environ.get('FORWARD_MESSAGE', "False")), False)
SOURCE_CODE = os.environ.get("SOURCE_CODE", "https://github.com/Ps705112/URL-Shortener-V2")
USERNAME = os.environ.get("USERNAME", None)
HEADER_TEXT = os.environ.get("HEADER_TEXT", '')
FOOTER_TEXT = os.environ.get("FOOTER_TEXT", '')
BANNER_IMAGE = os.environ.get("BANNER_IMAGE", '')
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '')
LINK_BYPASS = is_enabled((os.environ.get('LINK_BYPASS', "False")), False)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU = True if HEROKU_API_KEY and HEROKU_APP_NAME else False
mongodb+srv://Raju143:Raju143@cluster0.rn7g4nh.mongodb.net/?retryWrites=true&w=majority
