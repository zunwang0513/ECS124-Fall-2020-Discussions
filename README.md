# Usage

This repository includes the Jupyter notebooks for discussion classes of ECS-124, Fall 2020 at UC Davis.

You can get the notebook for each session by pulling the repo just before the class begins.

These instructions will work only on Mac and Linux systems. If you're on Windows things will be very different. I suggest dual-booting a Linux along your Windows or using a virtual machine to get a Linux distribution such as Ubuntu working. Those on Windows 10 can use the Windows Subsystem for Linux (WSL) to get a working linux distribution with much less hassle. You can follow [these](https://docs.microsoft.com/en-us/windows/wsl/install-win10) instructions for getting WSL to work.

# Initial Setup

First clone this repository:

```
git clone https://github.com/Parsoa/ECS124-Fall-2020-Discussions
```

Navigate to the cloned directory:

```
cd ECS124-Fall-2020-Discussions
```

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

# Every Week

Before each class, you can get the latest notebook by pulling from the git repository. Navigate to where you cloned the repository and run:

```
git pull origin master
```

This will pull the latest changes. You'll then need to activate the virtualenv and run Jupyetr as above.

**DON'T MAKE** changes to files and folders inside the cloned repository, otherwise you may encounter *merge conflicts* when pulling (if you know how to handle them, then do as you please!).

To experiment and play with the code, copy the stuff you want to a directory outside of
