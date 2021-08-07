from .base import Base
from db import db


class HNX30(Base, db.Model):
    __tablename__ = 'HNX30'

    def __init__(self, date, price_close, price_open, price_high, price_low, volume, change):
        super().__init__(date, price_close,
                         price_open, price_high, price_low, volume, change)
