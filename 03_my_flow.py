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

if __name__ == "__main__":
    # For instance methods, you must instantiate the class first
    obj = MyClass()
    obj.my_instance_method.deploy(
        name="instance-method-deployment",
        work_pool_name="default-work-pool"
    )

    # For class methods, call deploy directly on the class attribute
    MyClass.my_class_method.deploy(
        name="class-method-deployment",
        work_pool_name="default-work-pool"
    )

