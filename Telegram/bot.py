import logging
import os
import telegram
import random
from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
import time


#Configurar Logging
logging.basicConfig(
  level=logging.INFO, format = " %(asctime)s - %(name)s - %(levelname)s - %(message)s,"
)
logger=logging.getLogger()

#Solicitar Token

TOKEN = "1686868043:AAGomDK3Tvdu31IUHPHvgzio1PlG-4pFIko"

def start(update,context):
  logger.info(f"El usuario {update.effective_user['username']}, ha iniciado una conversacion")
  name = update.effective_user['first_name']
  update.message.reply_text(f"Hola {name} yo soy tu bot")
  #print("Hola entro aqui")

def datos(update,context):
  logger.info(f"El usuario {update.effective_user['username']}, ha iniciado una conversacion")
  name = update.effective_user['first_name']
  idd = update.effective_user['id']
  apellido = update.effective_user['last_name']
  username = update.effective_user['username']
  bott=update.effective_user['is_bot']

  if (not bott):
    update.message.reply_text(f"Hola, yo soy tu bot\nTu nombre es: {name}\nTu apellido es: {apellido}\nTu id es: {idd}\nTu username es: {username} \nY no eres un bot: {bott}")
  else:
    update.message.reply_text(f"Hola, yo soy tu bot\nTu nombre es: {name}\nTu apellido es: {apellido}\nTu id es: {idd}\nTu username es: {username} \nEres un bot: {bott}")
  #print("Hola entro aqui")

def random_number(update,context):
  user_id = update.effective_user['id']
  #print(update.effective_user)
  #Para imprimir
  print(user_id)
  logger.info(f'El usuario {user_id}, ha solicitado un numero aleatorio')
  number = random.randint(0,10)
  context.bot.sendMessage(chat_id = user_id, parse_mode = "HTML",text = f"<b>Numero</b>  aleatorio: \n {number}")


def info(update,context):
  user_id = update.effective_user['id']
  logger.info(f'El usuario {user_id}, ha solicitado la linea de comandos')
  update.message.reply_text("Mis funciones son:\n\n   /start: Te saludo\n   /random: Te doy un numero aleatorio\n    /info: Te doy mis comandos\n   /datos: Te doy tus datos\n\nSi me manda otro mensaje te lo repito")

def echo(update, context):
  user_id = update.effective_user['id']
  logger.info(f"El usuario {user_id}, ha enviado un mensaje de texto")
  text = update.message.text


  context.bot.sendMessage(
  chat_id=user_id,
  parse_mode = "MarkdownV2",
  text = f"*Escribiste: *\n_{text}_"
  )


def comprobar_notificaciones():
  comprobar=True
  if comprobar==True:
    user_id = "Cjo148"
    #Para imprimir
    logger.info('Entro aqui')
    #sendMessage(chat_id = user_id, parse_mode = "HTML",text = "<b>Numero</b>  aleatorio: ")



if __name__ == "__main__":
  #Obtenemosinformacion de nuestro bot
  my_bot = telegram.Bot(token=TOKEN)
  #print(my_bot.getMe())


  #Enlanzar nuestro Updater con nuestro bot
  updater = Updater(my_bot.token, use_context=True)

  #Creamos un despachador
  dp = updater.dispatcher

  #creamos los manejadores
  dp.add_handler(CommandHandler("start",start))
  
  dp.add_handler(CommandHandler("random",random_number))

  dp.add_handler(CommandHandler("datos",datos))

  dp.add_handler(CommandHandler("info",info))

  dp.add_handler(MessageHandler(Filters.text, echo))

 #comprobar_notificaciones()

#Aqui pregunta si hay nuevos mensajes
updater.start_polling()
print("Bot Cargado")
#Aqui para cerrar la consola con control + C
updater.idle()