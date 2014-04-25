test:
	cd blog && python manage.py test

test_forever:
	cd blog && nosier -b .coverage python manage.py test
