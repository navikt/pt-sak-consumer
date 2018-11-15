NAME := navikt/pt-sak-consumer
bump:
	/bin/bash bump.sh

build:
	docker build --build-arg CLUSTER_ENV=preprod -t ${NAME}:$(shell /bin/cat ./version) -t ${NAME}:latest -t pt-sak-consumer .

push:
	docker push ${NAME}:$(shell /bin/cat ./version)

release: bump build push
