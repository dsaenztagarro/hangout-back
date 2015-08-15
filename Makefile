PY=python2
SETTINGS=settings.local

migrate:
	$(PY) manage.py migrate --settings=$(SETTINGS)
run:
	$(PY) manage.py runserver --settings=$(SETTINGS)
rundebug:
	$(PY) -m pdb manage.py runserver --settings=$(SETTINGS)
freeze:
	$(PY) freeze > requirements.txt
