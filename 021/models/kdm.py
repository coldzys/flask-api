from .base import Base
from db import base


class KDM(Base, base):
    __tablename__ = 'KDM'

    def __init__(self, date, price_close, price_open, price_high, price_low, volume, change):
        super().__init__(date, price_close,
                         price_open, price_high, price_low, volume, change)
