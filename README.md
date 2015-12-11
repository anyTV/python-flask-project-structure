Python Flask Project Structure
=====

Introduction
-----
A boilerplate for REST APIs implement using python flask and pymysql. This project uses python3 and follows the (company's Python conventions)(https://github.com/anyTV/Python-conventions).

## Running the application

1. Download zip
2. Extract to your project's folder
3. Import `database/schema.sql` and `database/seed.sql`
  ```sh
  mysql -uroot < database/schema.sql
  mysql -uroot < database/seed.sql
  ```
4. Install dependecies
  ```sh
  python setup.py
  ```
5. Update instance/config.py
5. Run the app
  ```sh
  python run.py
  ```

Project Structure
-----
  - app
    - module-1
      - __init__.py
      - dispatch.py
    - module-n
      - __init__.py
      - dispatch.py
  - instance
    - env
      - development.py
      - production.py
      - staging.py
    - config.py
  - lib
    - database.py
    - error_handler.py
    - response.py
  - venv
  - setup.py
  - run.py

## Request context
  app - contains the files for the main app

  module-n - contains the files for secific module (eg. user module)

  module-n/dispatch.py - this file contains all the request context and will be responsible for the routing and setting request related functions.

  module-n/\_\_init\_\_.py will contain all the functions native to the object. All functions and variables in this file most not be dependent on the request context. eg. the function "register" should be put in dispatch while the function "create user" is in __init__.py. The function register is responsible for getting all the clean data from the request.

  instance - contains all the config files.

  lib - contains all the core files

  util - contains helper functions

## Author
[Freedom! Labs, any.TV Limited DBA Freedom!](https://www.freedom.tm)

