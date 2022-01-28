.PHONY: init

init:
	make down
	make up
	make ps
	make fixtures
down:
	docker-compose down --volumes --remove-orphans
pull:
	docker-compose pull
build:
	docker-compose build
up:
	make pull
	make build
	docker-compose up -d
ps:
	docker-compose ps
migrations:
	python app.py makemigrations
migrate:
	make migrations
	python app.py migrate
fixtures:
	make migrate
	python app.py loaddata films people planets species starships transports vehicles
su:
	python manage.py createsuperuser
test:
	python app.py test
remove_files:
	rm -rf core/media/*
collecstatic:
	python app.py collectstatic --noinput
shell:
	python app.py shell
reset_db:
	python app.py reset_db --noinput --close-sessions
pipenv.lock:
	pipenv lock
pipenv:
	# pipenv install --system --deploy
	pipenv install
pipenv.dev:
	make pipenv
	# pipenv install --system --deploy --dev
	pipenv install --dev
serve:
	python app.py runserver 0:8000
venv:
	python3.8 -m venv env
