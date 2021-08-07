from db import ma


class Schema(ma.Schema):
    class Meta:
        fields = (
            "date",
            "price_close",
            "price_open",
            "price_high",
            "price_low",
            "volume",
            "change"
        )
