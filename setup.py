from setuptools import setup, find_packages

setup(
    name='last_moment_gold_price_telegram_channel',  # Use underscores instead of spaces and avoid special characters
    version='0.1',
    description='A package to fetch the latest gold prices and post to Telegram channel',
    author='sajad',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-telegram-bot',
        'schedule',
    ],
    entry_points={
        'console_scripts': [
            'start-scheduler=last_moment_gold_price.scheduler:start_scheduler',
        ],
    },
)
