# NimAI

NimAI is a web application that allows the user to challenge a reinforcement learning agent to a game of Nim. Before playing, the user can decide how much practice the AI is getting in order to learn a good policy.

A deployed version hosted on [Heroku](https://heroku.com/) can be found [here](https://nimai.herokuapp.com/). 

Click [here](https://towardsdatascience.com/who-learns-faster-you-or-my-ai-681e442416b0) for a high-level explanation of how the reinforcement learning part works.

## Getting started

### Prerequisites

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

## Architecture Overview

The main file controling the routing is `application.py`.

Some views are rendered server-side using HTML templates and sent to the client. However, for the game playing part, a dynamic AJAX infrastructure is used to manipulate the UI client-side based on the AI moves. 

These moves, in turn, are determined by calling Python functions (see `nimAI.py` and `nim_gameplay.py`) and passed to the client via JSON objects.

To keep track of session data, we use the `flask_session` package, which stores information like the session-level high score in a dictionary-like object.

Consider this general overview:

![](diagram.PNG?raw=true "Diagram")
## Built with

- Python 3.7.4
- Flask 1.1.2
- Werkzeug 1.0.1

## Authors

- Jakob Schmitt (Machine Learning, Backend, Frontend)
- Irina Bayova (Design, Styles, Frontend)

## Acknowledgements

Parts of the reinforcement learning code were taken from the great online course [CS50's Introduction to Artificial Intelligence](https://cs50.harvard.edu/ai/2020/), in particular from [unit 4 on learning](https://cs50.harvard.edu/ai/2020/weeks/4/).
