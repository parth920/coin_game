import telebot
from telebot import types

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
print("Starting bot...")
bot = telebot.TeleBot('7252079345:AAFo5O8mJ5VhXfmxFjj1KlluxzvykEY8UnU')

# URL of your Python HTTP server hosting the game
game_url = 'https://parth920.github.io/coin_game/'  # Replace with the URL of your Python HTTP server

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("Received /start command")
    user_id = message.chat.id

    markup = types.InlineKeyboardMarkup(row_width=1)
    game_button = types.InlineKeyboardButton("Play Game", url=game_url)
    markup.add(game_button)

    bot.send_message(user_id, "Welcome! Click the button below to play the game:", reply_markup=markup)

@bot.message_handler(commands=['playgame'])
def play_game(message):
    print("Received /playgame command")
    user_id = message.chat.id

    markup = types.InlineKeyboardMarkup(row_width=1)
    game_button = types.InlineKeyboardButton("Play Game", url=game_url)
    markup.add(game_button)

    bot.send_message(user_id, "Redirecting you to the game...", reply_markup=markup)

print("Starting polling...")
bot.polling()
