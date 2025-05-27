import asyncio
import edge_tts
import os

# Загрузка текста из файла
with open("wake_surf_camp.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Выбор голоса (мужской, хриплый)
voice = "ru-RU-DmitryNeural"

async def main():
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("wake_surf_camp.mp3")
    print("✔ Озвучка завершена: wake_surf_camp.mp3")
    os.startfile("wake_surf_camp.mp3")  # Только Windows

asyncio.run(main())
