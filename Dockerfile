FROM python:3.10.15-bookworm

# Evita criação de arquivos .pyc e força output do Python no console
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diret�rio de trabalho dentro do container
WORKDIR /rotacric

# Instala dependências do sistema - CORRIGIDO
RUN apt update --allow-unauthenticated --allow-insecure-repositories && \
    apt install -y --allow-unauthenticated bash sed pkg-config gcc wkhtmltopdf && \
    rm -rf /var/lib/apt/lists/*

# Vari�veis para MySQL (mysqlclient)
ENV MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
ENV MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient"

# Copiar apenas requirements para aproveitar cache do Docker
COPY requirements.txt .

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar projeto completo
COPY . .

# Criar diretório para static coletado e midia
RUN mkdir -p staticfiles media

# Expor porta do Django
EXPOSE 8000

# Comando final: coleta static e inicia Gunicorn
CMD sh -c "python manage.py collectstatic --noinput && gunicorn projetocric.wsgi:application --bind 0.0.0.0:8000 && python manage.py makemigration && python manage.py migrate"