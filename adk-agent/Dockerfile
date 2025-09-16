# adk-agent/Dockerfile
# FROM python:3.11-slim

# WORKDIR /app

# # Install system deps
# RUN apt-get update && apt-get install -y gcc

# # Copy requirements
# COPY ./adk-agent/requirements.txt .

# # Install Python deps
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy code
# COPY . ./adk-agent/app
# # Expose port
# EXPOSE 8000

# # Run agent
# CMD ["uvicorn", "adk-agent.main:app", "--host", "0.0.0.0", "--port", "8000"]



# FROM python:3.11-slim
# # Set working directory inside container
# WORKDIR /app
# # Install system dependencies
# RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*
# # Copy only requirements first (for caching)
# COPY requirements.txt .
# # Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt
# # Copy the rest of the code (everything in adk-agent)
# COPY . .
# # Expose port
# EXPOSE 8000
# # Run app with uvicorn
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


FROM python:3.11-slim
# Set base workdir
WORKDIR /app
# Install system deps
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*
# Copy requirements first for caching
COPY ./adk-agent/requirements.txt .
# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt
# Copy everything
COPY ./adk-agent /app
# Change workdir to where agents live
WORKDIR /app
EXPOSE 8000
# Start ADK web server
CMD ["adk", "web", "--host", "0.0.0.0", "--port", "8000"]
