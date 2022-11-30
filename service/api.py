from typing import List, Union
from pydantic import condecimal
from datetime import date
from fastapi import APIRouter,HTTPException
from db import database
from service.models import Statistic
from service.shemas import StatisticSchema
from service.utils import get_statistic_query
service_router = APIRouter()

CreateStatistic = Statistic.get_pydantic(exclude={"id": ...})
GetStatistic = Statistic.get_pydantic()


@service_router.post("/create/statistic", response_model=GetStatistic, status_code=201)
async def create_statistic(statistic: CreateStatistic):
    return await Statistic(**statistic.dict()).save()


@service_router.get("/get/statistic", response_model=List[StatisticSchema])
async def get_statistic(
        from_date: Union[None, date] = None,
        to_date: Union[None, date] = None,
        order_field: str = 'date'
    ):
    if order_field not in Statistic.order_fields():
        raise HTTPException(
            status_code=400,
            detail=f"{order_field} order field does not exist. Possible Fields {','.join(Statistic.order_fields())}")
    query = get_statistic_query(from_date, to_date, order_field)
    qs = await database.fetch_all(query)
    qs = list(map(dict, qs))
    return qs


@service_router.delete("/delete/statistic", )
async def delete_statistic():
    await Statistic.objects.delete(each=True)
    return {"status": "ok"}
