# NimAI

NimAI is a web application that allows the user to challenge a reinforcement learning agent to a game of Nim. Before playing, the user can decide how much practice the AI is getting in order to learn a good policy.

A deployed version can be found [here](https://nimai.herokuapp.com/).

## Getting started

### Prerequisits

There should be a recent [Python](https://www.python.org/downloads/) version (3.x) installed on your computer. 

Moreover, we recommend using a common web browser like Chrome or Firefox.

### Setting up an environment

First, navigate to the local directory you would like to place the project code in. Then, clone the NimAI repository.

```s
cd <PATH_TO_DIRECTORY>
git clone https://github.com/JokusPokus/Nim_AI.git
```

Create a virtual environment. The first command is only required if the virtualenv package is not yet installed on your machine.

```s
pip install virtualenv
virtualenv venv
```

Activate the virtual environment.

```s
source venv/bin/activate
```

Alternatively, you can use your preferred Python IDE and select the venv there. This project was created using [PyCharm](https://www.jetbrains.com/pycharm/).

Next, install all required packages.

```s
pip install -r requirements.txt
```

To run the application locally, you need to execute some commands based on the OS you are using.

Windows:

```s
set FLASK_APP=application.py
flask run
```

Linux / macOS:

```s
export FLASK_APP=application
flask run
```

## Built with

- Python 3.7.4
- Flask 1.1.2
- Werkzeug 1.0.1

## Authors

- Jakob Schmitt (Machine Learning, Backend, Frontend)
- Irina Bayova (Design, Styles, Frontend)