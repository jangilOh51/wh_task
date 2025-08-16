import json
import functools
import allure

def api_info_on_report(func):
    """
    API 응답을 Allure 리포트에 JSON 형식으로 첨부하는 데코레이터.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        try:
            json_data = args[0].get_api_info()
            
            allure.attach(
                json.dumps(json_data, indent=4, ensure_ascii=False),
                name="API Response",
                attachment_type=allure.attachment_type.JSON
            )
        except Exception as e:
            allure.attach(
                f"Failed to attach JSON response: {e}\nRaw response: {response}",
                name="API Response Error",
                attachment_type=allure.attachment_type.TEXT
            )
        return response
    return wrapper
