'''
This file (test_information.py) contains the functional tests for the users blueprint.

These tests use GETs and POSTs to different URLs to check for the proper behavior
of the information blueprint.
'''

import os
import json


def test_status(test_client):
    '''
    GIVEN a Flask application
    WHEN the '/information/status' route is requested (GET)
    THEN check the response is valid

    Parameters:
    -----------
    test_client
        Flask test application.

    Returns:
    --------
    None
    '''

    response = test_client.get('/information/status')

    # Verifing response code
    assert response.status_code == 200

    # Verifing response data
    data = json.loads(response.data.decode("utf-8").replace('\'', '"'))
    anims = [x.split('.')[0] for x in os.listdir('server/static/animations/')]

    # Veifing the status contains valid animation names
    assert ((data['red'] in anims or not data['red']) and
            (data['yellow'] in anims or not data['yellow']) and
            (data['green'] in anims or not data['green']))
