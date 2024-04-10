## README для Клавиатурного Тренажёра

Клавиатурный тренажёр - это приложение, написанное на Python с использованием
библиотеки Tkinter, предназначенное для улучшения навыков печати 
пользователя. Оно предоставляет различные упражнения для печати, 
подсчитывает количество ошибок и измеряет скорость печати.

### Основные функции:

### Class `typing_trainer`
Класс, отвечающий за запуск программы

#### `__init__(self, root)` 
Конструктор класса `typing_trainer`. 

Инициализирует все дополнительные классы

#### `start_training`
Запуск тренировки


### Class `graphic_editor`

#### `__init__(self, root)`
Инициализирует главное окно приложения, вызывает методы настройки интерфейса и загрузки упражнений

#### `setup_ui(self)`
Настройка графического интерфейса пользователя. Создаёт элементы интерфейса, такие как метка для отображения текста упражнения и поле ввода для пользователя.

#### `load_exercises(self)`
Загружает упражнения из файла JSON. В случае отсутствия файла использует текст по умолчанию.

#### `display_current_exercise(self)`
Отображает текущее упражнение в графическом интерфейсе и очищает поле ввода.

#### `on_type(self, *args)`
Метод-обработчик, вызываемый каждый раз при изменении текста в поле ввода. Проверяет соответствие введённого текста текущему упражнению и подсчитывает ошибки. При успешном завершении упражнения вызывает метод `finish_exercise`.


### Class `statistics`

#### `__init__(self, root)`
Устанавливает начальные значения для времени начала упражнения и общего числа ошибок.

#### `start_exercise(self)`
Инициализирует таймер для измерения времени, начало подсчета количества ошибок.

#### `finish_exercise(self)`
Вызывается при успешном завершении упражнения. Останавливает таймер, рассчитывает скорость печати, отображает результаты и переключается на следующее упражнение.

### Class `text`

#### `read_files(self)`
Считывает файлы формата `.txt` из папки `texts`

#### `processing_file(self, file.txt)` 
Содержимое file.txt записывает в `exercises.json`

### Как использовать:

1. Установите Python и Tkinter на ваш компьютер.
2. Сохраните код в файл с расширением `.py`, например, `typing_trainer.py`.
3. Запустите скрипт из командной строки или терминала с помощью команды `python typing_trainer.py`.
4. Следуйте инструкциям на экране для выполнения упражнений по печати.

### Зависимости:
- Tkinter (библиотека встроена, но если выдается ошибка, то )
попробуйте переустановить библиотеку через ```sudo apt-get install python3-tk```