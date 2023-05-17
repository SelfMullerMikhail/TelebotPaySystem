import os
import threading

import telebot
from bot_commands.basket_command import Basket
from bot_commands.history_command import History
from bot_commands.inline_handler_command import Inline
from bot_commands.order_command import Order
from bot_commands.settings_command import Settings
from bot_commands.start_command import Start
from bot_commands.stock_command import Stock
from bot_functions.callback_query import CallbackQuery
from bot_functions.text_holder import TextHolder
from dotenv import load_dotenv
from telebot import types

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
BD_PORT = os.getenv("BD_PORT")
BD_PASSWORD = os.getenv("BD_PASSWORD")


__bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None, threaded=False,
                        skip_pending=False)


@__bot.message_handler_start(commands=['start'])
def send_start_hanlder(call: types.ChatJoinRequest):
    threading.Thread(target=Start(__bot, call.from_user.id).send_start,
                     args=(call, )).start()


@__bot.inline_handler(lambda query: True)
def inline_handler(query):
    threading.Thread(target=Inline(__bot).get_inline_menu,
                     args=(query,)).start()


@__bot.message_handler(commands=['order'])
def send_start_hanlder_order(update: types.ChatJoinRequest):
    threading.Thread(target=Order(__bot).send_order, args=(update,)).start()


@__bot.message_handler(commands=['basket'])
def send_start_hanlder_basket(update: types.ChatJoinRequest):
    threading.Thread(target=Basket(__bot, update.from_user.id).send_basket,
                     args=()).start()


@__bot.message_handler(commands=['stock'])
def send_start_hanlder_stock(update: types.ChatJoinRequest):
    threading.Thread(target=Stock(__bot, update.from_user.id).send_stock,
                     args=()).start()


@__bot.message_handler(commands=['history'])
def send_start_hanlder_history(update: types.ChatJoinRequest):
    threading.Thread(target=History(__bot, update.from_user.id).send_history,
                     args=()).start()


@__bot.message_handler(commands=['settings'])
def send_start_hanlder_settigs(update: types.ChatJoinRequest):
    threading.Thread(target=Settings(__bot, update.from_user.id).send_settings,
                     args=()).start()


@__bot.callback_query_handler(func=lambda call: True)
def callback_query_handler(call: types.CallbackQuery):
    threading.Thread(target=CallbackQuery(__bot, call.from_user.id).
                     callback_query, args=(call,)).start()


@__bot.message_handler(content_types='text')
def text_holder_hanlder(call: types.CallbackQuery):
    threading.Thread(target=TextHolder(__bot, call.from_user.id).text_holder,
                     args=()).start()


if __name__ == "__main__":
    # tg_bot = threading.Thread(target=__bot.polling, kwargs={"non_stop":True})

    # mailing = Mailing1()
    # malling = threading.Thread(target=mailing.example_func, args=())
    # malling.start()
    # bot_commands_list = get_bot_commands(BOT_COMMANDS)
    # __bot.set_my_commands(bot_commands_list)
    # tg_bot.start()
    __bot.polling(non_stop=True)
