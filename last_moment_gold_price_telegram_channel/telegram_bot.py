from telegram import Bot
from .config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID
from .logger import setup_logger

logger = setup_logger()
bot = Bot(token=TELEGRAM_BOT_TOKEN)


def post_to_telegram(message):
    try:
        bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message)
        logger.info("Message sent to Telegram successfully.")
    except Exception as e:
        logger.error(f"Failed to send message to Telegram: {str(e)}")
