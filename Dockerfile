FROM python:3.9

COPY ./requirements.txt /src/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

COPY . /src


EXPOSE 6060

WORKDIR src

CMD ["python3", "-u", "manage.py", "--host", "0.0.0.0", "--port", "6060"]