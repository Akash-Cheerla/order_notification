import os
import json
from loguru import logger
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from core import find_orders
from models import OrderRequest, OrderResponse

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

app = FastAPI(
    title="Order Notification",
    description="API for selecting orders for which notification will be sent.",
    version="1.0.0",
    extra={"vf": 23}
    )

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/order", response_model=OrderResponse)
def find_order_ids(payload: OrderRequest, request: Request):
    logger.info("Recevied request for id = {}".format(payload.id))
    response = find_orders(payload.orders_nos, payload.arrival_rate, payload.service_rate, config)
    if response["status"]:
        logger.info("Successfully returning the response")
        return {"id": payload.id, **response["stdout"]}
    else:
        logger.error("Error = {}".format(response["stderr"]))
        raise HTTPException(status_code=500, detail=response["stderr"])
