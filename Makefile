NAME := navikt/pt-sak-consumer
VERSION := $(shell openssl rand -base64 6)

test-build:
	docker build -t ${NAME}:${VERSION}-preprod -t ${NAME}:latest -t pt-sak-consumer .

push-preprod:
	docker push ${NAME}:${VERSION}-preprod

test-release: test-build test-push
