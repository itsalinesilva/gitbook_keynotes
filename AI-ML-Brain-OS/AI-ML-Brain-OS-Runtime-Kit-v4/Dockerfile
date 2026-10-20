FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY pyproject.toml README.md ./
COPY runtime ./runtime
RUN pip install --no-cache-dir .
USER 10001
CMD ["brain-os", "health", "--db", "/tmp/brain_os.sqlite3"]
