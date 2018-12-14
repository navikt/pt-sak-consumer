NAME := navikt/pt-sak-consumer
DATE := $(shell date "+%Y-%m-%d")
SHA := $(shell git --no-pager log -1 --pretty=%h)
VERSION := ${DATE}-${SHA}
PREPROD_VERSION := $(shell openssl rand -base64 6)

build-preprod:
	docker build -t ${NAME}:${PREPROD_VERSION}-preprod -t ${NAME}:latest -t pt-sak-consumer --target=preprod .

push-preprod:
	docker push ${NAME}:${PREPROD_VERSION}-preprod

release-preprod: build-preprod push-preprod

build-prod:
	docker build -t ${NAME}:${VERSION}-1 -t ${NAME}:latest -t pt-sak-consumer --target=prod .

push-prod:
	docker push ${NAME}:${VERSION}-1

release-prod: build-prod push-prod
