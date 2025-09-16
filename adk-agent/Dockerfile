# adk-agent/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y gcc

# Copy requirements
COPY ./adk-agent/requirements.txt .

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Expose port
EXPOSE 8000

# Run agent
CMD ["uvicorn", "adk-agent.main:app", "--host", "0.0.0.0", "--port", "8000"]