import requests
import configuration
import data

# Ивченко Генрих, 36-я когорта - Финальный проект.
def create_order():
    response = requests.post(
        configuration.url + configuration.create_order, json=data.order_data)
    return response.json()["track"]


def get_order_by_track(track_number):
    response = requests.get(f"{configuration.url}{configuration.order_track_info}?t={track_number}")
    return response


track = create_order()


def test_get_order_by():
    track_number = track
    response = get_order_by_track(track_number)
    assert response.status_code == 200
