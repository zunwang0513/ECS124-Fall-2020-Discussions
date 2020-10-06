# Usage

This repository includes the Jupyter notebooks for discussion classes of ECS-124, Fall 2020 at UC Davis.

You can get the notebook for each session by pulling the repo just before the class begins.

# Setup

Jupyter for running these, plus obviously Python3.

We'll set up everything inside a virtualenv for easier management of dependencies. First install virtualenv if you don't have it already:

```
pip3 install virtualenv
```

Clone this repository to some directory, say `ECS124` and navigate to it. Then create a virtualenv:

```
virtualenv -p python3 venv
```

Activate the virtualenv:

```
source venv/bin/activate
```

Once activated, install the needed libraries:

```
pip install -r requirements.txt
```

Now you're good to go. Start Jupyter (it was installed during the previous step):

```
jupyter notebook
```

It will open a web browser page. Navigate to the folder for the current class and run the corresponding notebook.
