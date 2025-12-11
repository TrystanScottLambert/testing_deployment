cd
curl -O https://www.python.org/ftp/python/3.12.8/python-3.12.8-macos11.pkg
sudo installer -pkg python-3.12.8-macos11.pkg -target

cd /path/to/rip-validator

# Create new venv with universal Python
/Library/Frameworks/Python.framework/Versions/3.12/bin/python3 -m venv .venv-universal

# Activate it
source .venv-universal/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install pyinstaller
