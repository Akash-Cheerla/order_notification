from loguru import logger


def find_orders(orders, arrival_rate, service_rate, config):
    response = {"status": False, "stderr": None, "stdout": None}
    logger.info("Number of orders = {}, arrival rate = {}, service rate = {}".format(len(orders), arrival_rate, service_rate))

    try:
        if len(orders) < config["min_order_length"]:
            selected_orders = []
            for order_no in orders:
                selected_orders.append(order_no)
            response["stdout"] = {"order_nos": selected_orders}
        else:
            number_of_orders = int(len(orders)*arrival_rate/service_rate)
            logger.info("Number of Selected Orders = {}".format(number_of_orders))
            sorted_orders = sorted(orders)[:number_of_orders]
            response["stdout"] = {"order_nos": sorted_orders}

        response["status"] = True
    except Exception as ex:
        response["stderr"] = str(ex)
    
    return response

