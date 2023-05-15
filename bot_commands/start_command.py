import os
import sys
from  telebot import types

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from CONSTANTS import BUTTON_SHOPS, BUTTON_CONTACT_INFO, BUTTON_SETTINGS, \
    CONTROLL_PANEL



class Start:
    def __init__(self, bot, user_id) -> None:
        self.__bot = bot
        self.user_id = user_id
        
    def send_start(self, call):
        keyboard = types.ReplyKeyboardMarkup()
        button_shops = types.InlineKeyboardButton(text=BUTTON_SHOPS, 
                                                callback_data="button_shops")
        button_contact_info = types.InlineKeyboardButton(text=
                    BUTTON_CONTACT_INFO, callback_data="button_contact_info")
        button_settings = types.InlineKeyboardButton(text=BUTTON_SETTINGS,
                                            callback_data="button_settings")
        keyboard.add(button_shops)
        keyboard.add(button_contact_info, button_settings)
        self.__bot.send_message(call.from_user.id, CONTROLL_PANEL,
                                                        reply_markup=keyboard)
        