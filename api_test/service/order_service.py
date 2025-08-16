import allure
from api_test.service.step.order_step import OrderStep
from api_test.model.dto import *
from api_test.model.mock_res import *
import time



class OrderService:
    def __init__(self, header:dict = None):
        self.header = header 
        self.order_step = OrderStep(header=self.header)


    @allure.step("주문 요청")
    def create_order(self, mocker, member_no:str, menu_id:str, quantity:int, shop_id:str):
        # 메뉴 선택
        # API연결이 되지 않아서 목설정
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectSucessResMock()
        )
        reservation_id = self.post_menu_select(member_no, menu_id, quantity, shop_id)
        
        # 주문 생성
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=OrderCreateSucessResMock()
        )

        self.post_order_create(member_no, reservation_id)
        



    def post_menu_select(self,member_no:str, menu_id:str, quantity:int, shop_id:str):
        # 메뉴 조회 API 호출
        menu_req_dto = MenuSelectReqDto(menu_id=menu_id, quantity=quantity, shop_id=shop_id, member_no=member_no)
        menu_assert_dto = MenuSelectAssertDto(status=MenuSelectStatus.SUCCESS)
        self.order_step.post_menu_select(req_dto=menu_req_dto, assert_dto=menu_assert_dto)

        return self.order_step.menu_api.client.response.json().get("data").get("reservationId")
    
    def post_order_create(self, member_no:str, reservation_id:str):
        # 주문 생성 API 호출
        order_create_req_dto = OrderCreateReqDto(reservation_id=reservation_id, member_no=member_no)
        order_create_assert_dto = OrderCreateAssertDto(status=OrderCreateStatus.SUCCESS)
        self.order_step.post_order_create(req_dto=order_create_req_dto, assert_dto=order_create_assert_dto)




