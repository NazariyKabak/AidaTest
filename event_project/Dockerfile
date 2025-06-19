# Базовий образ
FROM python:3.11-slim

# Робоча директорія в контейнері
WORKDIR /app

# Копіюємо залежності
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копіюємо решту коду проєкту
COPY . .

# Команди за замовчуванням
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
