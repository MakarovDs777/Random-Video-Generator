import numpy as np
import cv2

def generate_random_video(width, height):

    # Функция для генерации случайного видео с изменяющимися параметрами на каждой итераций
    # Начальные параметры
    colors = np.random.randint(0, 256, (height, width, 3)) # Радуга цветов
    frame_count = 0

    while True:

        # Генерация кадра
        frame = np.ones((height, width, 3), dtype=np.uint8) * 255 # Белый фон

        # Изменение параметров
        colors = np.random.permutation(colors) # Перемешиваем цвета

        # Рисуем случайные пиксели с радуги цветов
        for i in range(height):
            for j in range(width):
                frame[i][j] = colors[i][j]

        yield frame

        # Усложнение параметров на каждой итерации
        frame_count += 1
        if frame_count % 100 == 0:
            # Каждые 100 кадров увеличиваем амплитуду изменения параметров
            pass

if __name__ == "__main__":
    width = 1280 # Ширина видео
    height = 720 # Высота видео

    # Генерация видео на ходу
    frames_generator = generate_random_video(width, height)

    # Отображение видео в отдельном окне
    for frame in frames_generator:
        cv2.imshow("Random Video", frame)
        if cv2.waitKey(25) & 0xFF == ord('q'): # Нажмите 'q', чтобы выйти из цикла
            break

    cv2.destroyAllWindows()
