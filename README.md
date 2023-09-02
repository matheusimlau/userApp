## This is my django user authentication and registration app. You can register a new user on a SQlite DB and perform authentication with your user or authenticate with google as you prefer.



## To run the application if you have docker installed simply run:

```bash
docker compose up --build
```

## pass the -d flag with you want to run in detached mode


## To run the application locally in case you dont have or don't want to use docker you can create a virtual environment

```bash
python3 -m venv myenv
```

## On Windows, run:

```bash
tutorial-env\Scripts\activate.bat && cd userManagerApp
```

## On Unix or MacOS, run:

```bash
source tutorial-env/bin/activate && cd userManagerApp
```
## Then download the dependencies to your environment

```bash
pip install -r requirements.txt
```

## After that you can start the server with the following command
```bash
python manage.py runserver
```