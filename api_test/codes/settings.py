from enum import StrEnum

class MenuId(StrEnum):
    valid_menu_id = "menu_001"
    invalid_menu_id = "2"

class ShopId(StrEnum):
    valid_shop_id = "1"
    invalid_shop_id = "2"
    disabled_shop_id = "3"

class MemberNo(StrEnum):
    valid_member_no = "1"
    invalid_member_no = "2"
    withdrawn_member_no = "3"


class CaseType(StrEnum):
    Happy = "Happy"
    Negative = "Negative"

class ReservationId(StrEnum):
    valid_reservation_id = "RSV_A7K9M2X8"
    invalid_reservation_id = "invalid_reservation_id"

