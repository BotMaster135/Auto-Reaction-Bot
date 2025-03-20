from os import environ

API_HASH = environ.get("API_HASH", "340f87444e648a712eae77c310648e21")
API_ID = int(environ.get("API_ID", "26597768"))
BOT_TOKEN = environ.get("BOT_TOKEN", "7675882405:AAEiAqtJz96hwxXH1cf7lRdT18oJa0MzOv0")
BOT_OWNER = int(environ.get("BOT_OWNER", "@botmaster55"))
BOT_USERNAME = environ.get("BOT_USERNAME", "ReactionAuto1_bot")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002309087993"))
AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002046895970"))
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://dbmongo702:xtb9PzLmv5dstZYG@cluster0.2dxbh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Define default emojis list
EMOJIS = [
    "👍", "🤷‍♂", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🤬", "😢", 
    "🥶", "🤩", "🥳", "😎", "🙏", "👌", "🤣", "😇", "🥱", "🥴", "😍", "🤓", 
    "❤‍🔥", "🌚", "😐", "💯", "🦄", "⚡", "👾", "🏆", "💔", "🤨", "🌟", "😡", 
    "👅", "🆒", "😘", "😈", "😴", "😭", "👻", "🌈", "👨‍💻", "👀", "🎃", "🙄", 
    "🤧", "😨", "🤝", "🤐", "🤗", "🫡", "🤭", "🥸", "🤫", "😶‍🌫", "🤪", "😏"
]
