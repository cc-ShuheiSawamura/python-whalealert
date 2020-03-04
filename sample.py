
import config
import requests


"""
API rate limiting is dependent on your plan. 
For the free plan the number of requests is limited to 10 per minute. 
The personal plan has a rate limit of 60 per minute. 
If you need more requests, please contact us for an Enterprise account.
"""



key = config.api_key
url = 'https://api.whale-alert.io/v1'

def post(endpoint, **params):
    params['api_key'] = key
    print(params)
    res = requests.get(url+endpoint, params=params)
    print(res.text)
    return res


post('/status', params={'a':5})