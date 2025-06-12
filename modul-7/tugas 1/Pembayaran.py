from abc import ABC, abstractmethod

class MetodePembayaran(ABC):
    @abstractmethod
    def bayar(self, jumlah: float) -> float:
        pass
