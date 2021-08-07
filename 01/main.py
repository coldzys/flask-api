import requests
import pandas as pd
import schedule
import time
from stock_code import CODE, PAYLOAD


def crawl_stock_data():
    for code, url in CODE.items():
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data)
        df = df[PAYLOAD]
        changes = [0]
        for i in range(1, len(df.index)):
            change = (df["PriceClose"][i] - df["PriceClose"]
                      [i - 1]) / df["PriceClose"][i - 1]
            changes.append(round(change * 100, 2))
        df["Change"] = changes
        df["Date"] = df["Date"].str[0:10]
        df.to_csv("./01/databases/" + code + ".csv", header=False, index=False)


if __name__ == '__main__':
    schedule.every().day.at("15:00").do(crawl_stock_data)

    while True:
        schedule.run_pending()
        time.sleep(1)
