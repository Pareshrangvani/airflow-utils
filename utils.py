import requests


def invoke_http_request(endpoint, method, headers=None, payload=None, json_data=None, timeout=61):
    response = None

    if method == 'GET':
        response = requests.get(url=endpoint, data=payload, timeout=timeout, headers=headers)
    if method == 'POST':
        response = requests.post(url=endpoint, data=payload, json=json_data, timeout=timeout, headers=headers)
    if method == 'PUT':
        response = requests.put(url=endpoint, data=payload, timeout=timeout, headers=headers)
    if method == 'DELETE':
        response = requests.delete(url=endpoint, data=payload, timeout=timeout, headers=headers)

    return response.json(), response.status_code