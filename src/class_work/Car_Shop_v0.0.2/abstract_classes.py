# abstract_classes.py
'''
Здесь описаны абстрактные классы и интерфейсы:
'''

from abc import ABC, abstractmethod

class ICar(ABC):
    @abstractmethod
    def display_info(self):
        pass

    @abstractmethod
    def configure_vehicle(self):
        pass