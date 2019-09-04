# pt-sak-consumer

> pt-sak sin Python Kafka consumer

Denne Python-appen leser fra en eller flere topics, og lagrere de i en tabell i en database. Den støtter å lese fra flere topics, men skriver kun til en database.


## Bygging

Bygger automatisk i skyen (CircleCi) for hver push til master.

Trenger du å teste manuelt, kan du kjøre `make test-release`, som bygger, og laster opp et image til Docker hub.


## Testing

Vi har en egen katalog, og README for testing, sjekk ut [testing/README.md](testing/README.md).

Før du kan begynne å teste må du installere Python-pakken `psycopg2-binary`, som brukes for å kommunisere med Postgres-databasen.

```bash
pip install --user psycopg2-binary
```


## Gjennbruk

Du kan enkelt gjenbruke det vi har skrevet her, ved å lage en fork av repoet vårt, og følge punktene nedenfor:

* skriv om database-modellen i `database.py`
* endre `pt-sak` avhengigheter i `nais.yaml`
* legge til secrets i [Vault](https://github.com/nais/doc/blob/master/documentation/contracts/vault.md)
* lag din egen config i `config/`-katalogen
* bestille og konfigurere din egen Jenkins-server

Lykke til!
