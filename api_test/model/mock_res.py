class MenuSelectSucessResMock:
    def json(self):
        res = {
                "status": "SUCCESS",
                "message": "메뉴 예약이 완료되었습니다",
                "timestamp": "2025-08-07T12:30:00.123Z",
                "data": {
                "reservationId": "RSV_A7K9M2X8",
                "reservationExpiresAt": "2025-08-07T12:35:00.123Z",
                "menuId": "menu_001",
                "quantity": 2
                }
        }       
        return res

    @property
    def status_code(self):
        return 200
    
    @property
    def headers(self):
        return { "Content-Type": "application/json;charset=UTF-8"}
    
    def raise_for_status(self):
        pass 

class MenuSelectErrorResMock:
    def json(self):
        res =  {
            "status": "ERROR","message": "주문하신 수량만큼 재료가 부족합니다",
            "errorCode": "INSUFFICIENT_INGREDIENTS",
            "timestamp": "2025-08-07T12:30:00.123Z"
            }
    
        return res

    @property
    def status_code(self):
        return 400
    
    @property
    def headers(self):
        return { "Content-Type": "application/json;charset=UTF-8"}
    
    def raise_for_status(self):
        pass  

class MenuSelectInvalidRequestErrorResMock:
    def json(self):
        res =  {
            "status": "ERROR","message": "요청이 유효하지 않습니다. 누락된 필드를 확인하세요.",
            "errorCode": "INVALID_REQUEST",
            "timestamp": "2025-08-07T12:30:00.123Z"
            }
    
        return res

    @property
    def status_code(self):
        return 400
    
    @property
    def headers(self):
        return { "Content-Type": "application/json;charset=UTF-8"}
    
    def raise_for_status(self):
        pass 

class MenuSelectMenuNotFoundErrorResMock:
    def json(self):
        res =  {
            "status": "ERROR","message": "메뉴가 존재하지 않습니다. 메뉴ID를 확인해주세요.",
            "errorCode": "MENU_NOT_FOUND",
            "timestamp": "2025-08-07T12:30:00.123Z"
            }
    
        return res

    @property
    def status_code(self):
        return 400
    
    @property
    def headers(self):
        return { "Content-Type": "application/json;charset=UTF-8"}
    
    def raise_for_status(self):
        pass 


class OrderCreateSucessResMock:
    def json(self):
        res = {
            "status": "SUCCESS",
            "message": "주문이 성공적으로 생성되었습니다",
            "timestamp": "2025-08-07T12:30:00.123Z",
            "data": {
                "orderNo": "R7X9K2M8",
                "orderStatus": "INITIALIZING",
                "reservationId": "RSV_A7K9M2X8",
                "createdAt": "2025-08-07T12:30:00.123Z",
                "memberInfo": {"memberNo": "member_123"}
            }
        }
        return res

    @property
    def status_code(self):
        return 200
    
    @property
    def headers(self):
        return { "Content-Type": "application/json;charset=UTF-8"}
    
    def raise_for_status(self):
        pass 

class OrderCreateReservationExpiredResMock:
    def json(self):
        res = {
            "status": "ERROR","message": "예약 만료 (5분 초과)",
            "errorCode": "RESERVATION_EXPIRED",
            "timestamp": "2025-08-07T12:30:00.123Z"
            }
        return res

    @property
    def status_code(self):
        return 400
    
    @property
    def headers(self):
        return { "Content-Type": "application/json;charset=UTF-8"}
    
    def raise_for_status(self):
        pass 

class OrderCreateIngredientsExhaustedResMock:
    def json(self):
        res = {
            "status": "ERROR","message": "예약 후 재료 소진",
            "errorCode": "INGREDIENTS_EXHAUSTED",
            "timestamp": "2025-08-07T12:30:00.123Z"
            }
        return res

    @property
    def status_code(self):
        return 500
    
    @property
    def headers(self):
        return { "Content-Type": "application/json;charset=UTF-8"}
    
    def raise_for_status(self):
        pass 

class OrderCreateInvalidReservationResMock:
    def json(self):
        res = {
            "status": "ERROR","message": "유효하지 않은 예약",
            "errorCode": "INVALID_RESERVATION",
            "timestamp": "2025-08-07T12:30:00.123Z"
            }
        return res

    @property
    def status_code(self):
        return 400
    
    @property
    def headers(self):
        return { "Content-Type": "application/json;charset=UTF-8"}
    
    def raise_for_status(self):
        pass 