import telebot
from config import token
from logic import Pokemon

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['go'])
def go(message):
    username = message.from_user.username
    if username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['set_name'])
def set_name(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        new_name = message.text.split(' ', 1)[1]
        Pokemon.pokemons[username].update_name(new_name)
        bot.reply_to(message, f"Имя твоего покемона изменено на {new_name}")
    else:
        bot.reply_to(message, "Ты ещё не создал покемона")

bot.infinity_polling(none_stop=True)
