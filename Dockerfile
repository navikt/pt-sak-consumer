FROM navikt/oracle18-3-python36:1.0.0 AS common

ENV SECURITY_PROTOCOL=SASL_SSL
ENV SASL_MECHANISM=PLAIN
ENV GROUP_ID=pt-sak-consumer

WORKDIR /root

RUN pip3.6 install --upgrade  pip

ADD requirements.txt .
RUN pip3.6 install -r requirements.txt

ADD src/ /root/
ADD start.sh .

ENTRYPOINT ["/root/start.sh"]


FROM common AS preprod
ENV TOPICS=aapen-oppgave-opprettet-v1-preprod,aapen-oppgave-endret-v1-preprod
ENV BOOTSTRAP_SERVERS=b27apvl00045.preprod.local:8443,b27apvl00046.preprod.local:8443,b27apvl00047.preprod.local:8443


FROM common AS prod
ENV TOPICS=aapen-oppgave-opprettet-v1-prod,aapen-oppgave-endret-v1-prod
ENV BOOTSTRAP_SERVERS=a01apvl00145.adeo.no:8443,a01apvl00146.adeo.no:8443,a01apvl00147.adeo.no:8443,a01apvl00148.adeo.no:8443,a01apvl00149.adeo.no:8443,a01apvl00150.adeo.no:8443
