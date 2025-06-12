from abc import ABC, abstractmethod

class BisaDipinjam(ABC):
    @abstractmethod
    def pinjam(self) -> None:
        pass
