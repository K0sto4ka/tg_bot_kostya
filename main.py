
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
TOKEN = "5742426469:AAFd__uxzh5WWFnrD6gKRh2n00yFrXpTdZg"

from Wiki import search_wiki

def echo(update, context):
    txt = update.message.text
    if txt.lower() in ['привет', 'салам']:
        txt = "И тебе Салам пополам мой друг!"
    elif txt.lower() in ['как здоровье чел?']:
        txt = "Пока жив роднуля"
    update.message.reply_text(txt)

def start(update, context):
    update.message.reply_text("Это учебный бот.\nДля вывоза помощи наберите /help")


def help(update, context):
    update.message.reply_text("Для вызова помощи наберите /help \nДля поиска в википедии наберите /wiki <текст для поиска>")


def wikiword(update, context):
    print(context.args)
    word = " ".join(context.args)
    if word:
        update.message.reply_text("Идёт поиск...")
        result, url = search_wiki(word)
        update.message.reply_text(result+url)
    else:
        update.message.reply_text("Необходимо ввести текст для поиска")




def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    print("Бот запущен")


    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("wiki", wikiword))




    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()