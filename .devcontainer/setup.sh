#!/bin/bash

echo "🛠 Instalando dependências do sistema..."
apt-get update && apt-get install -y \
    cmake \
    libsm6 \
    libxext6 \
    libxrender-dev \
    build-essential \
    python3-dev \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

echo "🐍 Instalando dependências do Python..."
pip install --no-cache-dir --upgrade pip
pip install --no-cache-dir -r requirements.txt

echo "✅ Ambiente configurado!"
