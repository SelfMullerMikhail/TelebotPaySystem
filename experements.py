# from bot_functions.left_chat_member import LeftChat
# from bot_functions.join_request import JoinRequest

# @__bot.message_handler(content_types=['left_chat_member'])
# def left_chat_member_handler(update: types.ChatMemberLeft):
#     threading.Thread(target=LeftChat().left_chat_member, 
#         args=(update,)).start()

# @__bot.message_handler(content_types=['new_chat_members'])
# def join_request_handler(update: types.ChatJoinRequest):
#     threading.Thread(target=JoinRequest().join_request, 
#         args=(update,)).start()
    
# # Окно оповещения на весь экран
# __bot.answer_callback_query(callback_query_id=call.id, text="Привет, мир!", show_alert=True)

# from apiaqsi import ApiAqsiClasses
# from apiaqsi.aqsi_types.aqsi_types import *
# from apiaqsi import ShopsAqsi
# from apiaqsi import DeviceAqsi
# from apiaqsi import CashiersAqsi
# from apiaqsi import ReceiptsAqsi
# from apiaqsi import Slips
# from apiaqsi import ShiftsAqsi
# from apiaqsi import GoodsAqsi
# from apiaqsi import GoodsCategoryAqsi
# from apiaqsi import ClientsAqsi
# from apiaqsi import OrdersAqsi

# # markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
# # markup.add(types.KeyboardButton('Кнопка 1'))
# # markup.add(types.KeyboardButton('Кнопка 2'))
# # markup.add(types.KeyboardButton('Кнопка 3'))
# # bot.send_message(message.chat.id, "Выберите действие:", reply_markup=markup)

import base64
a = base64.b64decode("Y29mZmVlJjE0MSYw")
print(a)

# if call.data == 'button_pressed':
#     # Меняем текст сообщения и устанавливаем кнопки
#     text = 'Новый текааааст'
#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.add(types.InlineKeyboardButton(text='Нажми меня', callback_data='button_pressed'))
#     # Редактируем сообщение и оставляем текст в поле ввода
#     __bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text, reply_markup=keyboard)