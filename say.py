import asyncio
import edge_tts
import os

async def main():
    print("Введите текст (Enter дважды — закончить):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    # Вставляем паузы — многоточия
    joined_text = "... ".join(lines)

    # Выбор голоса
    print("Выберите голос: [1] Светлана (женский), [2] Дмитрий (мужской): ", end="")
    choice = input().strip()
    voice = "ru-RU-SvetlanaNeural" if choice != "2" else "ru-RU-DmitryNeural"

    # Генерация речи
    communicate = edge_tts.Communicate(joined_text, voice)
    await communicate.save("output.mp3")
    print("✔ Аудиофайл сохранён: output.mp3")

    # Воспроизведение
    os.startfile("output.mp3")

asyncio.run(main())
