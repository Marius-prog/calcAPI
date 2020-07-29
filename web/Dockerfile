FROM python:3
WORKDIR /Users/Mariusmac/Documents/calcAPI
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "api.py"]