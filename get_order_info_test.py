import sender_stand_request
import data



#тест для получения заказа по его треку
def test_get_order_info():
    response = sender_stand_request.post_new_order(data.order_body)
    status = sender_stand_request.get_order_info(response).status_code
    assert status == 200

# Александра Дианова, 20-я когорта — Финальный проект. Инженер по тестированию плюс