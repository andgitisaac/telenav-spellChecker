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
        Return: [
            ["5000", ["5000"]],
            ["1st", ["st", "1st", "21st"]],
            ["n", ["a", "in", "i", "ln"]],
            ["ave", ["ave", "have"]]
        ]
        ```

        * Usage:  
        ```
        Requested json format: {"query": <query>}
        ```
