"""
Лабораторная работа №7 — Работа с API
Студент: Denis Novikov-Ahbabovic
Вариант 6 — Steam Web API
"""

from datetime import datetime
import requests
from config import OPENWEATHER_API_KEY


def show_weather():
    city_name = "Sarajevo"
    country_code = "BA"

    print("=" * 55)
    print("ЗАДАНИЕ 1. OPENWEATHERMAP")
    print("=" * 55)

    if not OPENWEATHER_API_KEY.strip():
        print("API-ключ не указан. Откройте config.py и вставьте ключ.")
        print()
        return

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{city_name},{country_code}",
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "ru"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            print(f"Город:              {data['name']}")
            print(f"Страна:             {data['sys']['country']}")
            print(f"Погода:             {data['weather'][0]['description']}")
            print(f"Температура:        {data['main']['temp']} °C")
            print(f"Ощущается как:      {data['main']['feels_like']} °C")
            print(f"Влажность:          {data['main']['humidity']} %")
            print(f"Давление:           {data['main']['pressure']} hPa")
        elif response.status_code == 401:
            print("Ошибка 401: API-ключ неправильный или ещё не активирован.")
        else:
            print("Ошибка OpenWeatherMap:", response.status_code)
            print(response.text)

    except requests.RequestException as error:
        print("Ошибка соединения:", error)

    print()


def show_steam_news():
    print("=" * 55)
    print("ЗАДАНИЕ 2. ВАРИАНТ 6 — STEAM WEB API")
    print("=" * 55)

    url = "https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/"
    params = {
        "appid": 730,       # Counter-Strike 2
        "count": 1,
        "maxlength": 300,
        "format": "json"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            appnews = data["appnews"]
            news = appnews["newsitems"][0]

            news_date = datetime.fromtimestamp(
                news["date"]
            ).strftime("%d.%m.%Y %H:%M")

            print(f"AppID игры:         {appnews['appid']}")
            print(f"Название новости:   {news['title']}")
            print(f"Автор:              {news.get('author', 'Не указан')}")
            print(f"Источник:           {news.get('feedlabel', 'Не указан')}")
            print(f"Дата:               {news_date}")
            print(f"Внешняя новость:    {news.get('is_external_url', False)}")
            print(f"Ссылка:             {news['url']}")
        else:
            print("Ошибка Steam API:", response.status_code)
            print(response.text)

    except (requests.RequestException, KeyError, IndexError, ValueError) as error:
        print("Ошибка при работе со Steam API:", error)

    print()


def main():
    print("\nЛабораторная работа №7")
    print("Студент: Denis Novikov-Ahbabovic\n")
    show_weather()
    show_steam_news()
    print("Лабораторная работа завершена.")


if __name__ == "__main__":
    main()
