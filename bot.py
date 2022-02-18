
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
#Будем записывать отчет о работе бота
logging.basicConfig(filename='bot.log', level=logging.INFO)

# Настройки прокси
PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }
}

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

#Бот вызовет функцию greet_user, когда пользователь напишет команду /start или
#нажмет кнопку Start при первом подключении к боту.

def greet_user(update, context):
    print('Вызван /start')

    #Ответим пользователю на его сообщение при помощи update.message.reply_text():
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

# Вызываем функцию main() - именно эта строчка запускает бота
main()    

#Напишем функцию talk_to_me, которая будет "отвечать" пользователю

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)