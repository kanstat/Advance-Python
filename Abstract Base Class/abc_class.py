"""Abstract Base Class"""

"""
An abstract class in Python is a class that cannot be instantiated on its own and serves as a blueprint
for other classes to inherit from. It is essentially a class that provides a template for its subclasses to follow,
and it is up to the subclasses to implement the abstract methods defined in the abstract class.

:
"""




from abc import ABC, abstractmethod
class abstract_base_class(ABC):
    @abstractmethod
    def abstract_method_name(self):
        pass
