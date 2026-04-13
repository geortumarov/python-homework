# Проект автоматизации тестирования

Проект содержит автоматизированные тесты для:
- Калькулятора с задержкой (slow-calculator)
- Интернет-магазина SauceDemo

## Технологии
- Python 3.14.0
- Selenium WebDriver
- Pytest
- Allure Framework
- WebDriver Manager

## Установка
1. Клонировать репозиторий:
```bash
git clone <url-репозитория>
cd <имя-папки>
```

2. Установка зависимостей:
```bash
pip install -r requirements.txt
```

## Структура проекта
```
├── pages/                 # Page Object классы
│   ├── calculator_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/                 # Тесты
│   ├── test_calculator.py
│   └── test_shop.py
├── results/               # Результаты тестов (Allure)
├── final-report/          # Сгенерированный отчёт
├── requirements.txt       # Зависимости
└── README.md             # Документация
```

## Предварительные требования
Убедитесь, что установлен Allure Commandline:
```bash
# Проверка установки
allure --version
```

Если не установлен:
```bash
# Для Windows (через scoop):
scoop install allure

# Для macOS:
brew install allure

# Для Linux:
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```

## Запуск тестов

### Очистка старых результатов и запуск всех тестов:

**Windows (командная строка):**
```bash
rmdir /s /q results 2>nul
rmdir /s /q final-report 2>nul
pytest tests/ --alluredir=results
allure generate results -o final-report --clean
```

**Windows (PowerShell):**
```powershell
Remove-Item -Recurse -Force results -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force final-report -ErrorAction SilentlyContinue
pytest tests/ --alluredir=results
allure generate results -o final-report --clean
```

**Linux/Mac:**
```bash
rm -rf results final-report
pytest tests/ --alluredir=results
allure generate results -o final-report --clean
```

### Запуск конкретного теста:
```bash
# Тест калькулятора
pytest tests/test_calculator.py --alluredir=results

# Тест магазина
pytest tests/test_shop.py --alluredir=results
```

### Использование bat-файла (только Windows)
Если в проекте есть файл run_tests.bat:
```bash
run_tests.bat
```

## Просмотр отчёта

### Способ 1: Открыть сгенерированный отчёт в браузере
```bash
# Windows
start final-report/index.html

# macOS
open final-report/index.html

# Linux
xdg-open final-report/index.html
```

### Способ 2: Запустить Allure сервер (рекомендуется)
```bash
# Из папки с результатами
allure serve results

# Или открыть уже сгенерированный отчёт
allure open final-report
```

## Описание тестов

### Тест 1: Медленный калькулятор (test_calculator.py)
Проверяет работу калькулятора с искусственной задержкой:
- Открытие страницы калькулятора
- Установка задержки 45 секунд
- Выполнение операции: 7 + 8
- Ожидание результата 15
- Проверка соответствия результата

### Тест 2: Оформление заказа в магазине (test_shop.py)
Проверяет итоговую сумму заказа:
- Авторизация в магазине (standard_user)
- Добавление трёх товаров в корзину
- Переход в корзину
- Заполнение формы оплаты
- Проверка итоговой суммы: $58.29

## Особенности реализации
- **Page Object Model**: каждый класс страницы инкапсулирует логику работы с конкретной страницей
- **Allure-отчёты**: каждый шаг теста задокументирован и отображается в отчёте
- **WebDriver Manager**: автоматически скачивает и настраивает драйверы браузеров
- **Кросбраузерность**: тесты используют Chrome и Firefox

## Зависимости (requirements.txt)
Создайте файл requirements.txt с содержимым:
```txt
pytest==7.4.0
selenium==4.11.2
webdriver-manager==4.0.1
allure-pytest==2.13.2
```

## .gitignore (что не пушить в репозиторий)
Создайте файл .gitignore с содержимым:
```text
# Виртуальное окружение
venv/
env/
ENV/

# Результаты тестов и отчёты
results/
final-report/
allure-results/
allure-report/

# Файлы IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Логи и временные файлы
*.log
*.pyc
__pycache__/
.pytest_cache/
```

## Troubleshooting

**Проблема: "allure: command not found"**
Решение: Установите Allure Commandline (см. раздел "Предварительные требования")

**Проблема: "ModuleNotFoundError"**
Решение: Проверьте, что виртуальное окружение активировано и зависимости установлены:
```bash
pip list
```

**Проблема: Тесты падают с ошибками драйвера**
Решение: Обновите webdriver-manager:
```bash
pip install --upgrade webdriver-manager
```

**Проблема: Русские символы в консоли Windows**
Решение: Используйте bat-файл или установите кодировку:
```bash
chcp 65001
```

## Контакты
По вопросам и предложениям обращайтесь к автору проекта.

**Примечание:** Папки results/ и final-report/ не включаются в репозиторий. Все результаты тестов и отчёты генерируются локально.