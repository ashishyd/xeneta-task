import json
from app import app


def test_get_test():
    """
    Test the `/test` endpoint
    """
    with app.test_client() as client:
        response = client.get('/test')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['message'] == 'test route'


def test_get_rates():
    """
    Test the `/rates` endpoint
    """
    with app.test_client() as client:
        response = client.get('/rates')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) == 0


def test_get_rates_with_args():
    """
    Test the `/rates` endpoint with args
    """
    with app.test_client() as client:
        response = client.get('/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=EETLL')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data) > 0
