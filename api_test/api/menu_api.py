from api_test.api.base_api import BaseAPI
from typing import Dict, Any
from api_test.config.domain import base_url
from api_test.model.dto import MenuSelectReqDto, MenuSelectAssertDto
from api_test.common.data_handler import dto_to_camel_case_dict
import allure


class MenuSelectApi(BaseAPI):

    def __init__(self, header:dict = None):
        api_name = self.__class__.__name__
        super().__init__(api_name, base_url)
        self.header = header if header else {}
        self.body = {}
        self.req_dto = None
        self.endpoint = "/api/v1/menu/select"

    def request(self, req_dto:MenuSelectReqDto):
        self.req_dto = req_dto
        self.body = dto_to_camel_case_dict(req_dto)
        self.client.post(endpoint=self.endpoint, header=self.header, json=self.body)

    def assert_success(self, assert_dto:MenuSelectAssertDto):
        res = self.client.response.json()

        # 정상인 경우 추가 항목 검증
        self.asserter.assert_exists(target="timestamp", actual=res.get("timestamp"))
        self.asserter.assert_exists(target="data", actual=res.get("data"))

        # data검증 
        self.asserter.assert_exists(target="data.reservationId", actual=res.get("data").get("reservationId"))
        self.asserter.assert_exists(target="data.reservationExpiresAt", actual=res.get("data").get("reservationExpiresAt"))
        self.asserter.assert_equal(target="data.menuId",expected=self.req_dto.menu_id, actual=res.get("data").get("menuId"))
        self.asserter.assert_equal(target="data.quantity",expected=self.req_dto.quantity, actual=res.get("data").get("quantity"))




