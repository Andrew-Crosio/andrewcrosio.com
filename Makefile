test:
	cd blog && python manage.py test --settings=blog.conf.test_settings

test_forever:
	cd blog && nosier -b .coverage 'python manage.py test --settings=blog.conf.test_settings'
