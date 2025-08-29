import telebot

# Вставь сюда токен, который дал BotFather
BOT_TOKEN = "ВАШ_BOTFATHER_TOKEN"
bot = telebot.TeleBot(BOT_TOKEN)

# Список VPN-ключей (например, из Outline Manager)
vpn_keys = [
    "ss://ключ_1",
    "ss://ключ_2",
    "ss://ключ_3",
]

user_keys = {}  # чтобы ключи не повторялись

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для покупки VPN.\nНапиши /buy чтобы получить доступ.")

@bot.message_handler(commands=['buy'])
def buy(message):
    if message.chat.id in user_keys:
        bot.send_message(message.chat.id, f"Ты уже получил ключ:\n{user_keys[message.chat.id]}")
        return

    if vpn_keys:
        key = vpn_keys.pop(0)
        user_keys[message.chat.id] = key
        bot.send_message(message.chat.id, f"Спасибо за покупку!\nВот твой VPN-ключ:\n{key}")
    else:
        bot.send_message(message.chat.id, "Ключи закончились. Попробуй позже.")

bot.infinity_polling()
