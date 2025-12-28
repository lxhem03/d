import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8190792814:AAE-wulapTPufU68xykzoRTktgH3O8pcGck")
API_ID = int(os.environ.get("API_ID", "23340285"))
API_HASH = os.environ.get("API_HASH", "ab18f905cb5f4a75d41bb48d20acfa50")
ADMINS = [int(id) for id in os.environ.get("ADMINS", "7465574522").split(",")]
DB_URI = os.environ.get("DB_URI", "mongodb+srv://RahulPrince720:Q7qg69E1oH30LT6d@cluster0.fb0ldjk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "contentXsaverobot")
LOG_CHANNEL = -1003553966358
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
KEEP_ALIVE_URL = os.environ.get("KEEP_ALIVE_URL", "")
