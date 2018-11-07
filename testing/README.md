Hvordan teste
=============

Vi bruker `docker-compose` for å sette opp et Kafka Cluster og Postgres for å teste konsumering av meldinger.

Før du kan begynne å teste må du installere Python-pakken `psycopg2-binary`, som brukes for å kommunisere med Postgres-databasen.

```bash
pip install --user psycopg2-binary
```

Det er tre kommandoer du må kjøre for å få alt satt opp:

1. `docker-compose up -d`
   * Setter opp selve Kafka clusteret med Postgres
2. `./init_postgres`
   * Lager DB-schema, tabell, og UUID-trigger (tabellen må matche hva vi har i `database.py`)
3. `./create_topic`
   * Lager topic'en `test-producer-topic`

Nå dette er gjort, kan du starte Python-consumeren med `python app.py`.

For å `produce` meldinger på Kafka kan du kjøre scriptet `./start_produce`, hvor hver linje regnes som en ny melding.

```bash
$ ./start_producing
> hello world
>
```

PS: Husk å vent med å sende meldinger til du ser `>`.


## Nullstille test-miljøet

Gjøres enkelt ved å kjøre `docker-compose down`. Da blir hele clusteret tatt ned, og dataen slettet.
