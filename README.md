# Library Management System

A command-line based Library Management System built with Python and Object-Oriented Programming principles. This project was developed as part of my journey in mastering software development concepts such as OOP, file handling, user authentication, and data persistence.

## Overview

The Library Management System is designed to simulate how a real-world library operates. The application provides separate roles for administrators and users, each with specific permissions and responsibilities.

Administrators can manage the library's collection by adding books and monitoring available inventory, while registered users can browse available books and borrow them.

The project currently operates as a Command Line Interface (CLI) application and serves as a practical exercise in applying Python programming concepts to solve real-world problems.

## Features

### Authentication System

* User registration
* User login
* Admin registration
* Admin login

### Book Management


* Add new books
* View available books
* Track borrowed books

### User Operations

* Browse available books
* Borrow books
* View borrowed books

### Data Persistence

* Store library data using JSON files
* Maintain records between application sessions

## Technologies Used

* Python
* JSON
* Object-Oriented Programming (OOP)

## Skills Demonstrated

This project highlights several core software engineering concepts:

* Object-Oriented Programming
* Class Design
* Encapsulation
* File Handling
* Data Persistence
* Authentication Logic
* Clean Code Practices
* Problem Solving
* Software Architecture Fundamentals

## Project Structure

```text
library-management-system/
│
├── models/
│   ├── user.py
│   ├── admin.py
│   └── book.py
│
├── data/
│   ├── users.json
│   ├── admins.json
│   └── books.json
│
├── services/
│   ├── auth_service.py
│   ├── library_service.py
│
├── main.py
│
└── README.md
```

## Learning Objectives

The primary goal of this project is not simply to build a library system but to strengthen my understanding of professional software development practices.

Through this project, I am actively learning:

* How to design reusable classes
* How to organize larger Python applications
* How to separate responsibilities across modules
* How to persist application data
* How authentication systems work
* How real-world software projects evolve over time

## Future Improvements

Planned enhancements include:

* Migration from JSON storage to a database
* Web-based interface
* Book return functionality
* Search and filtering system
* Password hashing
* Input validation improvements
* Activity logs
* REST API integration
* Automated testing

## Why This Project Matters

Many beginner projects focus only on producing output. This project focuses on building software using maintainable design principles while solving a realistic problem.

The application demonstrates how Python can be used to manage data, implement authentication systems, enforce role-based access, and organize code using Object-Oriented Programming techniques.

## About Me

Hi, I'm **Alpha-Coder042**.

I'm a student at the University of Port Harcourt and a self-taught Python developer passionate about software engineering and Artificial Intelligence.

My current focus is strengthening my programming fundamentals through practical projects while preparing for larger backend and AI-related applications.

I'm continuously learning and improving my skills through hands-on development and real-world problem solving.

## Connect With Me

GitHub: https://github.com/Alpha-Coder042

Feel free to explore the project, provide feedback, or contribute ideas for future improvements.
