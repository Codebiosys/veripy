# Veri-Py

*Browser based Gherkin Testing Made Easy*

[![Build Status](https://travis-ci.com/Codebiosys/veri-py.svg?token=sqxCEuNQWHfr2F3qwRmC&branch=master)](https://travis-ci.com/Codebiosys/veri-py)
![Python Versions](https://img.shields.io/badge/Python-3.6-blue.svg)

## Installation

Installing Veri-Py is really simple but has a few more steps than most Python projects.

1. Clone this repo.
2. If you're using a Virtual Environment (which you should) then create it with a Python version of 3.6 or higher.
3. Install the requirements

```bash
# For production use, just install the normal requirements.txt.
pip install -r dev-requirements.txt
```

4. Set up your preferred browser driver (default is chrome). Use these instructions

```bash
# For macOS
brew cask install chromedriver

# For Linux
cd $HOME/Downloads
wget https://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip
unzip chromedriver_linux64.zip

mkdir -p $HOME/bin
mv chromedriver $HOME/bin
echo "export PATH=$PATH:$HOME/bin" >> $HOME/.bash_profile
```

For more information, refer to the [Splinter Installation Instructions](https://splinter.readthedocs.io/en/latest/drivers/chrome.html#setting-up-chrome-webdriver)


### Environment Variables

Behave is configured using environment variables. Please refer to the settings.py file for full documentation but the required variables are listed below. It is recommended that you create a file called `environment.sh` with the following contents and source that file before running Veri-Py.

```bash
cat > environment.sh << EOF
export ENVIRONMENT=dev
export PYTHONPATH=`pwd`/veripy:$PYTHONPATH
EOF

source environment.sh
```


## Running the Tests

Veri-Py is built on Behave. As such any files ending in `.feature` inside of the `features/` directory will be run when the application starts. Veri-Py comes with a sample set of tests demonstrating how to use the statements. To run these or any custom tests, use the following command:

```bash
behave veripy/features/
```


## Generating Documentation

VeriPy uses Sphinx for documentation. Once you've installed the dependencies, simply run the following command to generate the docs.

```bash
cd docs/
make html
```

You should now see a `_build` directory. Either open `index.html` in a browser or serve the directory directly using the following command.

```bash
cd _build/html
python -m http.server
```

You should now be able to navigate to [http://localhost:8000/](http://localhost:8000/) and see the documentation.
