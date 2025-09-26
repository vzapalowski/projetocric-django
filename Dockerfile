RUN apt install -y git bash sed pkg-config gcc wkhtmltopdf

# Fast Fix Building MySQL
ENV MYSQLCLIENT_CFLAGS="-I/usr/include/mysql"
ENV MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmysqlclient"

# Clonar código atual do projeto (branch dev-2024)
RUN git clone https://github.com/vzapalowski/projetocric-django . --branch dev-2024

# Resolução temporária para erro de requirements.txt
#COPY ./fixed/ .

# Substituir projetocric/settings.py para produção (gambiarra temporária/permanente)
COPY . /buildfiles/
RUN rm -rf /rotacric/projetocric/settings.py
RUN cp /buildfiles/projetocric/settings.py /rotacric/projetocric/settings.py
#RUN echo $(cat /buildfiles/projetocric/settings.py) /rotacric/projetocric/settings.py

# Adaptar urls
RUN sed -i 's|http://127.0.0.1:8000|https://rota-cric.charqueadas.ifsul.edu.br|g' /rotacric/templates/static/js/helpers/urls.js
RUN sed -i 's|http://127.0.0.1:8000|https://rota-cric.charqueadas.ifsul.edu.br|g' /rotacric/templates/static/js/routes/map.js

# Instalar dependências do python
RUN pip install --no-cache-dir -r requirements.txt

# Instalar o Gunicorn
RUN pip install gunicorn

# Expor porta da aplicação
EXPOSE 8080

CMD [ "gunicorn", "--log-file=-", "--bind", "0.0.0.0:8000", "projetocric.wsgi:application" ]
Dockerfile (END)r urls
RUN sed -i 's|http://127.0.0.1:8000|https://rota-cric.charqueadas.ifsul.edu.br|g' /rotacric/templates/static/js/helpers/urls.js
RUN sed -i 's|http://127.0.0.1:8000|https://rota-cric.charqueadas.ifsul.edu.br|g' /rotacric/templates/static/js/routes/map.js

# Instalar dependências do python
RUN pip install --no-cache-dir -r requirements.txt

# Instalar o Gunicorn
RUN pip install gunicorn

# Expor porta da aplicação
EXPOSE 8080

CMD [ "gunicorn", "--log-file=-", "--bind", "0.0.0.0:8000", "projetocric.wsgi:application" ]