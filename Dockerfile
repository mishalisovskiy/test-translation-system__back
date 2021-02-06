FROM python:3.9
#RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -

RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get install -y poppler-utils && \
    apt-get install binutils libproj-dev gdal-bin -y && \
    apt-get install ffmpeg -y

COPY . /code

WORKDIR /code

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

RUN apt-get remove -y build-essential && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.cache

CMD ["./docker/start.sh"]

EXPOSE 8000