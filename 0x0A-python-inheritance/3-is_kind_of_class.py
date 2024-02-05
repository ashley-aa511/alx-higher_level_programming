#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class; otherwise False.
    """
    return isinstance(obj, a_class)

# Example usage:
class BaseClass:
    pass

class DerivedClass(BaseClass):
    pass

obj_instance_base = BaseClass()
obj_instance_derived = DerivedClass()

# Test cases
print(is_kind_of_class(obj_instance_base, BaseClass))   # Should print True
print(is_kind_of_class(obj_instance_derived, BaseClass)) # Should print True
print(is_kind_of_class(obj_instance_derived, str))       # Should print False
