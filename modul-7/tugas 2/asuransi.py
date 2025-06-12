from abc import ABC, abstractmethod

class AsuransiKendaraan(ABC):
    @abstractmethod
    def biaya_asuransi(self) -> float:
        pass
