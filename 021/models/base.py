from sqlalchemy.sql.sqltypes import Date
from sqlalchemy import Column, Float


class Base():

    date = Column(Date, nullable=False, primary_key=True)
    price_close = Column(Float, nullable=False)
    price_open = Column(Float, nullable=False)
    price_high = Column(Float, nullable=False)
    price_low = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)
    change = Column(Float, nullable=False)

    def __init__(self, date, price_close, price_open, price_high, price_low, volume, change):
        self.date = date
        self.price_close = price_close
        self.price_open = price_open
        self.price_high = price_high
        self.price_low = price_low
        self.volume = volume
        self.change = change
