import allure
import pytest
from api_test.api.menu_api import MenuSelectApi
from api_test.codes.settings import MenuId, ShopId, MemberNo, CaseType
from api_test.model.dto import MenuSelectReqDto, MenuSelectAssertDto
from api_test.codes.response import MenuSelectStatus
from api_test.model.mock_res import MenuSelectErrorResMock, MenuSelectSucessResMock, MenuSelectInvalidRequestErrorResMock, MenuSelectMenuNotFoundErrorResMock




mark = [pytest.mark.menu_api, pytest.mark.menu, pytest.mark.happy]

@allure.epic("주문 API 테스트")
@allure.feature("메뉴 선택 API 테스트")
@allure.story("시나리오")
class TestMenuAPI:


    @allure.title(f"[메뉴선택][{CaseType.Happy}] 메뉴 선택 성공")
    def test_menu_select_0001(self, f_default_header, mocker):
        # 데이터 설정
        menu_req_dto = MenuSelectReqDto(menu_id=MenuId.valid_menu_id, quantity=2, shop_id=ShopId.valid_shop_id, member_no=MemberNo.valid_member_no)
        menu_assert_dto = MenuSelectAssertDto(status=MenuSelectStatus.SUCCESS)

        # API연결이 되지 않아서 목설정
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectSucessResMock()
        )


        # 호출 
        menu_api = MenuSelectApi(header=f_default_header)
        menu_api.request(menu_req_dto)

        # 테스트
        menu_api.test(menu_assert_dto)

    @allure.title(f"[메뉴선택][{CaseType.Negative}] 재료 부족")
    def test_menu_select_0002(self, f_default_header, mocker):
        # 데이터 설정
        menu_req_dto = MenuSelectReqDto(menu_id=MenuId.valid_menu_id, quantity=1, shop_id=ShopId.valid_shop_id, member_no=MemberNo.valid_member_no)
        menu_assert_dto = MenuSelectAssertDto(status=MenuSelectStatus.ERROR)

        # API연결이 되지 않아서 목설정
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectErrorResMock()
        )


        # 호출 
        menu_api = MenuSelectApi(header=f_default_header)
        menu_api.request(menu_req_dto)

        # 테스트
        menu_api.test(menu_assert_dto)

    @allure.title(f"[메뉴선택][{CaseType.Negative}] 유효하지 않은 인증으로 실패")
    def test_menu_select_0003(self, f_default_header, mocker):
        # 데이터 설정
        menu_req_dto = MenuSelectReqDto(menu_id=MenuId.valid_menu_id, quantity=1, shop_id=ShopId.valid_shop_id, member_no=MemberNo.valid_member_no)
        menu_assert_dto = MenuSelectAssertDto(status=MenuSelectStatus.INVALID_REQUEST)

        # API연결이 되지 않아서 목설정
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectInvalidRequestErrorResMock()
        )

        # 인증 제외
        f_default_header.pop("Authorization")


        # 호출 
        menu_api = MenuSelectApi(header=f_default_header)
        menu_api.request(menu_req_dto)

        # 테스트
        menu_api.test(menu_assert_dto)

    @allure.title(f"[메뉴선택][{CaseType.Negative}] 유효하지 않은 메뉴")
    def test_menu_select_0004(self, f_default_header, mocker):
        # 데이터 설정
        menu_req_dto = MenuSelectReqDto(menu_id=MenuId.valid_menu_id, quantity=1, shop_id=ShopId.valid_shop_id, member_no=MemberNo.valid_member_no)
        menu_assert_dto = MenuSelectAssertDto(status=MenuSelectStatus.MENU_NOT_FOUND)

        # API연결이 되지 않아서 목설정
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectMenuNotFoundErrorResMock()
        )

        # 유효하지 않은 메뉴 설정
        menu_req_dto.menu_id = MenuId.invalid_menu_id

        # 호출 
        menu_api = MenuSelectApi(header=f_default_header)
        menu_api.request(menu_req_dto)

        # 테스트
        menu_api.test(menu_assert_dto)

    @allure.title(f"[메뉴선택][{CaseType.Negative}] 수량 0으로 실패")
    def test_menu_select_0005(self, f_default_header, mocker):
        # 데이터 설정
        menu_req_dto = MenuSelectReqDto(menu_id=MenuId.valid_menu_id, quantity=1, shop_id=ShopId.valid_shop_id, member_no=MemberNo.valid_member_no)
        menu_assert_dto = MenuSelectAssertDto(status=MenuSelectStatus.INVALID_REQUEST)

        # API연결이 되지 않아서 목설정
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectInvalidRequestErrorResMock()
        )

        # 수량 0설정
        menu_req_dto.quantity = 0

        # 호출 
        menu_api = MenuSelectApi(header=f_default_header)
        menu_api.request(menu_req_dto)

        # 테스트
        menu_api.test(menu_assert_dto)

    @allure.title(f"[메뉴선택][{CaseType.Negative}] 수량 음수로 실패")
    def test_menu_select_0006(self, f_default_header, mocker):
        # 데이터 설정
        menu_req_dto = MenuSelectReqDto(menu_id=MenuId.valid_menu_id, quantity=1, shop_id=ShopId.valid_shop_id, member_no=MemberNo.valid_member_no)
        menu_assert_dto = MenuSelectAssertDto(status=MenuSelectStatus.INVALID_REQUEST)

        # API연결이 되지 않아서 목설정
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectInvalidRequestErrorResMock()
        )

        # 수량 0설정
        menu_req_dto.quantity = -1

        # 호출 
        menu_api = MenuSelectApi(header=f_default_header)
        menu_api.request(menu_req_dto)

        # 테스트
        menu_api.test(menu_assert_dto)

    @allure.title(f"[메뉴선택][{CaseType.Negative}] 수량 최대값초과로 실패")
    def test_menu_select_0007(self, f_default_header, mocker):
        # 데이터 설정
        menu_req_dto = MenuSelectReqDto(menu_id=MenuId.valid_menu_id, quantity=1, shop_id=ShopId.valid_shop_id, member_no=MemberNo.valid_member_no)
        menu_assert_dto = MenuSelectAssertDto(status=MenuSelectStatus.INVALID_REQUEST)

        # API연결이 되지 않아서 목설정
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectInvalidRequestErrorResMock()
        )

        # 수량 java int타입 2,147,483,647초과 설정
        menu_req_dto.quantity = 2147483648

        # 호출 
        menu_api = MenuSelectApi(header=f_default_header)
        menu_api.request(menu_req_dto)

        # 테스트
        menu_api.test(menu_assert_dto)

    @allure.title(f"[메뉴선택][{CaseType.Negative}] 존재하지 않은 Shop_id로 실패")
    def test_menu_select_0008(self, f_default_header, mocker):
        # 데이터 설정
        menu_req_dto = MenuSelectReqDto(menu_id=MenuId.valid_menu_id, quantity=1, shop_id=ShopId.valid_shop_id, member_no=MemberNo.valid_member_no)
        menu_assert_dto = MenuSelectAssertDto(status=MenuSelectStatus.INVALID_REQUEST)

        # API연결이 되지 않아서 목설정
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectInvalidRequestErrorResMock()
        )

        # shop_id를 유효하지 않은 값으로 변경
        menu_req_dto.shop_id = ShopId.invalid_shop_id

        # 호출 
        menu_api = MenuSelectApi(header=f_default_header)
        menu_api.request(menu_req_dto)

        # 테스트
        menu_api.test(menu_assert_dto)

    @allure.title(f"[메뉴선택][{CaseType.Negative}] 존재하지 않은 member_no로 실패")
    def test_menu_select_0009(self, f_default_header, mocker):
        # 데이터 설정
        menu_req_dto = MenuSelectReqDto(menu_id=MenuId.valid_menu_id, quantity=1, shop_id=ShopId.valid_shop_id, member_no=MemberNo.valid_member_no)
        menu_assert_dto = MenuSelectAssertDto(status=MenuSelectStatus.INVALID_REQUEST)

        # API연결이 되지 않아서 목설정
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectInvalidRequestErrorResMock()
        )

        # member_no를 유효하지 않은 값으로 변경
        menu_req_dto.member_no = MemberNo.invalid_member_no

        # 호출 
        menu_api = MenuSelectApi(header=f_default_header)
        menu_api.request(menu_req_dto)

        # 테스트
        menu_api.test(menu_assert_dto)

    @allure.title(f"[메뉴선택][{CaseType.Negative}] Menu_id 누락으로 실패")
    def test_menu_select_0010(self, f_default_header, mocker):
        # 데이터 설정
        menu_req_dto = MenuSelectReqDto(menu_id=MenuId.valid_menu_id, quantity=1, shop_id=ShopId.valid_shop_id, member_no=MemberNo.valid_member_no)
        menu_assert_dto = MenuSelectAssertDto(status=MenuSelectStatus.INVALID_REQUEST)

        # API연결이 되지 않아서 목설정
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectInvalidRequestErrorResMock()
        )

        # menu_id 변경
        menu_req_dto.menu_id = None

        # 호출 
        menu_api = MenuSelectApi(header=f_default_header)
        menu_api.request(menu_req_dto)

        # 테스트
        menu_api.test(menu_assert_dto)

    @allure.title(f"[메뉴선택][{CaseType.Negative}] quantity 누락으로 실패")
    def test_menu_select_0011(self, f_default_header, mocker):
        # 데이터 설정
        menu_req_dto = MenuSelectReqDto(menu_id=MenuId.valid_menu_id, quantity=1, shop_id=ShopId.valid_shop_id, member_no=MemberNo.valid_member_no)
        menu_assert_dto = MenuSelectAssertDto(status=MenuSelectStatus.INVALID_REQUEST)

        # API연결이 되지 않아서 목설정
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectInvalidRequestErrorResMock()
        )

        # quantity 변경
        menu_req_dto.quantity = None

        # 호출 
        menu_api = MenuSelectApi(header=f_default_header)
        menu_api.request(menu_req_dto)

        # 테스트
        menu_api.test(menu_assert_dto)

    @allure.title(f"[메뉴선택][{CaseType.Negative}] shop_id 누락으로 실패")
    def test_menu_select_0012(self, f_default_header, mocker):
        # 데이터 설정
        menu_req_dto = MenuSelectReqDto(menu_id=MenuId.valid_menu_id, quantity=1, shop_id=ShopId.valid_shop_id, member_no=MemberNo.valid_member_no)
        menu_assert_dto = MenuSelectAssertDto(status=MenuSelectStatus.INVALID_REQUEST)

        # API연결이 되지 않아서 목설정
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectInvalidRequestErrorResMock()
        )

        # shop_id 변경
        menu_req_dto.shop_id = None

        # 호출 
        menu_api = MenuSelectApi(header=f_default_header)
        menu_api.request(menu_req_dto)

        # 테스트
        menu_api.test(menu_assert_dto)

    @allure.title(f"[메뉴선택][{CaseType.Negative}] member_no 누락으로 실패")
    def test_menu_select_0013(self, f_default_header, mocker):
        # 데이터 설정
        menu_req_dto = MenuSelectReqDto(menu_id=MenuId.valid_menu_id, quantity=1, shop_id=ShopId.valid_shop_id, member_no=MemberNo.valid_member_no)
        menu_assert_dto = MenuSelectAssertDto(status=MenuSelectStatus.INVALID_REQUEST)

        # API연결이 되지 않아서 목설정
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectInvalidRequestErrorResMock()
        )

        # member_no을 변경
        menu_req_dto.member_no = None

        # 호출 
        menu_api = MenuSelectApi(header=f_default_header)
        menu_api.request(menu_req_dto)

        # 테스트
        menu_api.test(menu_assert_dto)

    @allure.title(f"[메뉴선택][{CaseType.Negative}] 탈퇴한 member_no로 실패")
    def test_menu_select_0014(self, f_default_header, mocker):
        # 데이터 설정
        menu_req_dto = MenuSelectReqDto(menu_id=MenuId.valid_menu_id, quantity=1, shop_id=ShopId.valid_shop_id, member_no=MemberNo.valid_member_no)
        menu_assert_dto = MenuSelectAssertDto(status=MenuSelectStatus.INVALID_REQUEST)

        # API연결이 되지 않아서 목설정
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectInvalidRequestErrorResMock()
        )

        # member_no을 변경
        menu_req_dto.member_no = MemberNo.withdrawn_member_no

        # 호출 
        menu_api = MenuSelectApi(header=f_default_header)
        menu_api.request(menu_req_dto)

        # 테스트
        menu_api.test(menu_assert_dto)

    @allure.title(f"[메뉴선택][{CaseType.Negative}] 비활성화된 Shop_id로 실패")
    def test_menu_select_0015(self, f_default_header, mocker):
        # 데이터 설정
        menu_req_dto = MenuSelectReqDto(menu_id=MenuId.valid_menu_id, quantity=1, shop_id=ShopId.valid_shop_id, member_no=MemberNo.valid_member_no)
        menu_assert_dto = MenuSelectAssertDto(status=MenuSelectStatus.INVALID_REQUEST)

        # API연결이 되지 않아서 목설정
        mocker.patch(
            "api_test.core.api_client.requests.request",
            return_value=MenuSelectInvalidRequestErrorResMock()
        )

        # shop_id 변경
        menu_req_dto.shop_id = ShopId.disabled_shop_id

        # 호출 
        menu_api = MenuSelectApi(header=f_default_header)
        menu_api.request(menu_req_dto)

        # 테스트
        menu_api.test(menu_assert_dto)