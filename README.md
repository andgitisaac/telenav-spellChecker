# telenav-spellChecker

A web server for local spell checker. 


## Environment Setup for venv

Use venv to create and manage the project for each virtual environment you have.
`sudo apt install -y python3-venv`

Go to a folder of your choice and create the following folder:
`mkdir environments`

Run the command inside this folder to create our venv (remember to always give it a good name):
`python3 -m venv enviornment_name`

Make sure the enviornment is activated:
`source enviornment_name/bin/activate`

To install all packages: 
`pip3 install -r requirements.txt`

## APIs
For backend, go to src/demo to run the Django application in order to test the endpoints:
`python manage.py runserver`

After you see the log showing our server is up and running, go to the browser and access http://localhost:8000/api/home/

For frontend, go to home-fe and run:
`npm start --prefix src/demo/home-fe`

It will automatically open the browser in the http://localhost:3000/ url. 



## Environment Setup for conda
To create conda environment with specific packages (preferred):  
`$ conda create --name <env_name> --file <this file_name>`  

To activate conda enviroment:  
`$ conda activate <env>`

To deactivate an active enviornment:  
`$ conda deactivate`

To install packages:  
`$ conda install <package_name>`

Most of them can be found at anaconda.org, choose the package that still being maintained.  
DO NOT use `$pip install <package_name>`

To update requirements.txt:  
`$conda list -e > requirements.txt`  
Remember to update requirements.txt if new packages are installed.  

To run in local:  
`$ bash run.sh`

## APIs

Check web page: http://127.0.0.1:8000/.

* home/history
    * GET:
        * Return all the queries in the DB.

* home/add_query
    * POST:
        * Return 201 and add the query in the DB.
        * Usage:  
        ```py
        Requested json format: {"query": <query>}
        ```

* home/search
    * POST:
        * Return list of (word, [candidates])
        ```
        For example

        Input: "5000 1st N ave."
        Return (Json serialized): 
        [
            ["5000", ["5000"]],
            ["1st", ["st", "1st", "21st"]],
            ["n", ["a", "in", "i", "ln"]],
            ["ave", ["ave", "have"]]
        ]
        ```

        * Usage:  
        ```
        Requested json format: {"query": <query>}