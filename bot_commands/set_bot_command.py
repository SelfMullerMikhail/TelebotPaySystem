import telebot


def get_bot_commands(commands):
    commands = [telebot.types.BotCommand(command[0], command[1]) for command in commands]
    return commands


# создаем объект бота
# bot = telebot.TeleBot('your_token')


# # список команд бота
# commands = [
#     telebot.types.BotCommand('/start', emoji.emojize(':smiling_face_with_smiling_eyes:') + 'Начать работу с ботом'),
#     telebot.types.BotCommand('/help', emoji.emojize(':smiling_face_with_smiling_eyes:') + 'Помощь'),
#     telebot.types.BotCommand('/settings', emoji.emojize(':smiling_face_with_smiling_eyes:') + 'Настройки')
# ]

# # устанавливаем список команд бота
# bot

# # запускаем бота
# bot.polling()
