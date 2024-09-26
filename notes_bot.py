from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from function import *


#настройка логирования 
logging.basicConfig(level=logging.INFO, filename='./log/bot.log', filemode='a+', format='%(filename)s #%(levelname)s - %(asctime)s - %(message)s', datefmt='%d.%b %H:%M')
# Для отладки: DEBUG | INFO
# logging.basicConfig(format=u'%(filename)s #%(levelname)s %(message)s', level=logging.INFO)


bot = Bot(token=TOKEN)  # Инициализация бота с токеном 
dp = Dispatcher(bot, storage=MemoryStorage())  # Создание диспетчера с хранилищем состояний в памяти


async def shutdown(dispatcher: Dispatcher):  
    # Закрываем соединение с хранилищем состояний
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == "__main__":
    # импортируем все обработчики и состояния из соответсвующих модулей (dp из __init__.py)
    from handlers import *
    from states import *

    executor.start_polling(dp, skip_updates=False, on_shutdown=shutdown) # запускаем цикл обработки обновлений 
