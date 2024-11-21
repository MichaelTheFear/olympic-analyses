import json

from fastapi.testclient import TestClient
from endpoints import app  # Replace 'main' with the filename where your app instance is defined

client = TestClient(app)

def test_get_fairest_sports():
    response = client.get("/api/fairestSports", params={"agg_level": "Sport", "gender": "M"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all(isinstance(item, dict) for item in data)
    for item in data:
        assert "Sport" in item
        assert "total" in item
    print(data)

def test_get_fairest_sports_2():
    response = client.get("/api/fairestSports", params={"agg_level": "Event", "gender": "F"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all(isinstance(item, dict) for item in data)
    for item in data:
        assert "Event" in item
        assert "total" in item
    print(data)

def test_get_features_sport():
    response = client.get(
        "/api/getFeatures",
        params={
            "agg_level": "Sport",
            "names": ["Football", "Basketball"],
            "gender": "M"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list), "Response data should be a list"
    assert all(isinstance(item, dict) for item in data), "Each item in data should be a dict"
    for item in data:
        assert "Sport" in item, "Each item should contain 'Sport' key"
        # You can add more assertions here based on the expected keys in the item
    print(data)

def test_get_names_sport():
    response = client.get(
        "/api/getNames",
        params={
            "agg_level": "Sport",
            "gender": "M"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list), "Response data should be a list"
    assert all(isinstance(item, str) for item in data), "Each item in the response should be a string"
    print(data)


def test_get_sports_for_user():
    user_data = {
        "Height": 194,
        "BMI": 25.8,
        "Age": 21,
        "Sex": "M",
        "NOC": "BRA"
    }

    response = client.get(
        "/api/getSportsForUser",
        params={
            "_user_data": json.dumps(user_data),
            "agg_level": "Sport"  # Replace with the actual agg_level in your dataset
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list), "Response should be a list of dictionaries"
    assert all(isinstance(item, dict) for item in data), "Each item in the response should be a dictionary"
    for item in data:
        assert "Sport" in item or "Event" in item, "Each item should contain the aggregation level key"
        assert "Distance" in item, "Each item should contain a 'Distance' key"
    print(data)

# test_get_fairest_sports()
# test_get_fairest_sports_2()
# test_get_features_sport()
# test_get_names_sport()
test_get_sports_for_user()