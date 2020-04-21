# telenav-spellChecker

A web server for local spell checker. 

## Environment Setup
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

Check web page: http://127.0.0.1:5487/.

Currently there are 2 apis for testing.  
CSRF tokens are needed for the POST methods.

* home/index
    * GET:
        * Return all the queries in the DB.

* home/add_query
    * POST:
        * Return 201 and add the query in the DB.
        * Usage:  
        ```py
        Requested json format: {"query": <query>}
        ```

    * GET:
        * <font color="#dd0000">Will be disabled later</font><br/>
        * Return 200 and the query in the request.
        * Usage: Add `?query=<query>` to the url.   
