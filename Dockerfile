FROM python:3.10.15-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /rotacric

# Dependências do sistema
RUN apt update && \
    apt install -y bash sed pkg-config gcc wkhtmltopdf

# Fast fix para MySQL
ENV MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
ENV MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient"

# Copiar apenas o necessário
COPY requirements.txt /rotacric/
COPY app/ /rotacric/app/

# Ajustar URLs JS se necessário (opcional)
RUN sed -i 's|http://127.0.0.1:8000|https://rota-cric.charqueadas.ifsul.edu.br|g' /rotacric/templates/static/js/helpers/urls.js && \
    sed -i 's|http://127.0.0.1:8000|https://rota-cric.charqueadas.ifsul.edu.br|g' /rotacric/templates/static/js/routes/map.js

# Instalar dependências Python
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

EXPOSE 8080

CMD ["gunicorn", "--log-file=-", "--bind", "0.0.0.0:8000", "projetocric.wsgi:application"]