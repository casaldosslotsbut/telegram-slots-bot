import os
import asyncio
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("TOKEN")

async def start(update, context):
    await update.message.reply_text("🤖 Bot Slots ativo!")

async def main():
    if not TOKEN:
        raise RuntimeError("TOKEN não encontrado nos Secrets")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot rodando...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
