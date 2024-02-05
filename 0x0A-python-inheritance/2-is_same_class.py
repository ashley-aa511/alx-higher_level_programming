#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class, otherwise False."""
    return type(obj) == a_class

# Example usage:
class ExampleClass:
    pass

obj_instance = ExampleClass()

# Test cases
print(is_same_class(obj_instance, ExampleClass))  # Should print True
print(is_same_class(obj_instance, str))           # Should print False
