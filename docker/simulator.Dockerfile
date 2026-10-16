FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src

RUN pip install --no-cache-dir .

# Replace this command when the sensor simulator is implemented.
CMD ["python", "-c", "print('sensor simulator scaffold')"]

