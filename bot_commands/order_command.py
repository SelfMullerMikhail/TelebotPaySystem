import os
import sys

from telebot import types

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from CONSTANTS import get_order_info
from CONSTANTS import BUTON_MENU, BUTTON_BASKET, BUTTON_STOCK

class Order:
    def __init__(self, bot) -> None:
        self.__bot = bot
        
    def send_order(self, update):
        keyboard = types.InlineKeyboardMarkup()
        menu_button = types.InlineKeyboardButton(text=BUTON_MENU, 
                                switch_inline_query_current_chat="tesffft")
        stock_button = types.InlineKeyboardButton(text=BUTTON_STOCK, 
                                callback_data="stock_button")
        basket_button = types.InlineKeyboardButton(text=BUTTON_BASKET, 
                                                    callback_data="basket")
        
        keyboard.add(menu_button, stock_button, basket_button)
        text = get_order_info(discount=0, discount_money=0,
                            summ=100, city="Москва",
                            address="Улица пушкина, дом колотушкина")
        self.__bot.send_message(update.chat.id, text, reply_markup=keyboard)