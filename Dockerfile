FROM 907457203140.dkr.ecr.us-west-2.amazonaws.com/python:latest
MAINTAINER Sun <wenhaijie@light2cloud.com>

WORKDIR /opt/l2cim
RUN useradd l2cim

COPY . /opt/l2cim

RUN cd /opt/l2cim/requirements && yum -y install $(cat rpm_requirements.txt)

RUN cd /opt/l2cim/requirements && pip3 --default-timeout=1000 install --upgrade pip setuptools \
    && pip3 install -r requirements.txt \
    || pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt

# 安装gunicorn
RUN pip3 install gunicorn || pip3 install -i https://mirrors.aliyun.com/pypi/simple/ gunicorn
RUN ln -s /usr/local/python3/bin/gunicorn /usr/bin/gunicorn
RUN ln -s /usr/local/python3/bin/celery /usr/bin/celery

VOLUME /opt/l2cim/data
VOLUME /opt/l2cim/logs

EXPOSE 80
EXPOSE 8080
ENTRYPOINT ["./entrypoint.sh"]