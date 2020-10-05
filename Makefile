arch-install-reqs:
	yay -S google-chrome
	yay -S chromedriver

python-setup:
	python3 -m venv .venv

install-python-reqs:
	pip3 install -r requirements.txt

