 ![juli.co](https://github.com/julianramirezch/juli_url_shortener/blob/master/src/juli_url_shortener.png)

<p align="center"> 
    <b>HBnb the Console!<b>

---

## AirBnB clone, first part, the console

---

Description

>We will create a storage system, creating objects through execution and saving them to a Js. We will manipulate two types of storage, file and DataBase, for this projecy we will focus on file.
---
### Program download
>To download this program, you must go to this github repo and download it:

    https://github.com/julianramirezch/AirBnB_clone.git

>Once in your local repo, you can run it from the folder using the following command:

    ./console.py

### Execution:
>There are two modes
    
    Interactive mode:
>$ ./console.py

    $  (hbnb) [write here your commands]

>Non-interactive mode

    $ echo "[put_commands and_arguments]" | ./console.py

### Commands

    • help
    • EOF
    • quit
    • create
    • show
    • destroy
    • all
    • update
    • count
### Examples
    1. help
    • non interactive

$ echo "help" | ./console.py

    $ (hbnb) 
    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update

    (hbnb)


    • interactive mode

>$ ./console.py

     (hbnb) help

>(hbnb)

>Documented commands (type help <topic>):
 
>========================================
 
>EOF  all  count  create  destroy  help  quit  show  update

>(hbnb)

    (hbnb) quit

$
### Some error output

>$ ./console.py

    (hbnb) all MyModel
    ** class doesn't exist **
    (hbnb) show BaseModel
    ** instance id missing **
    (hbnb) show BaseModel Holberton
    ** no instance found **



### Tasks:

| Name | Description                    |
| ------------- | ------------------------------ |
| `__init__.py`      |  With this file, the folder will become a Python module   |
| `models/base_model`      | Class Base |
| `models/engine/file_storage`      | Class Filestorage |
| `models/amenity.py`   | Class Amenity   |
| `models/city.py`      | Class City|
| `models/place.py`      | Class Place|
| `models/review.py`      | Class Review|
| `models/state.py`      | Class State|
| `models/user.py`      | Class User|
| `tests/test_models/test_base.py`      | Test Class Base |
| `tests/test_models/test_engine/test_file_storage.py`      |  Test Class FileStorage   |
| `tests/test_models/test_amenity.py`      |  Test Class Amenity   |
| `tests/test_models/test_place.py`      |  Test Class Place   |
| `tests/test_models/test_city.py`      |  Test Class City   |
| `tests/test_models/test_state.py`      |  Test Class State   |
| `tests/test_models/test_user.py`      |  Test Class User   |
| `tests/test_models/test_review.py`      |  Test Class Review    |

## Author: 
### Julian Ramirez <julianramirezch1@gmail.com>
### Santiago Mendieta <santmendieta@icloud.com>
----
[![Twitter Follow](https://img.shields.io/twitter/follow/JulianR_30.svg?style=social&label=Follow)](https://twitter.com/JulianR_30)

[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/sto_stat.svg?style=social&label=Follow%20%40sto_stat)](https://twitter.com/sto_stat)

2020
