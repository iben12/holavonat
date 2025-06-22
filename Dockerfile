FROM python:3.11-slim
WORKDIR /app
COPY ./proxy/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "mav:app"]
