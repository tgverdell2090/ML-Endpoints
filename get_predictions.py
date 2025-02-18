from requests import get

def single_prediction():

    url = "http://0.0.0.0:5001/model/v1"

    params = {
        'AveRooms': 3,
        'AveBedrms': 1
    }

    response = get(url, params=params)

    print(response.json())

def batch_predictions():

    url = "http://0.0.0.0:5001/model/v1/batch"

    json = [
        {'AveRooms': 9, 'AveBedrms': 3},
        {'AveRooms': 5, 'AveBedrms': 3},
        ]

    response = get(url, json=json)

    print(response.json())
