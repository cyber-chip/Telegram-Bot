
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
#Будем записывать отчет о работе бота
logging.basicConfig(filename='bot.log', level=logging.INFO)

# Настройки прокси
PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

#Бот вызовет функцию greet_user, когда пользователь напишет команду /start или
#нажмет кнопку Start при первом подключении к боту.        
def greet_user(update, context):
    print("Вызван /start")
    update.message.reply_text("Здравствуй, пользователь!")


#Напишем функцию talk_to_me, которая будет "отвечать" пользователю
def talk_to_me(update, context):
    text = update.message.text
    print(text)
    #Ответим пользователю на его сообщение при помощи update.message.reply_text():
    update.message.reply_text(text)

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    #будем использовать диспетчер mybot.dispatcher для того, 
    # чтобы при наступлении события вызывалась наша функция:
    p = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))

    #Добавим новый обработчик событий в main()
    #При использовании MessageHandler укажем, что мы 
    #хотим реагировать только на текстовые сообщения - Filters.text
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    #Залогируем в файл информацию о старте бота
    logging.info("Бот стартовал")
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()

    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

# В питоне есть общепринятый способ решить эту проблему. Если вам нужно вызвать 
# функцию не внутри другой функции, она заключается в специальный блок, который 
# исполняется только при прямом вызове файла python bot.py и не вызывается при
#  импорте, например from bot import PROXY. Вот как это выглядит:

if __name__ == "__main__":

    # Вызываем функцию main() - именно эта строчка запускает бота
    main()    

