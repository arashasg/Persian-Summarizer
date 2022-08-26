# Django Web-Based Panel for Models

This project is a web application powered by django and python, its goal is to get text input from user and
process it with nlp models and store and show the result.

# Installation

This project can run with or without docker
## - Without Docker (recommended)
First clone the project then create a virtual environment with the command below:

windows:
```bash
python -m venv venv
```

mac or linux:
```bash
python3 -m venv venv
```

Activating the virtual environment:

windows:
```bash
.\venv\scripts\activate
```

mac or linux:
```bash
source venv/bin/activate
```

Install python packages from the `requirements.txt` file provided for the project.

windows:
```bash
pip install -r requirements.txt
```

mac or linux:
```bash
python3 -m pip install -r requirements.txt
```

Now, run the command below to create the database.
```bash
python manage.py migrate
```

Now, database is already created. Create a super user to use to login by the command below:
```bash
python manage.py createsuperuser
```
for example: `username: hadi | password: hadi | email: (empty)`

You can now run the project by running the command below:
```bash
python manage.py runserver
```

now you can access the project via address http://127.0.0.1:8000/ on your computer.


## - Using Docker
Install docker from [here](https://docs.docker.com/get-docker/), don't forget to signup in [docker hub](https://hub.docker.com/)
you will need it.
After docker is installed, clone this project into your computer and open the terminal in the project root directory and
type

```bash
docker login
```
the enter your credentials, after that enter the command bellow to download necessary files and run the project, this may
take a while.

```bash
docker-compose up --build
```
now you need to apply migrations to build database, oepn another terminal in ther same directory, (note: don't close
current terminal!) then enter the command bellow and wait for it

```bash
docker-compose exec web python manage.py migrate
```

congratulations!!
now you can access the project via address http://127.0.0.1:8000/ on your computer.

# sending commands to docker-compose sevices

you can send you commands for any service defined in docker-compose file like bellow. for example:

```bash
docker-compose exec <service name> <command>
```

Thanks.