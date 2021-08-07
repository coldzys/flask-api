from datetime import date, timedelta

NUMBER_OF_DAYS = 10
URL = "https://svr8.fireant.vn/api/Data/Companies/HistoricalQuotes"
TIME = f"startDate={date.today() - timedelta(NUMBER_OF_DAYS)}&endDate={date.today()}"

CODE = {
    "VNI": URL + "?symbol=VNI&" + TIME,
    "STB": URL + "?symbol=STB&" + TIME,
    "VN30": URL + "?symbol=VN30&" + TIME,
    "HNX30": URL + "?symbol=HNX30&" + TIME,
    "TPB": URL + "?symbol=TPB&" + TIME,
    "FTM": URL + "?symbol=FTM&" + TIME,
    "HDG": URL + "?symbol=HDG&" + TIME,
    "VNP": URL + "?symbol=VNP&" + TIME,
    "KDM": URL + "?symbol=KDM&" + TIME,
    "VPG": URL + "?symbol=VPG&" + TIME,
}

PAYLOAD = ["Date", "PriceClose", "PriceOpen", "PriceHigh", "PriceLow", "Volume"]
