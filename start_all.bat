@echo off

start "" python C:\ExchangeBot\rate_bot.py

timeout /t 5 >nul

start "" python C:\ExchangeBot\hengmet_monitor.py
