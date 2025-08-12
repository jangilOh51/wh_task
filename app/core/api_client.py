import requests
from typing import Any, Dict, Optional

class ApiClient:
    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None):
        self.base_url = base_url
        self.headers = headers if headers is not None else {}

    def _request(self, method: str, endpoint: str, **kwargs) -> Any:
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
            response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err} - {response.text}")
            raise
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")
            raise
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            print(f"An error occurred: {req_err}")
            raise

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint: str, json: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("POST", endpoint, json=json)

    def put(self, endpoint: str, json: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("PUT", endpoint, json=json)

    def delete(self, endpoint: str) -> Any:
        return self._request("DELETE", endpoint)

# API 타입별 모듈화를 위한 예시 (선택 사항, 필요에 따라 확장)
# class UsersAPI:
#     def __init__(self, client: ApiClient):
#         self.client = client
#
#     def get_user(self, user_id: str) -> Any:
#         return self.client.get(f"users/{user_id}")
#
#     def create_user(self, user_data: Dict[str, Any]) -> Any:
#         return self.client.post("users", json=user_data)
#
# class ProductsAPI:
#     def __init__(self, client: ApiClient):
#         self.client = client
#
#     def get_product(self, product_id: str) -> Any:
#         return self.client.get(f"products/{product_id}")
#
# class MyServiceApiClient(ApiClient):
#     def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None):
#         super().__init__(base_url, headers)
#         self.users = UsersAPI(self)
#         self.products = ProductsAPI(self)
