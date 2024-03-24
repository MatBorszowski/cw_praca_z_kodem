requirements:
	pip install -r requirements.txt
run:
	python -m flask run
test:
	pylint app.py
