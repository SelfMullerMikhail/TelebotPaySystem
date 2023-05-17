import os

import telebot
from apiaqsi import ApiAqsiClasses


class Menu:
    def __init__(self, bot=..., user_id=...) -> None:
        self.__STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
        self.bot = bot
        self.user_id = user_id

    def send_menu(self) -> None:
        buttons_categorys = self.get_category()
        keyboard = self.get_category_keyboard(buttons_categorys)
        self.bot.send_message(self.user_id, text="Menu please",
                              reply_markup=keyboard)
        return None

    def get_category_keyboard(self, buttons_categorys: list
                              ) -> telebot.types.InlineKeyboardMarkup:
        keyboard = telebot.types.InlineKeyboardMarkup()
        for butn_name, id in buttons_categorys:
            button = telebot.types.InlineKeyboardButton(
                text=butn_name, callback_data=id)
            keyboard.add(button)
        return keyboard

    def get_category(self):
        self.goodsCategory = ApiAqsiClasses(
            self.__STRIPE_SECRET_KEY).get_goodsCategory()
        self.category_info = self.goodsCategory.goodsCategory_index()
        if self.category_info.status_code == 200:
            self.category_info = self.category_info.json()
            self.categorys = [(n["name"], n["id"]) for n in self.category_info]
            return self.categorys
        else:
            raise Exception("get_category. status_code != 200")
