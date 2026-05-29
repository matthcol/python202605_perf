from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Form(ABC):
    name: str

    @abstractmethod
    def translate(self, delta_x: float, delta_y: float) -> None:
        pass