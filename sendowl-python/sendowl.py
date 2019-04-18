import requests
from typing import List, Dict, Union


class SendOwl:
	def __init__(self, key: str = None, secret: str = None):
		self._key = key
		self._secret = secret

		self._baseUrl = f"https://{self._key}:{self._secret}@www.sendowl.com/api/v1/"

	def _apiRequest(self, method: str, path: str, params: Dict[str, str] = None) -> Union[List, Dict]:
		method = method.lower()
		url = f'{self._baseUrl}{path}'
		if method == 'get':
			if params:
				req = requests.get(path, params=params)
			else:
				req = requests.get(path)
		elif method == 'post':
			req = requests.post(url, data=params)
		elif method == 'put':
			req = requests.put(url, data=params)
		elif method == 'delete':
			req = requests.delete(url)
		else:
			raise ValueError(f'Invalid request method "{method}"')
		return req.json()

	def get_products(self) -> Union[List, Dict]:
		return self._apiRequest('get', 'products')

	def search_products(self, term: str) -> Union[List, Dict]:
		return self._apiRequest('get', 'products/search', {'term': term})

	def shopify_lookup_product(self, variant_id: str) -> Union[List, Dict]:
		return self._apiRequest('get', 'products/shopify_lookup', {'variant_id': variant_id})

	def get_product(self, product_id: Union[int, str]) -> Union[List, Dict]:
		return self._apiRequest('get', f'products/{product_id}')

	def new_product(self, product: Dict) -> Union[List, Dict]:
		return self._apiRequest('post', 'products', product)

	def update_product(self, product_id: Union[int, str], product_updates: Dict) -> Union[List, Dict]:
		return self._apiRequest('put', f'products/{product_id}', product_updates)

	def delete_product(self, product_id: Union[int, str]) -> Union[List, Dict]:
		return self._apiRequest('delete', f'products/{product_id}')

	def issue_product_order(self, product_id: Union[int, str], issue_details: Dict) -> Union[List, Dict]:
		return self._apiRequest('post', f'products/{product_id}/issue', issue_details)


