from pydantic import BaseModel, condecimal
from datetime import date


class StatisticSchema(BaseModel):
    id: int
    date: date
    views: int
    clicks: int
    cost: condecimal(max_digits=10, decimal_places=2)
    cpc: condecimal(max_digits=10, decimal_places=2)
    cpm: condecimal(max_digits=10, decimal_places=2)