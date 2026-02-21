def test_create_item(client):
    item_data = {
        "name": "Minecraft",
        "description": "Best selling game",
        "price": 450,
        "available": True,
    }

    response = client.post("/items/", json=item_data)

    assert response.status_code == 201

    data = response.json()

    assert "id" in data
    assert data["name"] == "Minecraft"
    assert data["price"] == 450

def test_get_all_items(client):
    client.post(
        "/items/",
        json={
            "name": "Coca-cola",
            "description": "Delicous and refreshing drink",
            "price": 15,
            "available": False,
        },
    )

    response = client.get("/items/")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

def test_get_item_by_id(client):
    create_response = client.post(
        "/items/",
        json={
            "name": "Blue T-shirt",
            "price": 450,
            "available": True,
        },
    )

    item_id = create_response.json()["id"]

    response = client.get(f"/items/{item_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == item_id

def test_get_item_by_id_not_found(client):
    response = client.get("/items/nonexistent-id")

    assert response.status_code == 404

def test_update_item(client):
    create_response = client.post(
        "/items/",
        json={
            "name": "Keyboard for PC",
            "description": "Amazon built",
            "price": 349,
            "available": True,
        },
    )

    item_id = create_response.json()["id"]

    response = client.put(f"/items/{item_id}", json={"price": 579, "available": False})

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == item_id
    assert data["price"] == 579
    assert data["available"] is False

def test_update_item_not_found(client):
    response = client.put("/items/nonexistent-id", json={"price": 199})

    assert response.status_code == 404

def test_delete_item(client):
    create_response = client.post(
        "/items/",
        json={
            "name": "Grand Theft Auto VI",
            "description": "Coming soon to PS5 and Xbox Series X",
            "price": 1599,
            "available": False,
        },
    )

    item_id = create_response.json()["id"]

    response = client.delete(f"/items/{item_id}")

    assert response.status_code == 204

    get_response = client.get(f"/items/{item_id}")

    assert get_response.status_code == 404

def test_delete_item_not_found(client):
    response = client.delete("/items/nonexistent-id")

    assert response.status_code == 404