from abc import ABC, abstractmethod

class BookingKendaraan(ABC):
    @abstractmethod
    def pesan(self, usia: int) -> bool:
        pass
