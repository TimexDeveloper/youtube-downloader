import yt_dlp
import os

def download_video():
    try:
        # Запрашиваем ссылку у пользователя
        video_url = input("Введите URL YouTube видео: ").strip()
        
        # Папка для сохранения (где лежит скрипт)
        output_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Настройки скачивания
        ydl_opts = {
            # Лучшее MP4-видео + M4A-аудио (или готовый MP4)
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            
            # Сохраняем рядом со скриптом
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
            
            # Если FFmpeg есть — объединит потоки в MP4
            'merge_output_format': 'mp4',
            
            # Убираем лишний вывод (можно заменить на False для подробного лога)
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            print(f"\n✅ Готово! Видео сохранено как:\n{os.path.join(output_dir, info['title']+'.mp4')}")

    except Exception as e:
        print(f"\n❌ Ошибка: {str(e)}")

if __name__ == "__main__":
    print("YouTube Video Downloader (MP4)")
    print("-----------------------------")
    download_video()
    input("\nНажмите Enter для выхода...")