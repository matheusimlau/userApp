SHELL := /bin/bash

docker-build:
	docker compose build

docker-clean:
	docker compose build --no-cache

docker-collect:
	docker compose run web python ./manage.py collectstatic --no-input

docker-migration:
	docker compose run web python ./manage.py makemigrations

docker-migrate:
	docker compose run web python ./manage.py migrate

docker-nuke:
	docker rmi -f $(docker images -aq) && docker rm -vf $(docker ps -aq)

docker-test:
	docker compose run web python ./manage.py test

docker-up:
	docker compose up