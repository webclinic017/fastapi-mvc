POETRY_HOME ?= ${HOME}/.local/share/pypoetry
POETRY_BINARY ?= ${POETRY_HOME}/venv/bin/poetry
POETRY_VERSION ?= 1.2.0

.PHONY: build
build: ## Build fastapi-mvc package
	echo "[build] Build fastapi-mvc package."
	${POETRY_BINARY} build

.PHONY: install
install: ## Install fastapi-mvc with poetry
	@build/install.sh

.PHONY: image
image: ## Build fastapi-mvc image
	@build/image.sh

.PHONY: clean-image
clean-image: ## Clean fastapi-mvc image
	@build/clean-image.sh

.PHONY: metrics
metrics: install ## Run fastapi-mvc metrics checks
	echo "[metrics] Run fastapi-mvc PEP 8 checks."
	${POETRY_BINARY} run flake8 --select=E,W,I --max-line-length 80 --import-order-style pep8 --extend-exclude=fastapi_mvc/generators/**/template --statistics --count fastapi_mvc
	echo "[metrics] Run fastapi-mvc PEP 257 checks."
	${POETRY_BINARY} run flake8 --select=D --ignore D301 --extend-exclude=fastapi_mvc/generators/**/template --statistics --count fastapi_mvc
	echo "[metrics] Run fastapi-mvc pyflakes checks."
	${POETRY_BINARY} run flake8 --select=F --extend-exclude=fastapi_mvc/generators/**/template --statistics --count fastapi_mvc
	echo "[metrics] Run fastapi-mvc code complexity checks."
	${POETRY_BINARY} run flake8 --select=C901 --extend-exclude=fastapi_mvc/generators/**/template --statistics --count fastapi_mvc
	echo "[metrics] Run fastapi-mvc open TODO checks."
	${POETRY_BINARY} run flake8 --select=T --extend-exclude=fastapi_mvc/generators/**/template --statistics --count fastapi_mvc tests
	echo "[metrics] Run fastapi-mvc black checks."
	${POETRY_BINARY} run black -l 80 --exclude "fastapi_mvc/generators/.*/template" --check fastapi_mvc

.PHONY: unit-test
unit-test: install ## Run fastapi-mvc unit tests
	echo "[unit-test] Run fastapi-mvc unit tests."
	${POETRY_BINARY} run pytest tests/unit

.PHONY: integration-test
integration-test: install ## Run fastapi-mvc integration tests
	echo "[unit-test] Run fastapi-mvc integration tests."
	${POETRY_BINARY} run pytest tests/integration

.PHONY: test
test: unit-test integration-test ## Run fastapi-mvc tests

.PHONY: docs
docs: install ## Build fastapi-mvc documentation
	echo "[docs] Build fastapi-mvc documentation."
	${POETRY_BINARY} run sphinx-build docs site
