
from telegram.ext import Updater, MessageHandler, Filters

TOKEN = "5742426469:AAFd__uxzh5WWFnrD6gKRh2n00yFrXpTdZg"

def echo(update, context):
    txt = update.message.text
    if txt.lower() in ['привет', 'салам']:
        txt = "И тебе Салам пополам мой друг!"
    elif txt.lower() in ['как здоровье чел?']:
        txt = "Пока жив роднуля"
    update.message.reply_text(txt)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    print("Бот запущен")

    dp.add_handler(MessageHandler(Filters.text, echo))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()