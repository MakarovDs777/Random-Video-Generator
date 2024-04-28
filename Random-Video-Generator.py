import os
import numpy as np
import cv2

def generate_random_video(width, height):
    # Функция для генерации случайного видео с изменяющимися параметрами на каждой итерации
    
    # Начальные параметры
    hue = np.random.randint(0, 180)  # Основной цвет
    saturation = np.random.uniform(0.5, 1.0)  # Насыщенность цвета
    brightness = np.random.uniform(0.5, 1.0)  # Яркость
    frame_count = 0
    
    while True:
        # Генерация кадра
        frame = np.ones((height, width, 3), dtype=np.uint8) * 255  # Белый фон
        
        # Изменение параметров
        hue = (hue + 10) % 180  # Увеличиваем основной цвет на 10, ограничивая его до 180
        saturation = max(0.5, min(saturation + np.random.uniform(-0.1, 0.1), 1.0))  # Случайное изменение насыщенности
        brightness = max(0.5, min(brightness + np.random.uniform(-0.1, 0.1), 1.0))  # Случайное изменение яркости
        
        # Преобразование кадра в цветовое пространство HSV для изменения цвета
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame[:, :, 0] = hue  # Изменяем основной цвет
        frame[:, :, 1] = (frame[:, :, 1] * saturation).astype(np.uint8)  # Изменяем насыщенность
        frame[:, :, 2] = (frame[:, :, 2] * brightness).astype(np.uint8)  # Изменяем яркость
        
        # Преобразование обратно в цветовое пространство BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
        
        yield frame
        
        # Усложнение параметров на каждой итерации
        frame_count += 1
        if frame_count % 100 == 0:
            # Каждые 100 кадров увеличиваем амплитуду изменения параметров
            hue_change = np.random.randint(-30, 30)  # Изменение основного цвета
            saturation_change = np.random.uniform(-0.2, 0.2)  # Изменение насыщенности
            brightness_change = np.random.uniform(-0.2, 0.2)  # Изменение яркости

def save_video_to_desktop(frames_generator):
    # Создаем директорию "Videos" на рабочем столе, если ее еще нет
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    videos_folder = os.path.join(desktop_path, 'Videos')
    if not os.path.exists(videos_folder):
        os.makedirs(videos_folder)
    
    # Создаем имя файла для видео
    video_filename = "random_video.mp4"
    destination_path = os.path.join(videos_folder, video_filename)
    
    # Создаем объект VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(destination_path, fourcc, 30, (1280, 720))
    
    # Записываем видео сгенерированными кадрами
    for frame in frames_generator:
        out.write(frame)
    
    # Освобождаем объект VideoWriter и закрываем видеофайл
    out.release()
    
    print(f"Видео успешно сохранено на рабочий стол: {video_filename}")

if __name__ == "__main__":
    width = 1280  # Ширина видео
    height = 720  # Высота видео
    
    # Генерация видео на ходу
    frames_generator = generate_random_video(width, height)
    
    # Сохранение видео на рабочий стол
    save_video_to_desktop(frames_generator)
