from http import HTTPStatus


def test_root_deve_retornar_ok_e_helloworld(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'password': 'testpassword',
            'email': 'test@email.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'testusername',
        'email': 'test@email.com',
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {'id': 1, 'username': 'testusername', 'email': 'test@email.com'}
        ]
    }


def test_read_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'testusername',
        'email': 'test@email.com',
    }


def test_read_user_not_found(client):
    response = client.get('/users/-5')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'id': 1,
            'username': 'alteredusername',
            'password': 'testpassword',
            'email': 'test@email.com',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'alteredusername',
        'email': 'test@email.com',
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/-5',
        json={
            'id': -5,
            'username': 'alteredusername',
            'password': 'testpassword',
            'email': 'test@email.com',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted!'}


def test_delete_user_not_found(client):
    response = client.delete('/users/-5')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
