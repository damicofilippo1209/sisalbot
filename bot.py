from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8947407608:AAHuNl3unnUZFv6rgMLhvdIHIuc3k-KzwyU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot attivo!")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot avviato...")
app.run_polling()