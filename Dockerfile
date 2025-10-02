FROM python:3.10.15-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Dependências do sistema
RUN apt update && \
    apt install -y bash sed pkg-config gcc wkhtmltopdf && \
    rm -rf /var/lib/apt/lists/*

# Variáveis para MySQL (se usar mysqlclient)
ENV MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
ENV MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient"

# Copiar apenas requirements para aproveitar cache
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código Django
COPY app/ ./app/

EXPOSE 8000

# Rodar o Gunicorn
CMD ["gunicorn", "--log-file=-", "--bind", "0.0.0.0:8000", "projetocric.wsgi:application"]