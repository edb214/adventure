# Adventure

By: EB TN CR EN


## Getting started

### Uninstall old Python (by default most of you will have an old Python 32 bit)

This is optional, but recommended so you're all on the same version of software

1. Start Control Panel
  - Start menu, type "control"
  - Select "Control Panel"
  - Select "Uninstall a program"

2. Remove Python
  - Select programs that look like "Python"
  - Select "Uninstall"
  - Repeat until all the Python things are gone


### Installing Python and PyGame

1. Install Python 3.7 64-bit
  - Download https://www.python.org/ftp/python/3.7.2/python-3.7.2-amd64.exe
  - Run the installer
  - Tick the "Add Python 3.7 to PATH" option, then "Install Now"
  - Accept all defaults

2. Install PyGame
  - Start menu, type `cmd`
  - Type `pip install -U pygame --user`
    - The `-U` means "upgrade any existing copy"
    - The `--user` means "just for my user", it's optional if you have administration rights on your computer
  - Wait for PyGame to install
  - Test it by typing `python -m pygame.examples.aliens`


### Getting a local clone of "Adventure"

1. Get a GitHub account
  - Go to https://github.com/
  - Follow the "sign up for GitHub" instructions
  - Make sure you record your username and password in a password manager
  - Choose a Free Account

2. EB has started a project for you already
  - https://github.com/edb214/adventure
  - You're looking at it!

3. Install GitHub Desktop
  - https://desktop.github.com
  - Click Download
  - Run the setup program
  - "Sign in to GitHub.com"

4. Clone the Adventure repository
  - Click "Clone a repository from the internet"
  - Select the "URL" tab
  - Type in "edb214/adventure"
  - Click "clone"

5. Click "Show in Explorer"... TADA!!


## How to make changes to the project

### Making a "commit" to the project, aka "push"

1. Before you can do this, EB needs to add you as a collaborator

2. Make sure all the files you want to push are saved

3. Push to GitHub
  - Open GitHub Desktop
  - Check Current respository is set to "adventure"
  - Select/unselect the files you would like to push
  - Click "Commit to master"
  - Click "Push to origin"

### Getting the latest code, aka "pull"
1.  Make sure all your files are saved

2. Pull from GitHub
  - Open GitHub Desktop
  - Check Current respository is set to "adventure"
  - Click "Fetch origin"
  - Click "Pull origin"
