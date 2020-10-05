arch-install-reqs:
	yay -S google-chrome
	yay -S chromedriver

mac-install-reqs:
	brew cask install google-chrome
	brew cask install chromedriver
	# will probably need to allow chromedriver to run in the mac security settings

python-setup:
	python3 -m venv .venv

install-python-reqs:
	pip3 install -r requirements.txt

