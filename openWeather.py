import asyncio
import aiohttp


async def fetch_weather(session, city):
    api_key = '7a3d214b03ef4957fb61'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    async with session.get(url) as response:
        data = await response.json()
        return data


async def main():
    cities = ['Tashkent', 'Samara', 'Istanbul']  # Список городов для запроса
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_weather(session, city) for city in cities]
        results = await asyncio.gather(*tasks)
        for result, city in zip(results, cities):
            if 'weather' in result:
                description = result['weather'][0]['description']
                temperature = result['main']['temp']
                print(f"Weather in {city}: {description}, Temperature: {temperature}°C")
            else:
                print(f"No weather data available for {city}")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
