# AsrIran web crawler project

This project crawls Asre-Iran website and extracts news and write them to a csv file.

# Installation

This project is written with python programming language and scrapy crawling framework so you need to install python in your computer,
You can access python official website for downloading python via [this link](https://www.python.org/).

After installing python, clone this project into your computer and open a terminal in project root directory. Now you need to create
and activate a python virtual environment, to do that follow the instruction bellow:

1- creating the virtual environment

windows:

```bash
python -m venv venv
```
mac or linux:

```bash
python3 -m venv venv
```

2- activating the virtual environment

windows:

```bash
.\venv\scripts\activate
```

mac or linux:

```bash
source venv/bin/activate
```
Now that you have an active virtual environment it is time to install project requirements, for that enter the command bellow:

windows:
```bash
pip install -r requirements.txt
```

mac or linux:
```bash
python3 -m pip install -r requirements.txt
```
now please wait for project dependencies to download this may take a few minutes, after that you can command the crawler to start crawling by simply typing
this command in the terminal:

```bash
scrapy crawl AsrIran
```

And it starts crawling :)

