from api_test.core.api_client import ApiClient
from api_test.model.dto import BaseAssertDto
from api_test.model.assert_model import Asserter
from abc import ABC, abstractmethod
from api_test.model.add_api_res_report import api_info_on_report
from api_test.common.data_handler import add_item





class BaseAPI(ABC):
    def __init__(self,api_name:str, base_url: str):
        self.api_name = api_name
        self.client = ApiClient(base_url=base_url)
        self.asserter = Asserter(test_name=api_name)
        self.body = None


    @api_info_on_report
    def test(self, assert_dto:BaseAssertDto):
        actual_res = self.client.response.json()
        self.asserter.assert_equal(target="http_status_code", expected=assert_dto.status.http_status_code, actual=self.client.response.status_code)
        self.asserter.assert_equal(target="status", expected=assert_dto.status.status, actual=actual_res.get("status"))
        self.asserter.assert_equal(target="message", expected=assert_dto.status.message,actual=actual_res.get("message"))
        if assert_dto.status.http_status_code != 200:
            self.asserter.assert_equal(target="error_code", expected=assert_dto.status.error_code, actual=actual_res.get("errorCode"))
        else:
            self.assert_success(assert_dto)

    @abstractmethod
    def assert_success(self, assert_dto: BaseAssertDto):
        pass

    def get_api_info(self):
        api_info = {
            "api_name": self.api_name,
            "response_status_code": self.client.response.status_code,
            "response_body": self.client.response.json(),
            "response_headers": self.client.response.headers,
        }
        add_item(api_info, "req_body",self.body)
        add_item(api_info, "response_status_code",self.client.response.status_code)
        add_item(api_info, "response_headers",self.client.response.headers)
        add_item(api_info, "response_body",self.client.response.json())
        add_item(api_info, "assertion",self.asserter.logs)

        return api_info






