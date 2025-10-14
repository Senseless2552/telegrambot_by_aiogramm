FROM python:3.11

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем текущую директорию в контейнер
COPY . .

# Устанавливаем зависимости 
RUN pip install -r requirements.txt

# Запускаем скрипт
CMD ["python", "main.py"]