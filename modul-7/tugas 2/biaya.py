from abc import ABC, abstractmethod

class BiayaKendaraan(ABC):
    @abstractmethod
    def hitung_biaya(self) -> float:
        pass
