from datetime import datetime
from sqlalchemy.orm import sessionmaker
import glob
import os

from stock_code import CODE
from db import engine, base, PATH


def update():
    for code, table in CODE.items():
        with open(f"./021/crawled/{code}.csv", "r") as f:
            rows = f.readlines()
        for row in rows:
            row = row.strip().split(",")
            date = datetime.strptime(row[0], '%Y-%m-%d').date()
            price_close = float(row[1])
            price_open = float(row[2])
            price_high = float(row[3])
            price_low = float(row[4])
            volume = float(row[5])
            change = float(row[6])
            new_stock = table(date, price_close, price_open,
                              price_high, price_low, volume, change)
            Session = sessionmaker(bind=engine)
            session = Session()
            session.add(new_stock)
            session.commit()


if __name__ == "__main__":
    files = glob.glob(PATH + "*")
    for f in files:
        os.remove(f)
    base.metadata.create_all(engine)
    update()
