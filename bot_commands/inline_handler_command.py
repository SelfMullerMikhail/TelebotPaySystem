import os
import sys
import time
from dotenv import load_dotenv
from telebot import types

from apiaqsi import GoodsAqsi

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(dotenv_path='env_file.env')

from CONSTANTS import APPROVE_TEXT


class Inline:
    def __init__(self, bot=None) -> None:
        self.__bot = bot
        
        
    def get_inline_menu(self, query=None):
        if query != None:
            user_id = query.from_user.id
            query_id = query.id
        goods = self.get_goods()
        result = self.get_button_list(goods)
        if self.__bot != None:
            self.__bot.answer_inline_query(query.id, result)
            
    def get_button_list(self, goods):
        results = []
        for i in goods:
            keyboard = self.get_callback_data(i)
            btn = self.get_goods_buttons(title=i[0], 
                                        callback_data_info=keyboard,
                                        price = i[2],
                                        goods_id=i[3])
            results.append(btn)
        return results
        
    def get_callback_data(self, i):
        time.sleep(3)
        return f'inline_{i[0]}_{i[2]}_{i[1]}'
        
    def get_goods_buttons(self, goods_id, callback_data_info, price, title,
                        thumbnail_url=...):
        keyboard_mark = types.InlineKeyboardMarkup()
        keyboard_btn = types.InlineKeyboardButton(text=APPROVE_TEXT,
                                            callback_data=callback_data_info)
        keyboard_mark.add(keyboard_btn)
        main_text = f"""{title} - {price} ₽""" 
        
        btn = types.InlineQueryResultArticle(
        id=goods_id,
        title= main_text,
        input_message_content=types.InputTextMessageContent(message_text=
                                                            main_text),
        reply_markup=keyboard_mark,
        )
        return btn
        
    def get_goods(self):
        goods = GoodsAqsi(os.getenv("STRIPE_SECRET_KEY")).goods_index()
        if goods.status_code == 200:
            return [(n["name"], n["id"], n["price"], n["group_id"]) for n in 
                                                        goods.json()["rows"]]
        else:
            raise Exception(f"get_goods is error {goods.response}")
        
if __name__ == "__main__":
    obj = Inline()
    info = obj.get_inline_menu()