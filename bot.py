from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask
from threading import Thread

TOKEN = "8947407608:AAHuNl3unnUZFv6rgMLhvdIHIuc3k-KzwyU"

app_web = Flask(__name__)

@app_web.route("/")
def home():
    return "Bot attivo"

def run_web():
    app_web.run(host="0.0.0.0", port=10000)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot attivo!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

Thread(target=run_web).start()

print("Bot avviato...")
app.run_polling()