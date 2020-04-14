# telenav-spellChecker

This is a web page for local spell checker. 

To run in local:
`$ bash run.sh` or `$ ./run.sh`.

To create package in conda environment (preferred):
`$ conda create --name <env> --file <this file>`
e.g. conda create --name spellcheckerUIEnv --file requirements.txt

To activate conda enviroment and run package: 
`$ conda activate <env>`
`$ bash run.sh` 

To deactivate an active enviornment: 
`$ conda deactivate`

Use GET to get access to home/index. 
Use POST to get acess to home/add_query.
Return 201 when add query successfully and 400 when fail. 

Check web page:
http://127.0.0.1:5487/home/add_query 