from enum import Enum

class BaseStatus(Enum):
    def __init__(self, status, http_status_code, message, error_code):
        self.status = status
        self.http_status_code = http_status_code
        self.message = message
        self.error_code = error_code


class MenuSelectStatus(BaseStatus):
    SUCCESS = ("SUCCESS", 200,"메뉴 예약이 완료되었습니다", None)
    ERROR = ("ERROR", 400,"주문하신 수량만큼 재료가 부족합니다", "INSUFFICIENT_INGREDIENTS")
    INVALID_REQUEST = ("ERROR", 400,"요청이 유효하지 않습니다. 누락된 필드를 확인하세요.", "INVALID_REQUEST")
    MENU_NOT_FOUND = ("ERROR", 400,"메뉴가 존재하지 않습니다. 메뉴ID를 확인해주세요.", "MENU_NOT_FOUND")

class OrderCreateStatus(BaseStatus):
    SUCCESS = ("SUCCESS", 200,"주문이 성공적으로 생성되었습니다", None)
    RESERVATION_EXPIRED = ("ERROR", 400,"예약 만료 (5분 초과)", "RESERVATION_EXPIRED")
    INGREDIENTS_EXHAUSTED = ("ERROR", 500,"예약 후 재료 소진", "INGREDIENTS_EXHAUSTED")
    INVALID_RESERVATION = ("ERROR", 400,"유효하지 않은 예약", "INVALID_RESERVATION")


        