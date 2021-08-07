from .base import Base
from db import db


class VNI(Base, db.Model):
    __tablename__ = 'VNI'

    def __init__(self, date, price_close, price_open, price_high, price_low, volume, change):
        super().__init__(date, price_close,
                         price_open, price_high, price_low, volume, change)
