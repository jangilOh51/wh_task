import allure
import pytest
from api_test.api.order_api import OrderCreateApi
from api_test.codes.settings import MenuId, ShopId, MemberNo, CaseType, ReservationId
from api_test.model.dto import OrderCreateAssertDto, OrderCreateReqDto
from api_test.codes.response import MenuSelectStatus
from api_test.model.mock_res import OrderCreateIngredientsExhaustedResMock, OrderCreateInvalidReservationResMock, OrderCreateReservationExpiredResMock, OrderCreateSucessResMock
from api_test.service.order_service import OrderService
from api_test.model.mock_res import *
from api_test.model.dto import *





mark = [pytest.mark.menu_api, pytest.mark.menu, pytest.mark.happy]

@allure.epic("주문 API 테스트")
@allure.feature("주문 생성 API 테스트")
@allure.story("시나리오")
class TestOrderCreateAPI:


    @allure.title(f"[주문생성][{CaseType.Happy}] 주문 생성 성공")
    def test_order_create_0001(self, f_default_header, mocker):

        order_svc = OrderService(header=f_default_header)
        order_svc.create_order(mocker, member_no=MemberNo.valid_member_no, menu_id=MenuId.valid_menu_id, quantity=2, shop_id=ShopId.valid_shop_id)


    @allure.title(f"[주문생성][{CaseType.Negative}] 메뉴선택과 주문 생성의 멤버정보가 달라서 실패")
    def test_order_create_0002(self, f_default_header, mocker):
        order_svc = OrderService(header=f_default_header)
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectSucessResMock()
        )
        reservation_id = order_svc.post_menu_select(member_no=MemberNo.valid_member_no, menu_id=MenuId.valid_menu_id, quantity=2, shop_id=ShopId.valid_shop_id)

        # 주문생성시 멤버를 예약할때와 다른 멤버로 전송
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=OrderCreateInvalidReservationResMock()
        )
        order_create_req_dto = OrderCreateReqDto(reservation_id=reservation_id, member_no=MemberNo.invalid_member_no)
        order_create_assert_dto = OrderCreateAssertDto(status=OrderCreateStatus.INVALID_RESERVATION)
        order_svc.order_step.post_order_create(req_dto=order_create_req_dto, assert_dto=order_create_assert_dto)


    @allure.title(f"[주문생성][{CaseType.Negative}] reservationId가 유효하지 않아서 실패")
    def test_order_create_0003(self, f_default_header, mocker):
        order_svc = OrderService(header=f_default_header)
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectSucessResMock()
        )
        order_svc.post_menu_select( member_no=MemberNo.valid_member_no, menu_id=MenuId.valid_menu_id, quantity=2, shop_id=ShopId.valid_shop_id)

        # 유효하지 않은 reservation_id 사용
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=OrderCreateInvalidReservationResMock()
        )
        order_create_req_dto = OrderCreateReqDto(reservation_id=ReservationId.invalid_reservation_id, member_no=MemberNo.valid_member_no)
        order_create_assert_dto = OrderCreateAssertDto(status=OrderCreateStatus.INVALID_RESERVATION)
        order_svc.order_step.post_order_create(req_dto=order_create_req_dto, assert_dto=order_create_assert_dto)

    @allure.title(f"[주문생성][{CaseType.Negative}] 유효하지 않은 인증으로 실패")
    def test_order_create_0004(self, f_default_header, mocker):
        order_svc = OrderService(header=f_default_header)
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectSucessResMock()
        )
        reservation_id = order_svc.post_menu_select( member_no=MemberNo.valid_member_no, menu_id=MenuId.valid_menu_id, quantity=2, shop_id=ShopId.valid_shop_id)

        # 유효하지 않은 인증
        f_default_header.pop("Authorization")
        order_svc = OrderService(header=f_default_header)

        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=OrderCreateInvalidReservationResMock()
        )
        order_create_req_dto = OrderCreateReqDto(reservation_id=reservation_id, member_no=MemberNo.valid_member_no)
        order_create_assert_dto = OrderCreateAssertDto(status=OrderCreateStatus.INVALID_RESERVATION)
        order_svc.order_step.post_order_create(req_dto=order_create_req_dto, assert_dto=order_create_assert_dto)

    @allure.title(f"[주문생성][{CaseType.Negative}] reservationId 누락으로 실패")
    def test_order_create_0005(self, f_default_header, mocker):
        order_svc = OrderService(header=f_default_header)
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectSucessResMock()
        )
        reservation_id = order_svc.post_menu_select(member_no=MemberNo.valid_member_no, menu_id=MenuId.valid_menu_id, quantity=2, shop_id=ShopId.valid_shop_id)

        # reservationId 누락
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=OrderCreateInvalidReservationResMock()
        )
        order_create_req_dto = OrderCreateReqDto(reservation_id=None, member_no=MemberNo.valid_member_no)
        order_create_assert_dto = OrderCreateAssertDto(status=OrderCreateStatus.INVALID_RESERVATION)
        order_svc.order_step.post_order_create(req_dto=order_create_req_dto, assert_dto=order_create_assert_dto)


    @allure.title(f"[주문생성][{CaseType.Negative}] MemeberNo 누락으로 실패")
    def test_order_create_0006(self, f_default_header, mocker):
        order_svc = OrderService(header=f_default_header)
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectSucessResMock()
        )
        reservation_id = order_svc.post_menu_select(member_no=MemberNo.valid_member_no, menu_id=MenuId.valid_menu_id, quantity=2, shop_id=ShopId.valid_shop_id)

        # 주문생성
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=OrderCreateInvalidReservationResMock()
        )
        order_create_req_dto = OrderCreateReqDto(reservation_id=reservation_id, member_no=None)
        order_create_assert_dto = OrderCreateAssertDto(status=OrderCreateStatus.INVALID_RESERVATION)
        order_svc.order_step.post_order_create(req_dto=order_create_req_dto, assert_dto=order_create_assert_dto)


    @allure.title(f"[주문생성][{CaseType.Negative}] 예약후 5분 초기로 실패")
    def test_order_create_0007(self, f_default_header, mocker):
        order_svc = OrderService(header=f_default_header)
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectSucessResMock()
        )
        reservation_id = order_svc.post_menu_select(member_no=MemberNo.valid_member_no, menu_id=MenuId.valid_menu_id, quantity=2, shop_id=ShopId.valid_shop_id)

        # 여기서 5분 대기하고 호출해야 하지만 목서버 사용으로 대기는 하지 않음.
        # 상황에 따라서는 DB에 미리 등록하고 사용하는 것이 더 좋을 수도 있다고 생각합니다.
        # time.sleep(300)
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=OrderCreateReservationExpiredResMock()
        )
        order_create_req_dto = OrderCreateReqDto(reservation_id=reservation_id, member_no=MemberNo.valid_member_no)
        order_create_assert_dto = OrderCreateAssertDto(status=OrderCreateStatus.RESERVATION_EXPIRED)
        order_svc.order_step.post_order_create(req_dto=order_create_req_dto, assert_dto=order_create_assert_dto)


    @allure.title(f"[주문생성][{CaseType.Negative}] 예약후 재료소진으로 실패")
    def test_order_create_0008(self, f_default_header, mocker):
        order_svc = OrderService(header=f_default_header)
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectSucessResMock()
        )
        reservation_id = order_svc.post_menu_select(member_no=MemberNo.valid_member_no, menu_id=MenuId.valid_menu_id, quantity=2, shop_id=ShopId.valid_shop_id)

        # 주문생성
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=OrderCreateIngredientsExhaustedResMock()
        )
        order_create_req_dto = OrderCreateReqDto(reservation_id=reservation_id, member_no=MemberNo.valid_member_no)
        order_create_assert_dto = OrderCreateAssertDto(status=OrderCreateStatus.INGREDIENTS_EXHAUSTED)
        order_svc.order_step.post_order_create(req_dto=order_create_req_dto, assert_dto=order_create_assert_dto)