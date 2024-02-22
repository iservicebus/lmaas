FROM python:3.10.7-slim

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    libopenblas-dev \
    libx11-dev \
    python3-dev \
    python3-pip \
    wget




# Copy your project or code files
COPY . .

RUN pip install --user  .

# Entry point (can be customized)
CMD ["python3", "./src/lmaas_server.py"]
