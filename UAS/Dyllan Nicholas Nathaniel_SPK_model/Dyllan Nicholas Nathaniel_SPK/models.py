from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Smartphone(Base):
    __tablename__ = 'spk_dyllan_nicholas_nathaniel_201011402073_07tplp013'
    id = Column(Integer, primary_key=True)
    brand = Column(String(50))
    ram = Column(String(50)) 
    storage = Column(String(10))
    prosesor = Column(String(50))
    baterai = Column(String(20))
    ukuran_layar = Column(String(10))
    harga = Column(String(20))

    def __repr__(self):
        return f"spk_dyllan_nicholas_nathaniel_201011402073_07tplp013(id={self.id!r}, brand={self.brand!r}"
