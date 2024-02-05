#!/usr/bin/python3
def lookup(obj):
    return [attribute for attribute in dir(obj) if not callable(getattr(obj, attribute)) or attribute.startswith("__")]

# Example usage:
class ExampleClass:
    def __init__(self):
        self.attribute1 = "value1"
        self.attribute2 = "value2"

    def method1(self):
        pass

    def method2(self):
        pass

example_instance = ExampleClass()

result = lookup(example_instance)
print(result)
