from dataclasses import dataclass
from api_test.codes.response import MenuSelectStatus, BaseStatus, OrderCreateStatus



# =====================Request Dto ====================

@dataclass
class MenuSelectReqDto:
    menu_id:str
    quantity:int
    shop_id:str
    member_no:str

@dataclass
class OrderCreateReqDto:
    reservation_id:str
    member_no:str


# =======================Assert Dto  ====================

class BaseAssertDto:
    status:BaseStatus

@dataclass
class MenuSelectAssertDto(BaseAssertDto):
    status:MenuSelectStatus
    timestamp:str = None
    data:dict = None


@dataclass
class OrderCreateAssertDto(BaseAssertDto):
    status:OrderCreateStatus
    timestamp:str = None
    data:dict = None
