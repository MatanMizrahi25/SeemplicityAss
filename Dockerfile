
FROM python:3.12-slim


WORKDIR /app


COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
