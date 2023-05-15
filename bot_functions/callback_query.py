import os
import sys

from telebot import types

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from CONSTANTS import DONE_TEXT




class CallbackQuery:
    def __init__(self, bot, user_id) -> None:
        self.__bot = bot
        self.user_id = user_id
        
    def callback_query(self, call):
        func = call.data.split("_")
        if func[0] == "inline":
            keyboard_mark = types.InlineKeyboardMarkup()
            types.InlineKeyboardMarkup()
            keyboard_btn = types.InlineKeyboardButton(text=DONE_TEXT,
                                                    callback_data="test")
            keyboard_mark.add(keyboard_btn)
            text_info = f"{func[1]} - {func[2]} ₽"
            return self.__bot.edit_message_text(
                inline_message_id=call.inline_message_id,
                text=text_info,
                reply_markup=keyboard_mark)