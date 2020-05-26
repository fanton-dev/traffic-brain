'''
This file (test_traffic_light.py) contains the functional tests for the users blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the traffic_light blueprint.
'''

import os.path
from os import path
import json


def test_animation_valid(test_client):
    '''
    GIVEN a Flask application
    WHEN the '/traffic-light/animation' route is posted to valid data (POST)
    THEN check the response is valid

    Parameters:
    -----------
    test_client
        Flask test application

    Returns:
    --------
    None
    '''

    data = {
        "name": "pytest_animation1",
        "fps": 0,
        "looped": False,
        "frames": [
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        ]
    }
    response = test_client.post('/traffic-light/animation',
                                data=json.dumps(data),
                                content_type='application/json')

    # Verifing response
    assert response.status_code == 200
    assert response.data == b'OK'

    # Verifing a file was created
    assert path.exists('server/static/animations/pytest_animation1.json')

    # Verifing the file contents
    with open('server/static/animations/pytest_animation1.json') as animation_file:
        assert data == json.load(animation_file)

    # Cleaning up
    os.remove('server/static/animations/pytest_animation1.json')


def test_animation_invalid(test_client):
    '''
    GIVEN a Flask application
    WHEN the '/traffic-light/animation' route is posted to invalid data (POST)
    THEN check the response is valid

    Parameters:
    -----------
    test_client
        Flask test application

    Returns:
    --------
    None
    '''

    data = {
        "name": "pytest_animation2",
        "invalid": "input data"
    }
    response = test_client.post('/traffic-light/animation',
                                data=json.dumps(data),
                                content_type='application/json')

    # Verifing response
    assert response.status_code == 400
    assert response.data == b'Invalid animation JSON.'
