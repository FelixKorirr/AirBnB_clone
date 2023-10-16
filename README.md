# AirBnB Clone - The Console
The console is the first segment of the AirBnB project that will collectively cover fundamental concepts of higher level programming. In this segment, the command interpreter is built to manage objects for the AirBnB(HBnB) website.

#### Functionalities of the command interpreter:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Examples of use](#examples-of-use)
* [Author](#author)

## Environment
This project is interpreted/tested on Ubuntu 20.04 LTS using python3 (version 3.8.10)

## Installation
* Clone this repository: `git clone https://github.com/FelixKorirr/AirBnB_clone.git`
* Access the directory: `cd AirBnB_clone`
* Run hbnb: `./console.py` and press Enter command

## File Descriptions
[console.py](console.py) - This is the entry point to the command interpreter.
List of commands:
* `EOF` - exits console 
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file). 
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 

#### `models/` directory contains classes used for this project:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the basemodel class
* `def __str__(self)` - Contains the string representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary representation of an instance

Classes inheriting from Base Model:
* [amenity.py](/models/amenity.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [city.py](/models/city.py)

#### `/models/engine` directory contains File Storage class that handles JSON serialization and deserialization :
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* ` def reload(self)` -  deserializes the JSON file to __objects

## Examples of use
## Example 1
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help quit
Quit command to exit the program.
(hbnb) quit
``` 
## Example 2
```
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
cebd134a-614e-401b-a20c-f94ce9223383
(hbnb) destroy BaseModel cebd134a-614e-401b-a20c-f94ce9223383
(hbnb) 

```

## Author
Felix Kipkorir - [Github](https://github.com/FelixKorirr)
