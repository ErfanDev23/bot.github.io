from flask import Flask, render_template, request
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

app = Flask(__name__)

# توکن ربات تلگرام
TOKEN = '8092848536:AAGNgi2G2h-nfv7xwa2k72sOgRuRXq_0fK8'
bot = Bot(token=TOKEN)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    chat_id = request.form['chat_id']
    message = request.form['message']
    bot.send_message(chat_id=chat_id, text=message)
    return 'Message sent!'

if __name__ == '__main__':
    app.run(debug=True)
