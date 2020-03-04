# _*_coding:utf-8_*_

import requests


"""
API rate limiting is dependent on your plan. 
For the free plan the number of requests is limited to 10 per minute. 
The personal plan has a rate limit of 60 per minute. 
If you need more requests, please contact us for an Enterprise account.
"""


class API(object):

    url = 'https://api.whale-alert.io/v1'

    def __init__(self, key):
        self.key = key

    def post(self, endpoint, params={}):
        params['api_key'] = self.key
        res = requests.get(self.url+endpoint, params=params)
        return res.json()

    def status(self):
        res = self.post('/status')
        return res

    def transaction(self, params={}):
        """
        Parameter	Type	Description
        blockchain	string	The blockchain to search for the specific hash (lowercase)
        hash	string	The hash of the transaction to return
        Please note that a single hash can return multiple transaction
        """
        res = self.post('/transaction', params=params)
        return res

    def transactions(self, start, params={}):
        """
        Parameter	Type	Description
        start	int	(Required) Unix timestamp for retrieving transactions from timestamp (exclusive). Retrieves transactions based on their execution time on the blockchain.
        end	int	Unix timestamp for retrieving transactions until timestamp (inclusive).
        cursor	int	Pagination key from the previous response. Recommended when retrieving transactions in intervals.
        min_value	int	Minimum USD value of transactions returned (value at time of transaction). Allowed minimum value varies per plan ($500k for Free, $100k for Personal).
        limit	int	Maximum number of results returned. Default 100, max 100.
        currency	string	Returns transactions for a specific currency code. Returns all currencies by default.
        """
        params['start'] = start
        res = self.post('/transactions', params=params)
        return res


if __name__ == "__main__":
    import config
    from time import time
    api = API(config.api_key)
    res = api.transactions(int(time()-3500))
    print(res)