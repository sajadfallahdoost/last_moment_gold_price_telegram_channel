import schedule
import time
from .fetcher import fetch_latest_prices
from .telegram_bot import post_to_telegram
from .enums import CurrencyType
from .logger import setup_logger

logger = setup_logger()


def process_prices():
    data = fetch_latest_prices()
    if data:
        harat_buy = data.get(CurrencyType.HARET_BUY.value, {}).get('value', 'N/A')
        harat_sell = data.get(CurrencyType.HARET_SELL.value, {}).get('value', 'N/A')
        change_buy = data.get(CurrencyType.HARET_BUY.value, {}).get('change', 'N/A')
        change_sell = data.get(CurrencyType.HARET_SELL.value, {}).get('change', 'N/A')
        timestamp = data.get(CurrencyType.HARET_BUY.value, {}).get('date', 'N/A')

        message = (f"Latest Prices:\nBuy: {harat_buy} Toman (Change: {change_buy})\n"
                f"Sell: {harat_sell} Toman (Change: {change_sell})\nUpdated: {timestamp}")
        post_to_telegram(message)
    else:
        logger.error("No data available to send to Telegram.")


def start_scheduler():
    logger.info("Starting scheduler to fetch prices every 5 minutes.")
    schedule.every(5).minutes.do(process_prices)
    while True:
        schedule.run_pending()
        time.sleep(1)
