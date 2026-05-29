from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(kw_only=True)
class Form(ABC):
    name: str | None = None

    @abstractmethod
    def translate(self, delta_x: float, delta_y: float) -> None:
        pass