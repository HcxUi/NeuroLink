
import telepot
from voice_utils import speak

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = telepot.Bot(TOKEN)

def reply_to_telegram():
    updates = bot.getUpdates()
    if not updates:
        speak("No new Telegram messages.")
    else:
        for u in updates[-3:]:
            msg = u['message']
            sender = msg['from']['first_name']
            text = msg['text']
            speak(f"{sender} said: {text}")
