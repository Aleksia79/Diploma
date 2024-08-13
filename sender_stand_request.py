import configuration
import requests


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)

def get_order_info(response):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + str(response.json()["track"]))