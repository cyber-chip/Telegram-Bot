from telegram.ext import Updater

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater("5195359469:AAHOPnb2nUtBoPDRMialE_HvzjP2MMvKmhk", use_context=True)
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()

# Вызываем функцию main() - именно эта строчка запускает бота
main()    