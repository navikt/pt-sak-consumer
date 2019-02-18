import logging

from database import Database
from kafka import KafkaConsumer
from os import getenv
from prometheus_client import Counter, start_http_server
from pythonjsonlogger import jsonlogger


if __name__ == '__main__':
    logger = logging.getLogger()
    logHandler = logging.StreamHandler()
    format_str = '%(message)%(levelname)%(name)%(asctime)'
    formatter = jsonlogger.JsonFormatter(format_str)
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)

    start_http_server(8080)

    topics = getenv('TOPICS', 'test-producer-topic').split(',')
    try:
        consumer = KafkaConsumer(
            *topics,
            bootstrap_servers=getenv('BOOTSTRAP_SERVERS',
                                     'localhost:9092').split(','),
            security_protocol=getenv('SECURITY_PROTOCOL', 'PLAINTEXT'),
            sasl_mechanism=getenv('SASL_MECHANISM'),
            sasl_plain_username=getenv('SASL_USERNAME'),
            sasl_plain_password=getenv('SASL_PASSWORD'),
            ssl_cafile='/etc/pki/tls/cacert.pem',
            group_id=getenv('GROUP_ID'))
    except Exception as e:
        logging.exception(e)
        logging.shutdown()
        exit(1)

    db_url = getenv('DB_URL',
                    'postgresql+psycopg2://postgres:postgres@localhost:5433/kafka')
    database = Database(db_url)
    database.open()

    logging.info(f'Consuming messages from {topics}')
    message_read = Counter('ptsak_messages_read', 'Meldinger lest')
    storing_failed = Counter('ptsak_storage_failed',
                             'Meldinger som har feilet under lagring')
    message_failed = Counter('ptsak_messages_failed',
                             'Meldinger som har feilet under lesing')

    try:
        for message in consumer:
            logging.info(f'Reading message with offsett={message.offset} from partition={message.partition} from topic={message.topic}')
            try:
                database.store_message(message.topic, message.value)
                message_read.inc()
            except Exception as e:
                logging.exception(e)
                storing_failed.inc()
            database.close()
    except Exception as e:
        logging.exception(e)
        logging.shutdown()
        exit(1)
