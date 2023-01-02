import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5915835203:AAEDu_D3pwygOxtvpDXrPWunMSc57vAXqFU")
API_ID = int(os.environ.get("API_ID", "2054877"))
API_HASH = os.environ.get("API_HASH", "4227c1e45e462209a3dcc67ada88a44f")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001366123484"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "957158815").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://duke:duke@cluster0.iebnx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
