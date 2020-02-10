## Starting up application instructions
# Requirements 
* Must have python3 installed.

## Instructions
* Instructions can be found at https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/requirements.html#create-a-project-directory-structure
* (After Installing Python3)
* 1. In the terminal fun the command `cd ~`
* 2. Run the command `git clone https://github.com/alexbaranov43/single-file-python-app.git`
* 3. Run the command `cd single-file-python-app`
* 4. For mac users run the command `export VENV=~/single-file-python-app/env
** For pc users `set VENV=c:\single-file-python-app\env`
* 5. For mac users run `python3 -m venv $VENV` and pc run `python -m venv %VENV%`
* 6. Update packaging tools in the virtual environment¶
* It's always a good idea to update to the very latest version of packaging tools because the installed Python bundles only the version that was available   * at the time of its release.

# macOS and Linux
** $VENV/bin/pip install --upgrade pip setuptools
# Windows
** %VENV%\Scripts\pip install --upgrade pip setuptools

* 7. Run the command `cd files`
* 8. Run the command $VENV/bin/python app.py and open up http://localhost:6543/ in your browser
