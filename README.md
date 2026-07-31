# 🤖 ChityBot - Detector de Expresiones Faciales

ChityBot es un bot de Discord desarrollado en Python capaz de recibir imágenes y analizarlas mediante un modelo de inteligencia artificial para clasificar expresiones faciales.

## 📌 Descripción

El bot permite a los usuarios enviar imágenes mediante comandos de Discord. La imagen es procesada por un modelo de visión por ordenador que analiza la expresión facial y devuelve la clasificación obtenida junto con su nivel de confianza.

El proyecto utiliza Python y la biblioteca `discord.py` para comunicarse con Discord, mientras que el modelo de inteligencia artificial se utiliza para realizar la clasificación de las imágenes.

### 🔎 ¿Cómo funciona?

1. El usuario envía una imagen al bot.
2. El bot recibe y guarda temporalmente la imagen.
3. El modelo de inteligencia artificial analiza la imagen.
4. Se obtiene la expresión facial detectada.
5. El bot muestra el resultado y el porcentaje de confianza.

## 🧠 Expresiones

El modelo puede clasificar diferentes expresiones faciales, como:

- 😀 Felicidad
- 😢 Tristeza
- 😠 Enojo
- 😨 Miedo
- 😮 Sorpresa
- 😐 Neutral

> El proyecto identifica expresiones faciales visibles en una imagen; no determina con certeza el estado emocional real de una persona.

## 💻 Tecnologías utilizadas

- Python
- Discord.py
- Hugging Face Transformers
- PyTorch
- Pillow

## ⚙️ Comandos

| Comando | Función |
|---|---|
| `$hello` | El bot responde con un saludo |
| `$smile` | Genera un emoji |
| `$coin` | Lanza una moneda |
| `$pass` | Genera una contraseña |
| `$dice` | Lanza un dado |
| `$image` | Guarda una imagen enviada al bot |
| `$loaded` | Muestra las imágenes guardadas |
| `$scan` | Analiza una imagen y detecta su expresión facial |


## 🚀 Instalación

Clona el repositorio e instala las dependencias:

```bash
pip install discord.py transformers torch pillow
