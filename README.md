# AirBnB Clone Console

## Description of the Project
The **AirBnB Clone** project is a simplified replica of the AirBnB platform. It focuses on backend operations, including data storage, command-line interface (CLI) interactions, and application logic. The primary goal is to build a command interpreter that manages the application through a console-based interface.

This project is part of the Holberton School curriculum and serves as a foundation for understanding full-stack development, data models, and file storage.

---

## Description of the Command Interpreter
The **Command Interpreter** (console) is the entry point to interact with the AirBnB clone project. It allows users to:
- Create, retrieve, update, and delete objects such as `User`, `Place`, `State`, `City`, `Amenity`, and `Review`.
- Persist and retrieve data using a JSON-based storage engine.
- Execute commands in both interactive and non-interactive modes.

---

### How to Start the Command Interpreter

1. In interactive mode run the command:
- ./console.py
Then you can type commands such as create, show, update, etc

---

## How to use the command Interpreter

1. To create a new instance of a class:
- (hbnb) create <ClassName>

2. To retrieve a class
- (hbnb) retrieve <ClassName> <id>

## Examples
- (hbnb) create User
- (hbnb) retrieve User <user_id>
