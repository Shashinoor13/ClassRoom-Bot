.PHONY:start
start:
	@echo "Starting the application"
	pip3 install -r requirements.txt
	python3 app.py