def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2  # Целочисленное деление
        guess = list[mid]
        if guess == item:        # Если элемент найден
            return mid
        if guess > item:         # Ищем в левой половине
            high = mid - 1
        else:                    # Ищем в правой половине
            low = mid + 1
    return None  # Элемент не найден

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 9))  # Выведет 1 (индекс числа 3)

from telebot import TeleBot
from config import TOKEN, state_storage
from handlers import start, services, citizen_services, org_services, consultation, feedback, prices, info


def main():
    # Инициализация бота
    bot = TeleBot(TOKEN, state_storage=state_storage)

    # Регистрация всех обработчиков
    start.register_handlers(bot)
    services.register_handlers(bot)
    citizen_services.register_handlers(bot)
    org_services.register_handlers(bot)
    consultation.register_handlers(bot)
    feedback.register_handlers(bot)
    prices.register_handlers(bot)
    info.register_handlers(bot)

    # Запуск бота
    print("Бот запущен...")
    bot.infinity_polling()


if __name__ == "__main__":
    main()

print("this info is from branch vetka")

