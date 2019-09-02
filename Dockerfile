FROM navikt/oracle18-3-python36:1.0.0

ENV SECURITY_PROTOCOL=SASL_SSL
ENV SASL_MECHANISM=PLAIN
ENV GROUP_ID=ptsak070119

WORKDIR /root

RUN pip3.6 install --upgrade pip

COPY requirements.txt .
RUN pip3.6 install -r requirements.txt

COPY src/ /root/
COPY start.sh .

ENTRYPOINT ["/root/start.sh"]
