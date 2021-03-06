import requests

# competitions
# teams


def fs_do(resource, filter=''):
    proxies = {}
    baseurl = "http://api.football-data.org/v2/"
    url = baseurl + resource
    if filter != '':
        url = url + '?' + filter
    headers = {
        'x-auth-token': "fe665f6a41fc41ab90296923a87df47b",
        'cache-control': "no-cache",
    }

    try:
        response = requests.request("GET", url, headers=headers)
    except requests.exceptions.ConnectionError:
        response = requests.request(
            "GET", url, headers=headers, proxies=proxies)

    # print(response.text)
    # test
    return response.json()
