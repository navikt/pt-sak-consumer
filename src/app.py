import logging

from database import Database
from kafka import KafkaConsumer
from os import getenv
from prometheus_client import Counter, start_http_server

if __name__ == '__main__':
    start_http_server(8080)
    logging.basicConfig(
        format='{"timestamp": "%(asctime)s", "message": "%(name)s:%(message)s", "level": "%(levelname)s"}',
        level=logging.INFO,
        datefmt='%Y-%m-%dT%H:%M:%S%z')
    topics = getenv('TOPICS', 'test-producer-topic').split(',')
    consumer = KafkaConsumer(
        *topics,
        bootstrap_servers=getenv('BOOTSTRAP_SERVERS',
                                 'localhost:9092').split(','),
        security_protocol=getenv('SECURITY_PROTOCOL', 'PLAINTEXT'),
        sasl_mechanism=getenv('SASL_MECHANISM'),
        sasl_plain_username=getenv('SASL_USERNAME'),
        sasl_plain_password=getenv('SASL_PASSWORD'),
        ssl_cafile=getenv('SSL_CAFILE'),
        group_id=getenv('GROUP_ID'))

    database = Database(
        getenv('DB_URL',
               'postgresql+psycopg2://postgres:postgres@localhost:5433/kafka'))
    database.open()

    logging.info(f'Consuming messages from {topics}')
    c = Counter('messages', 'Meldinger lest')

    for message in consumer:
        logging.info(f'Reading message with offsett={message.offset} from partition={message.partition} from topic={message.topic}')
        database.store_message(message.topic, message.value)
        c.inc()
    database.close()
