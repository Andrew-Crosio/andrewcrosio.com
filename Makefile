test:
	cd blog && python manage.py test --settings=blog.conf.test_settings

test_forever:
	cd blog && nosier -b .coverage -b cover 'python manage.py test --settings=blog.conf.test_settings'

travisci: test
	mv blog/.coverage .

make htmlcov:
	cd blog && python manage.py test --settings=blog.conf.test_settings --cover-html
