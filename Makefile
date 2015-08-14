SETTINGS=settings.local

migrate:
	python manage.py migrate --settings=$(SETTINGS)
run:
	python manage.py runserver --settings=$(SETTINGS)
rundebug:
	python -m pdb manage.py runserver --settings=$(SETTINGS)
freeze:
	python freeze > requirements.txt
