import aiohttp
import os
from typing import Optional, List, Any


async def get_it_news() -> Optional[List[Any]]:
    """
    Получает три свежие новости в области информационных технологий (IT) с помощью News API.
    :return: Список статей с новостями IT или None, если возникла ошибка при запросе.
    """
    api_key = os.getenv('NEWS_API_KEY')
    url = f'https://newsapi.org/v2/top-headlines?category=technology&apiKey={api_key}&pageSize=3&language=ru'

    async with aiohttp.ClientSession() as session:

        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()  # Получаем данные через await
                return data['articles']  # Возвращаем список статей
            else:
                return None
