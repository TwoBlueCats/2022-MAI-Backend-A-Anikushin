lab1-test:
	pytest -v utils/test_lru_cache.py

reload-nginx:
	sudo service nginx reload

start-app:
	uvicorn main:app