	mport os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""🤖 *Welcome to Mr Dakroma Bot!*

Please select an option:

1️⃣ - Help
2️⃣ - Joke
3️⃣ - Quote
4️⃣ - About

Type the number to continue...""", parse_mode='Markdown')

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text.strip()

    if msg == "1":
        await update.message.reply_text("ℹ️ Type /start anytime to see the menu!")
    elif msg == "2":
        await update.message.reply_text("😂 Why do programmers prefer dark mode? Because light attracts bugs!")
    elif msg == "3":
        await update.message.reply_text("💡 Code is like humor. When you have to explain it, it's bad.")
    elif msg == "4":
        await update.message.reply_text("🤖 Bot built by David — Mr Dakroma 😎")
    else:
        await update.message.reply_text("❓ Type /start to see available options!")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
