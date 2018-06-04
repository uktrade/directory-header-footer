build: test_requirements test

clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete

test_requirements:
	pip install -r requirements_test.txt

flake8:
	flake8 . --exclude=.venv,setup.py,directory_header_footer/version.py

pytest:
	pytest . --cov-config=.coveragerc --cov=. $(pytest_args)

CODECOV := \
	if [ "$$CODECOV_REPO_TOKEN" != "" ]; then \
	   codecov --token=$$CODECOV_REPO_TOKEN ;\
	fi

test: flake8 pytest
	$(CODECOV)

test_last_failed: test pytest_args='--last-failed'

compile_requirements:
	pip-compile requirements.in

upgrade_requirements:
	pip-compile --upgrade requirements.in

compile_test_requirements:
	pip-compile requirements_test.in

upgrade_test_requirements:
	pip-compile --upgrade requirements_test.in

compile_all_requirements: compile_requirements compile_test_requirements

upgrade_all_requirements: upgrade_requirements upgrade_test_requirements

header_footer:
	bash ./scripts/header_footer_git_make_branch.sh
	python ./scripts/upgrade_header_footer.py
	bash ./scripts/header_footer_git_push_changes.sh

.PHONY: build clean test_requirements flake8 pytest test
