test:
	cd blog && rm -f .coverage && coverage run --source='.' manage.py test --settings=blog.conf.test_settings && coverage report

test_forever:
	nosier -p blog/blog/ -p blog/tests/ 'make test'

travisci: test
	mv blog/.coverage .

make htmlcov:
	cd blog && rm -f .coverage && coverage run --source='.' manage.py test --settings=blog.conf.test_settings && coverage report && coverage html
