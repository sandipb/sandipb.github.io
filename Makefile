.PHONY: serve deploy

serve:
	docker-compose up mkdocs

deploy:
	docker-compose up deploy
