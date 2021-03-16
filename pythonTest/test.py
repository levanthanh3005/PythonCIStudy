import requests

def test_github_api():
    """
    Asserts current_user_url is a key in the base Github API GET result JSON
    """
    print("\ntest_github_api")
    json = requests.get('https://api.github.com/').json()
    assert('current_user_url' in json.keys())

def test_hello():
    """
    Asserts current_user_url is a key in the base Github API GET result JSON
    """
    print("\ntest_hello")
    text = requests.get('http://0.0.0.0:5000').text
    # print(text)
    assert(text == 'Hello Python')

def test_hello_2():
    """
    Asserts current_user_url is a key in the base Github API GET result JSON
    """
    print("\ntest_hello_2")
    text = requests.get('http://0.0.0.0:5000/hello2').text
    # print(text)
    assert(text == 'Hello Python 2')

def test_get_params():
    """
    Asserts current_user_url is a key in the base Github API GET result JSON
    """
    print("\ntest_get_params")
    text = requests.get('http://0.0.0.0:5000/getparams/1').text
    # print(text)
    assert(text == 'Hello 1')

# test_hello();