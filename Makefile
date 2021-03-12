# SQUAD user to use.
SQUAD_USER = squad
SQUAD_PWD = squad

SQUAD_DOCKER_NAME = squad_web_1
SQUAD_TOKEN = ZTNiMGM0NDI5OGZjMWMxNDlhZmJmNGM4OTk2ZmI5MjQyN2FlNDFlNDY0OWI5MzRj

all: squad squad-setup

squad:
	docker-compose up -d

squad-setup:
	docker-compose exec $(SQUAD_DOCKER_NAME) \
		squad-admin users add \
			--passwd $(SQUAD_PWD) \
			--staff --superuser \
			$(SQUAD_USER)
	docker-compose exec $(SQUAD_DOCKER_NAME) \
		squad-admin users set-token \
			$(SQUAD_USER) \
			$(SQUAD_TOKEN)

clean:
	docker-compose down -v

.PHONY: all squad squad-setup clean
