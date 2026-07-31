from main import settings
import discord
import os
import uuid
from transformers import pipeline
from PIL import Image
# import * - es una forma rápida de importar todos los archivos de la biblioteca
from bot_logic import *

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

modelo = pipeline(
    "image-classification",
    model="dima806/facial_emotions_image_detection"
)

# Una vez que el bot esté listo, ¡imprimirá su nombre!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')



# Cuando el bot reciba un mensaje, ¡enviará mensajes en el mismo canal!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('¡Hola! Soy un bot')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('$dice'):
        await message.channel.send(dice_roll())
    elif message.content.startswith('$image'):
        # Verificar si el mensaje tiene archivos adjuntos
        if len(message.attachments) == 0:
            await message.channel.send("❌ No enviaste ninguna imagen.")
            return

        # Crear la carpeta si no existe
        os.makedirs("images", exist_ok=True)

        # Tomar el primer archivo adjunto
        attachment = message.attachments[0]

        # Comprobar que sea una imagen
        if not attachment.content_type or not attachment.content_type.startswith("image/"):
            await message.channel.send("❌ El archivo adjunto no es una imagen.")
            return

        # Generar un nombre único conservando la extensión
        extension = os.path.splitext(attachment.filename)[1]
        filename = f"{uuid.uuid4()}{extension}"

        # Guardar la imagen
        path = os.path.join("images", filename)
        await attachment.save(path)

        await message.channel.send(f"✅ Imagen guardada como **{filename}**")
    elif message.content.startswith('$scan'):
            # Verificar si el mensaje tiene archivos adjuntos
            if len(message.attachments) == 0:
                await message.channel.send("❌ No enviaste ninguna imagen.")
                return

            # Crear la carpeta si no existe
            os.makedirs("images", exist_ok=True)

            attachment = message.attachments[0]

            # Comprobar que sea una imagen
            if not attachment.content_type or not attachment.content_type.startswith("image/"):
                await message.channel.send("❌ El archivo adjunto no es una imagen.")
                return

            # Generar nombre único
            extension = os.path.splitext(attachment.filename)[1]
            filename = f"{uuid.uuid4()}{extension}"

            # Guardar imagen
            path = os.path.join("images", filename)
            await attachment.save(path)

            # Analizar expresión
            await message.channel.send("🔎 Analizando expresión facial...")

            imagen = Image.open(path)
            resultado = modelo(imagen)

            mejor = resultado[0]

            expresion = mejor["label"]
            confianza = mejor["score"] * 100

            await message.channel.send(
                f"📸 **Expresión detectada:** {expresion}\n"
                f"📊 **Confianza:** {confianza:.1f}%"
            )
    elif message.content.startswith('$loaded'):
            # Verificar si existe la carpeta
            if not os.path.exists("images"):
                await message.channel.send("📂 No hay imágenes cargadas.")
                return

            # Obtener las imágenes
            archivos = os.listdir("images")

            imagenes = []

            for archivo in archivos:
                extension = os.path.splitext(archivo)[1].lower()

                if extension in [".png", ".jpg", ".jpeg", ".gif", ".webp"]:
                    imagenes.append(archivo)

            # Comprobar si hay imágenes
            if len(imagenes) == 0:
                await message.channel.send("📂 No hay imágenes cargadas.")
                return

            await message.channel.send(
                f"📸 **Imágenes cargadas: {len(imagenes)}**"
            )

            # Enviar las imágenes
            for archivo in imagenes:
                path = os.path.join("images", archivo)

                await message.channel.send(
                    file=discord.File(path)
                )
    else:
        await message.channel.send("No puedo procesar este comando, ¡lo siento!")

client.run(settings["TOKEN"])