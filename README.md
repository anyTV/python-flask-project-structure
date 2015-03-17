# python_flask


## Project Structure
	- app
		- module-1
			- __init__.py
			- dispatch.py
		.
		.
		.
		- module-n
		- _models
			- model1.py
		- __init__.py
	
	- instance
		- env
			- development.py
			- custom_config.py
		- config.py

	- lib
		- database.py
		- error_handler.py
		- res.py

	- venv

	- requirements.txt
	- run.py

## Request context
	app - contains the files for the main app
	
	module-n - contains the files for secific module (eg. user module)
		dispatch.py - this file contains all the request context and will be responsible for the routing and setting request related functions.
		__init__.py will contain all the functions native to the object. All functions and variables in this file most not be dependent on the request context. eg. the function "register" should be put in dispatch while the function "create user" is in __init__.py. The function register is responsible for getting all the clean data from the request.
	
	_models - put models file here if needed.

	instance - contains all the config files.

	lib - contains all the core files
