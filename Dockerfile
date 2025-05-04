FROM python:3.10-slim

# Avoid Python writing .pyc files and ensure output is shown immediately
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Copy local wheels and requirements
COPY wheels/ ./wheels/
COPY requirements.txt .

# Install only from local wheels (offline CPU-only build)
RUN pip install --no-index --find-links=./wheels -r requirements.txt

# Copy the rest of your source code
COPY . .

# Expose gRPC port
EXPOSE 50051

# Run gRPC server
CMD ["python", "-m", "app.grpc_server"]
