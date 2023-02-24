from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv('API_ID','3369707'))
API_HASH = getenv('API_HASH','aec1fd7abdfec322c426961a570ef336')

BOT_TOKEN = getenv('BOT_TOKEN','6148408277:AAHW-0O3LWUby1HLocCQSc2HQj9bRlblQfk')
OWNER_ID = int(getenv('OWNER_ID','1115053159'))

MONGO_DB_URI = getenv('MONGO_DB_URI','mongodb+srv://amdlinkzz:phoenix06@cluster0.n3s2u8t.mongodb.net/?retryWrites=true&w=majority')
MUST_JOIN = getenv('MUST_JOIN', 'AMD_LinkZz')
