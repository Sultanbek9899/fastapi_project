import datetime
import ormar
from typing import Optional, List, Union, Dict
from pydantic import condecimal
from db import MainMata


class Statistic(ormar.Model):
    class Meta(MainMata):
        pass

    id: int = ormar.Integer(primary_key=True, autoincrement=True)
    date: datetime.date = ormar.Date(nullable=False)
    views: int = ormar.Integer(default=0, nullable=True)
    clicks: int = ormar.Integer(default=0, nullable=True)
    cost: condecimal(max_digits=10, decimal_places=2) = ormar.Decimal(
        nullable=True,
        default=0,
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.date}'

    @staticmethod
    def order_fields():
        return [
            "id", "date", "views", "clicks", "cost", "cpc", "cpm"
        ]
