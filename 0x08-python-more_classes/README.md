# Python Object-Oriented Programming (OOP) Readme

This readme provides an overview of important concepts and features related to Python Object-Oriented Programming (OOP). It covers various aspects of OOP, including classes, objects, attributes, methods, and special methods. By understanding these concepts, you'll be able to design and implement object-oriented programs in Python effectively.

## Table of Contents
- [General](#general)
- [Requirements](#requirements)

## General
Python programming is awesome for several reasons, and one of the major reasons is its support for OOP. Object-Oriented Programming is a powerful paradigm that allows you to structure your code in a modular and reusable way. It promotes code organization, encapsulation, and abstraction, making it easier to manage complex projects.

### What is OOP?
OOP is a programming paradigm that organizes code into objects, which are instances of classes. It focuses on modeling real-world entities as objects, which have properties (attributes) and behaviors (methods). OOP provides concepts such as encapsulation, inheritance, and polymorphism, allowing for efficient code reuse and modularity.

### "First-class everything"
In Python, everything is considered an object. This means that classes, functions, and even modules are objects that can be manipulated, passed around, and assigned to variables. Python follows the principle of "first-class everything," treating objects as first-class citizens.

### What is a class?
A class is a blueprint or template that defines the structure and behavior of objects. It encapsulates data (attributes) and functionality (methods) related to a specific concept or entity. Objects are created from classes and inherit their properties and behaviors.

### What is an object and an instance?
An object is a specific instance of a class. It represents a concrete entity based on the blueprint provided by the class. Each object has its own unique state and can access the attributes and methods defined in its class.

### What is the difference between a class and an object or instance?
A class is a definition or blueprint, while an object is an instance created from that class. Think of a class as a general description, and an object as a specific realization based on that description. Multiple objects can be created from a single class, each with its own state and behavior.

### What is an attribute?
An attribute is a piece of data associated with an object. It represents the state or characteristics of an object. Attributes can be variables defined within a class and accessed by objects created from that class.

### What are public, protected, and private attributes?
In Python, attributes can have different levels of visibility: public, protected, and private. Public attributes are accessible from anywhere. Protected attributes are conventionally indicated by a single leading underscore (_), indicating that they should be treated as internal to the class or its subclasses. Private attributes are indicated by a double leading underscore (__), which provides name mangling to avoid naming conflicts.

### What is self?
In Python, `self` is a conventionally used parameter name within methods of a class. It represents the instance of the class that the method is being called on. By using `self`, you can access the attributes and methods of the object within the class.

### What is a method?
A method is a function defined within a class. It represents the behavior or actions that objects of the class can perform. Methods are associated with objects and can access and modify the object's state.

### What is the special __init__ method and how to use it?
The `__init__` method is a special method in Python classes that is automatically called when a new object is created from the class. It is used to initialize the attributes of an object and perform any necessary setup or configuration. By defining the `__init

__` method, you can ensure that certain actions are executed when an object is created.

### What is Data Abstraction, Data Encapsulation, and Information Hiding?
Data abstraction is the process of hiding complex implementation details and providing a simplified interface. It allows you to focus on the essential features and behavior of an object without worrying about the internal workings.

Data encapsulation is the practice of bundling data and the methods that operate on that data within a class. It ensures that data is only accessed and modified through the defined methods, providing control over the data's integrity and preventing direct access from outside the class.

Information hiding is a concept related to encapsulation, where the internal details of a class are hidden from other classes or objects. It allows you to define public interfaces that provide access to the desired functionality while keeping the implementation details private.

### What is a property?
A property is a special attribute that allows you to define getter, setter, and deleter methods for accessing and modifying class attributes. Properties provide a way to encapsulate attribute access and add additional logic or validation when getting or setting attribute values.

### What is the difference between an attribute and a property in Python?
An attribute is a piece of data associated with an object, while a property is a special attribute that provides controlled access to another attribute. Properties allow you to define custom logic for getting, setting, and deleting attribute values, whereas regular attributes directly store and retrieve values.

### What is the Pythonic way to write getters and setters in Python?
In Python, the preferred way to define getters and setters for attributes is by using properties. By using the `@property` decorator for the getter method and the `@<attribute_name>.setter` decorator for the setter method, you can define properties that provide controlled access to the underlying attributes.

### What are the special __str__ and __repr__ methods and how to use them?
The `__str__` and `__repr__` methods are special methods in Python classes that provide string representations of objects. The `__str__` method is used to return an "informal" and nicely printable string representation, while the `__repr__` method provides a more detailed and technical representation.

By implementing these methods in a class, you can customize how objects of that class are displayed when using the `str()` function, the `print()` function, or when the object is shown directly. It allows you to present meaningful and descriptive information about the object.

### What is the difference between __str__ and __repr__?
The `__str__` method is used to provide a human-readable and informal string representation of an object. It is intended for end-users and should be a user-friendly representation.

The `__repr__` method, on the other hand, provides a detailed and unambiguous representation of an object. It is primarily used for debugging and development purposes. The output of `__repr__` should ideally be a string that can be used to recreate the object.

### What is a class attribute?
A class attribute is an attribute that is shared by all instances of a class. It is defined within the class but outside of any methods. Class attributes are accessed and modified using the class itself or any instance of the class. Changes made to a class attribute will be reflected in all instances of the class.

### What is the difference between an object attribute and a class attribute?
An object attribute is specific to a particular instance of a class. It is defined within the `__init__` method or any other instance method and is accessed and modified using the instance itself. Each instance can have different values for object attributes.

In contrast, a class attribute is shared among all instances of a class. It is defined outside of any instance methods and is accessed and modified using the class

 itself or any instance of the class. Class attributes have the same value for all instances of the class.

### What is a class method?
A class method is a method that is bound to the class and not the instances of the class. It is defined using the `@classmethod` decorator and takes the class (usually denoted as `cls`) as the first parameter instead of the instance (`self`). Class methods can access and modify class-level attributes and perform operations that are not specific to individual instances.

### What is a static method?
A static method is a method that does not have access to the instance or class. It is defined using the `@staticmethod` decorator and does not take any special parameters like `self` or `cls`. Static methods are independent of the state of the object or class and can be called on the class itself or any instance of the class.

### How to dynamically create arbitrary new attributes for existing instances of a class?
In Python, you can dynamically create new attributes for existing instances of a class by simply assigning a value to a new attribute name. For example, `instance.new_attribute = value` creates a new attribute called `new_attribute` and assigns the `value` to it. This allows you to add or modify attributes at runtime.

### How to bind attributes to objects and classes?
In Python, attributes can be bound to objects or classes by simply assigning a value to an attribute name. When an attribute is assigned to an instance, it becomes an object attribute specific to that instance. When an attribute is assigned to a class, it becomes a class attribute shared by all instances of the class.

### What does `__dict__` contain for a class and an instance of a class?
For a class, `__dict__` is a dictionary that contains the namespace of the class. It includes all the attributes and methods defined within the class, including class attributes.

For an instance of a class, `__dict__` is a dictionary that contains the namespace of the instance. It includes all the object attributes specific to that instance.

### How does Python find the attributes of an object or class?
When accessing an attribute of an object or class, Python follows a specific attribute resolution order known as the "attribute lookup." It starts by searching for the attribute within the instance namespace. If the attribute is not found, it continues to search in the class namespace. If the attribute is still not found, it traverses the inheritance hierarchy, searching in parent classes and their ancestors.

### How to use the `getattr` function?
The `getattr` function is used to dynamically access an attribute of an object or class. It takes two parameters: the object or class to retrieve the attribute from and the name of the attribute as a string. If the attribute is found, `getattr` returns its value. If the attribute is not found, `getattr` can return a default value or raise an exception.

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.\*)
- All your files must be executable
- The length of your files will be tested using `wc`

Make sure to follow these requirements when working on your project.
