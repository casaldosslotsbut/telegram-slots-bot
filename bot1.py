from telegram import Bot
import random
from datetime import datetime
import pytz
import os

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

jogos = [
    "Fortune Tiger 🐯",
    "Fortune Ox 🐮",
    "Fortune Rabbit 🐇",
    "Dragon Hatch 🐉",
    "Ganesha Gold 🐘",
    "Sweet Bonanza 🍬",
    "Gates of Olympus ⚡"
]

agora = datetime.now(pytz.timezone("America/Sao_Paulo")).strftime("%H:%M")
jogo = random.choice(jogos)

mensagem = f"""
⏰ HORÁRIO DOS SLOTS ⏰

🎮 Jogo: {jogo}
⏰ Horário: {agora}

⚠️ Palpite
🎰 Jogue com responsabilidade
🔞 Proibido para menores
"""

bot.send_message(chat_id=CHAT_ID, text=mensagem)
