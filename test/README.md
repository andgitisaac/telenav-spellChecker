# telenav-spellChecker

A web server for local spell checker. 

## Environment Setup

Use venv to create and manage the project for each virtual environment you have.
`sudo apt install -y python3-venv`

Go to a folder of your choice and create the following folder:
`mkdir environments`

Run the command inside this folder to create our venv (remember to always give it a good name):
`python3 -m venv logrocket_env`

Make sure the enviornment is activated:
`source logrocket_env/bin/activate`

## APIs
For backend, run the Django application in order to test the endpoints:
`python manage.py runserver`

After you see the log showing our server is up and running, go to the browser and access http://localhost:8000/api/home/
For frontend, go to home-fe and run:
`npm start`

It will automatically open the browser in the http://localhost:3000/ url. 



