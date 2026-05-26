from dataclasses import dataclass
from typing import override


@dataclass
class City:
    name: str
    population: int

    @override
    def __str__(self) -> str: 
        return f"{self.name} ({self.population} hab.)"