FROM navikt/oracle18-3-python36:0.0.1
ARG CLUSTER_ENV

ENV TZ="Europe/Oslo"

WORKDIR /root

RUN pip3.6 install --upgrade  pip

ADD requirements.txt .
RUN pip3.6 install -r requirements.txt

ADD config/${CLUSTER_ENV}.env .env
ADD start.sh .

ADD src/ /root/

ENTRYPOINT ["/root/start.sh"]
