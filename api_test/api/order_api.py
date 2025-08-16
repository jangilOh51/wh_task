from api_test.api.base_api import BaseAPI
from typing import Dict, Any
from api_test.config.domain import base_url
from api_test.model.dto import OrderCreateReqDto, OrderCreateAssertDto
from api_test.common.data_handler import add_item
import allure


class OrderCreateApi(BaseAPI):

    def __init__(self, header:dict = None):
        api_name = self.__class__.__name__
        super().__init__(api_name, base_url)
        self.header = header if header else {}
        self.body = {}
        self.req_dto = None
        self.endpoint = "/api/v1/order/create"

    def request(self, req_dto:OrderCreateReqDto):
        self.req_dto = req_dto
        add_item(self.body,"reservationId", req_dto.reservation_id)
        add_item(self.body,"memberNo", req_dto.member_no)
        self.client.post(endpoint=self.endpoint, header=self.header, json=self.body)
    
    def assert_success(self, assert_dto:OrderCreateAssertDto):
        res = self.client.response.json()

        # 정상인 경우 추가 항목 검증
        self.asserter.assert_exists(target="timestamp", actual=res.get("timestamp"))
        self.asserter.assert_exists(target="data", actual=res.get("data"))

        # data null일경우 제외
        if assert_dto.data is None:
            return

        # data검증 
        self.asserter.assert_exists(target="data.orderNo", actual=res.get("data", {}).get("orderNo"))
        self.asserter.assert_equal(target="data.orderStatus",expected="INITIALIZING", actual=res.get("data", {}).get("orderStatus"))
        self.asserter.assert_exists(target="data.reservationId", actual=res.get("data", {}).get("reservationId"))
        self.asserter.assert_exists(target="data.createdAt",actual=res.get("data", {}).get("createdAt"))
        self.asserter.assert_equal(target="data.memberInfo.memberNo",expected=self.req_dto.member_no, actual=res.get("data", {}).get("memberInfo", {}).get("memberNo"))