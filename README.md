# telenav-spellChecker

This is a web page for local spell checker. 

To run in local:
`$ bash run.sh` or `$ ./run.sh`.

To create conda environment with specific packages (preferred):
`$ conda create --name <env> --file <this file>`
e.g. conda create --name spellcheckerUIEnv --file requirements.txt

To activate conda enviroment: 
`$ conda activate <env>`
`$ bash run.sh` 

To deactivate an active enviornment: 
`$ conda deactivate`

To install packages:
`$ conda install <package_name>`

Most of them can be found at anaconda.org, choose the package that still being maintained.
DO NOT use `$pip install <package_name>`.

Remember to update requirements.txt if new packages are installed.
To update requirements.txt:
`$conda list -e > requirements.txt`

Use GET to get access to home/index. 
Use POST to get acess to home/add_query.
Return 201 when add query successfully and 400 when fail. 

Check web page:
http://127.0.0.1:5487/home/add_query 