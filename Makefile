test:
	pytest --cov-report term-missing --cov-report html --cov-branch --cov bitchat/

lint:
	@echo
	isort --diff -c .
	@echo
	flake8 .
	@echo
	mypy -p bitchat
	@echo
	mypy -p tests
	@echo
	bandit -r bitchat/
	@echo
	pip-audit --ignore-vuln GHSA-hcpj-qp55-gfph

format:
	isort .
	blue .
	pyupgrade --py310-plus **/*.py

install_hooks:
	bash scripts/install_hooks.sh