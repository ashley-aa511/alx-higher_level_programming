#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited (directly or indirectly)
    from the specified class; otherwise False.
    """
    return issubclass(type(obj), a_class)

# Example usage:
class BaseClass:
    pass

class IntermediateClass(BaseClass):
    pass

class DerivedClass(IntermediateClass):
    pass

obj_instance_base = BaseClass()
obj_instance_derived = DerivedClass()
