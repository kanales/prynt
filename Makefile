.PHONY: sdist
sdist:
	python3 setup.py sdist

.PHONY: upload
upload: sdist
	twine upload dist/* --skip-existing