all: squad

squad:
	docker-compose up -d

clean:
	docker-compose down

.PHONY: all squad clean
