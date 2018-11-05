import logging
import os

from database import Database
from kafka import KafkaConsumer
from prometheus_client import Counter, start_http_server


if __name__ == '__main__':
    start_http_server(8080)
    logging.basicConfig(level=logging.INFO)
    topic = 'aapen-oppgave-opprettet-v1-preprod'
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=['b27apvl00045.preprod.local:8443',
                           'b27apvl00046.preprod.local:8443',
                           'b27apvl00047.preprod.local:8443'],
        security_protocol='SASL_SSL',
        sasl_mechanism='PLAIN',
        sasl_plain_username=os.environ['SASL_USERNAME'],
        sasl_plain_password=os.environ['SASL_PASSWORD'],
        ssl_cafile='/var/run/secrets/nais.io/vault/kafka.pem',
        group_id='pt-sak-consumer')

    database = Database(os.environ['DB_URL'])
    database.open()
    logging.info(f'Consuming messages from {topic}')
    c = Counter('messages', 'Meldinger lest')

    for message in consumer:
        logging.info(f'Reading message with offsett={message.offset}')
        database.store_message(message.value)
        c.inc()
    database.close()
