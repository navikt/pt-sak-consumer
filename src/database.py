from sqlalchemy import create_engine, CLOB, Column, Date, FetchedValue, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Oppgave(Base):
    __tablename__ = 'oppgave_json_dump'
    __table_args__ = {'schema': 'fk_p'}

    transId = Column('trans_id',
                     String(40),
                     primary_key=True,
                     server_default=FetchedValue())
    data = Column('data',
                  CLOB,
                  nullable=False)
    lastetDato = Column('lastet_dato',
                        Date(),
                        nullable=False,
                        server_default=FetchedValue())
    overfortStatus = Column('overfort_status',
                            String(20))


class Database():
    def __init__(self, url):
        self.engine = create_engine(url)
        self.sessionmaker = sessionmaker()
        self.sessionmaker.configure(bind=self.engine)

    def open(self):
        self.session = self.sessionmaker()

    def close(self):
        if self.session:
            self.session.close()

    def store_message(self, message):
        oppgave = Oppgave(data=message)
        self.session.add(oppgave)
        self.session.commit()