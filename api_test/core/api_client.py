import requests
from typing import Any, Dict, Optional
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.response = None

    def _log_request(self, method: str, endpoint: str, headers: dict, **kwargs) -> None:
        logging.info(f"Request Method: {method}")
        logging.info(f"Request URL: {self.base_url}{endpoint}")
        logging.info(f"Request Headers: {headers}")
        if 'json' in kwargs:
            logging.info(f"Request Body: {kwargs['json']}")

    def _log_response(self) -> None:
        if self.response is not None:
            logging.info(f"Response Status: {self.response.status_code}")
            logging.info(f"Response Headers: {self.response.headers}")
            try:
                logging.info(f"Response Body: {self.response.json()}")
            except requests.exceptions.JSONDecodeError:
                logging.info(f"Response Body: {self.response.text}")

    def _request(self, method: str, endpoint: str, header:dict, **kwargs) -> None:
        self.url = f"{self.base_url}{endpoint}"
        self._log_request(method, endpoint, header, **kwargs)
        try:
            self.response = requests.request(method, self.url, headers=header, **kwargs)
            self._log_response()
            self.response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err} - {self.response.text if self.response else 'No response'}")
            raise
        except requests.exceptions.ConnectionError as conn_err:
            logging.error(f"Connection error occurred: {conn_err}")
            raise
        except requests.exceptions.Timeout as timeout_err:
            logging.error(f"Timeout error occurred: {timeout_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            logging.error(f"An error occurred: {req_err}")
            raise

    def get(self, endpoint: str, header:dict, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        self._request("GET", endpoint, header, params=params)
        return self.response

    def post(self, endpoint: str, header:dict, json: Optional[Dict[str, Any]] = None) -> requests.Response:
        self._request("POST", endpoint,header, json=json)
        return self.response

    def put(self, endpoint: str,header:dict, json: Optional[Dict[str, Any]] = None) -> requests.Response:
        self._request("PUT", endpoint,header, json=json)
        return self.response

    def delete(self, endpoint: str, header:dict) -> requests.Response:
        self._request("DELETE", endpoint,header)
        return self.response

    def patch(self, endpoint: str, header:dict, json: Optional[Dict[str, Any]] = None) -> requests.Response:
        self._request("PATCH", endpoint,header, json=json)
        return self.response