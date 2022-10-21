import logging
from aiogram.utils import executor
from coin import  dp

from handlers import client, callback, fsmAdminMentor, eztra

client.register_handler_client(dp)
callback.register_handler_callback(dp)
fsmAdminMentor.register_handler_fsmAdminMentor(dp)
eztra.register_handler_ezta(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)


# Создайте FSMAdmin для создания списка
# менторов в отдельном файле fsmAdminMentor.
# Должны запрашиваться следущие данные:
# - ID ментора.
# - Имя ментора.
# - Напрвление.
# - Возраст ментора.
# - Группа
# Все это нужно записать в FSMCONTEXT PROXY
# STORAGE.
# Как на уроке, только для Менторов.
# ДОЛЖНО РАБОТАТЬ ТОЛЬКО ДЛЯ
# АДМИНИСТРАТОРА (Куратора) БОТА!