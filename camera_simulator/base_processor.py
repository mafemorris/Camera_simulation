"""Base processor of a camera simulator

Abstract class with the abstract method process that will have the processes of the camera compounds.
Also, it tells if the camera is enabled or not. 

    Typical usage example:
    
    class ExampleClass(Base_processor):
"""
from abc import ABC, abstractmethod


class Base_processor(ABC):
    """The base processor of a camera simulator

    Attributes:
        _enable: A boolean indicating if the base processor is enabled or not.
    """

    def __init__(self):
        """Inits base_processor with enable True."""
        self._enable = True

    @abstractmethod
    def process(self, image):
        """Abstract method of the process of the camera compoounds."""
        pass

    # Enable Property
    @property
    def enable(self):
        """Getter of the enable property"""
        return self._enable

    @enable.setter
    def enable(self, _enable):
        """Setter of the enable property"""
        self._enable = _enable
