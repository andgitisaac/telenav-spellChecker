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

Then your command line will look like this: (the name in parentheses is your confirmation that you’re in the venv):

`(enviornment_name) user_name@localhost: _`

Note: Once inside a venv, you can use the commands pip or python normally. If you’d be out of it, you must go for pip3 and python3.

That’s it. You’re good to go with your venv.

## Django Installation
For Django installation, you need to run the following command inside of your venv:

`pip install django djangorestframework django-cors-headers`

Note that we’re installing two more dependencies for our API:
- Django REST Framework: a powerful and flexible toolkit for building Web APIs
- django-cors-headers: app for handling the server headers required for Cross-Origin Resource Sharing (CORS).

This is going to be useful when we try to access the API from front end (React).

## APIs
For backend, go to src/demo to run the Django application in order to test the endpoints:
`python manage.py runserver`

After you see the log showing our server is up and running, go to the browser and access http://localhost:8000/home/

For frontend, go to home-fe and run:
`npm start --prefix src/demo/home-fe`

It will automatically open the browser in the http://localhost:3000/ url. 


## More for APIs

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

## Others
This project front end was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).
This project whole work was credit from https://blog.logrocket.com/creating-an-app-with-react-and-django/.

## Available Scripts for front end

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.<br />
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.<br />
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.<br />
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.<br />
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: https://facebook.github.io/create-react-app/docs/code-splitting

### Analyzing the Bundle Size

This section has moved here: https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size

### Making a Progressive Web App

This section has moved here: https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app

### Advanced Configuration

This section has moved here: https://facebook.github.io/create-react-app/docs/advanced-configuration

### Deployment

This section has moved here: https://facebook.github.io/create-react-app/docs/deployment

### `npm run build` fails to minify

This section has moved here: https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify
