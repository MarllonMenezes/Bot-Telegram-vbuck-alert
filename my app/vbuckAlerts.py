import requests
from bs4 import BeautifulSoup
import telebot
import schedule
import time
from config import botToken

bot = telebot.TeleBot(botToken)

def get_vbucks_alert():
    url = "https://fortnitedb.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'table asummary', 'id': 'summarytb'})
    rows = table.find_all('tr')

    vbucks_alerts = []
    suffixes = [" Stonewood", " Plankerton", " Canny Valley", " Twine Peaks", " Total de Vbucks"]

    for row in rows:
        columns = row.find_all('td')
        if len(columns) > 0 and 'V-Bucks' in columns[1].text:
            for i, column in enumerate(columns[2:]):  # Começa a partir da terceira coluna
                links = column.find_all('a')
                for link in links:
                    vbucks_alerts.append(link.text + suffixes[i])

    if vbucks_alerts:
        return "*⚠️ ALERTA DE VBUCKS - SALVE O MUNDO ⚠️*\n\n" + "\n\n".join(vbucks_alerts)
    else:
        return "*⚠️ ALERTA DE VBUCKS - SALVE O MUNDO ⚠️*\n\nNo V-Bucks alert today."

@bot.message_handler(commands=['alert'])
def send_alert(message):
    vbucks_alert = get_vbucks_alert()
    bot.reply_to(message, vbucks_alert, parse_mode='Markdown')

def job():
    vbucks_alert = get_vbucks_alert()
    bot.send_message(1846501521, vbucks_alert, parse_mode='Markdown')

schedule.every().day.at("21:01").do(job)

bot.polling()

while True:
    schedule.run_pending()
    time.sleep(1)