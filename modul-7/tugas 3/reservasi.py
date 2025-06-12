from abc import ABC, abstractmethod

class BisaDireservasi(ABC):
    @abstractmethod
    def reservasi(self) -> None:
        pass
