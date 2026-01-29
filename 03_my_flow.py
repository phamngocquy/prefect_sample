# your_file.py
from prefect import flow

class MyClass:
    @flow
    def my_instance_method(self):
        return "Hello, from an instance method!"

    @flow
    @classmethod
    def my_class_method(cls):
        return "Hello, from a class method!"
MyClass().my_instance_method()
