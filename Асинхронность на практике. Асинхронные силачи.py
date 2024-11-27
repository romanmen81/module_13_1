import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(1, 6):
        await asyncio.sleep(1 / power)  # Задержка обратно пропорциональна power
        print(f"Силач {name} поднял {i} шар")
    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    # Определяем участников с их мощностями
    participants = [("Pasha", 3), ("Denis", 4), ("Apollon", 5)]
    tasks = []
    for name, power in participants:
        tasks.append(start_strongman(name, power))

    # Ожидание завершения всех задач
    await asyncio.gather(*tasks)

# Запуск асинхронной функции
if __name__ == "__main__":
    asyncio.run(start_tournament())