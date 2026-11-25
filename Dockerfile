FROM python:3.12-alpine
WORKDIR /app
COPY app/ .
COPY scripts/ ./scripts/
EXPOSE 5000
CMD ["python", "app.py"]
