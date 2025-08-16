from api_test.api.order_api import OrderCreateApi
from api_test.api.menu_api import MenuSelectApi
import allure


class OrderStep:
    
    def __init__(self, header:dict = None):
        self.header = header 
        self.order_api = OrderCreateApi(header=self.header)
        self.menu_api = MenuSelectApi(header=self.header)

    @allure.step("메뉴 선택 API 호출")
    def post_menu_select(self,req_dto, assert_dto):
        self.menu_api.request(req_dto=req_dto)
        self.menu_api.test(assert_dto=assert_dto)
    
    @allure.step("주문 생성 API 호출")
    def post_order_create(self,req_dto, assert_dto):
        self.order_api.request(req_dto=req_dto)
        self.order_api.test(assert_dto=assert_dto)