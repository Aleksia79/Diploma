import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
# Это популярная библиотека, которая позволяет взаимодействовать с веб-сервисами
import requests
#Этот код отправляет HTTP GET-запрос к заданному URL-адресу, который складывается
#из базового адреса сервиса и пути к его документации, оба определены в модуле
#конфигурации. Затем он выводит HTTP-статус код ответа от сервера, который указывает
#на результат выполнения запроса.
# Импорт данных запроса из модуля data, в котором определено тело запроса
import data


def post_new_order(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_ORDERS объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)

def get_order_info(response):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + str(response.json()["track"]))
#нужно задать переменную для GET-запроса получив значение из пары ключа+значение в POST-запросе на создание заказа


#тест для получения заказа по его треку
def test_get_order_info():
    response = post_new_order(data.order_body)
    status = get_order_info(response).status_code
    assert status == 200

# Александра Дианова, 20-я когорта — Финальный проект. Инженер по тестированию плюс