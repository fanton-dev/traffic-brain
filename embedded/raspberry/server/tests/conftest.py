'''
Module containing pretest fixtures.

This module contains the following pretest fixtures:
    - test_client
        Starts a testing instance of the server.
'''

import pytest
from server import create_app


@pytest.fixture(scope='module')
def test_client():
    '''
    Starts a testing instance of the server.

    Parameters:
    -----------
    None.

    Returns:
    --------
    Flask test client generator.
    '''

    flask_app = create_app(config='flask_test.cfg')

    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()

    # The test genrator
    yield testing_client

    ctx.pop()
