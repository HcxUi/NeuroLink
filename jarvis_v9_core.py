
from voice_utils import listen, speak
from daily_logger import log_entry
from telegram_reply import reply_to_telegram
from voice_file_organizer import organize_downloads

def main():
    speak("Jarvis V9 activated with secure memory.")
    while True:
        command = listen()
        log_entry(command)

        if "exit" in command:
            speak("Shutting down Jarvis V9.")
            break
        elif "organize downloads" in command:
            organize_downloads()
        elif "telegram" in command:
            reply_to_telegram()
        elif "daily report" in command:
            with open("activity_summary.txt") as f:
                for line in f.readlines()[-5:]:
                    speak(line.strip())
        else:
            speak("Command not recognized.")

if __name__ == "__main__":
    main()
