from telebot import types
from logic import simplify_kmap
from config import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)
user_data = {}

def request_values(chat_id, value_index=1):
    question = f"Введите значение для комбинации {value_index} (A, B = 0 или 1):"
    msg = bot.send_message(chat_id, question)
    bot.register_next_step_handler(msg, process_value_input, value_index)

def process_value_input(message, value_index):
    chat_id = message.chat.id
    value = message.text.strip()

    # Проверка на корректный ввод
    if value not in ['0', '1']:
        msg = bot.reply_to(message, "Некорректный ввод. Пожалуйста, введите 0 или 1.")
        bot.register_next_step_handler(msg, process_value_input, value_index)
        return

    # Сохраняем значение и переходим к следующему или завершаем ввод
    if chat_id not in user_data:
        user_data[chat_id] = {'values': []}
    user_data[chat_id]['values'].append(int(value))

    if value_index < 4:
        request_values(chat_id, value_index + 1)
    else:
        simplified_expression = simplify_kmap(user_data[chat_id]['values'])
        bot.send_message(chat_id, f"Упрощенная булева функция:\n{simplified_expression}")
        del user_data[chat_id]  # Очищаем данные пользователя после завершения




@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = ("Привет! Я BoolSimplifyBot 🤖\n"
                    "Я помогу упростить твои булевы выражения с помощью карты Карно.\n"
                    "Нажмите на кнопку 'Начать ввод 🧮', чтобы начать вводить значения функции.")
    bot.reply_to(message, welcome_text, reply_markup=generate_markup())


def generate_markup():
    markup = types.InlineKeyboardMarkup()
    begin_button = types.InlineKeyboardButton(text='Начать ввод 🧮', callback_data='begin_input')
    markup.add(begin_button)
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'begin_input':
        request_values(call.message.chat.id)