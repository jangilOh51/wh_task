from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

@dataclass

class Asserter:
    def __init__(self, test_name: str):
        self.test_name = test_name
        self.logs: List[dict] = []

    def assert_equal(self, target: str, expected: Any, actual: Any):
        # 기대결과가 없을 경우 assert를 진행하지 않음
        # None 값을 명시적으로 검증해야 하는 경우, assert_true(target, actual is None) 사용.
        if expected is None:
            return 
        
        assert_log = {
            "type": "equal",
            "target": target,
            "expected": expected,
            "actual": actual,
        }
        self.logs.append(assert_log)
        assert expected == actual, f"대상:{target}, 기대값: {expected}, 실제값: {actual}"

    def assert_exists(self, target: str, actual: Any):
        assert_log = {
            "type": "exists",
            "target": target,
            "actual": actual,
        }
        self.logs.append(assert_log)
        assert actual is not None, f"{target} - 값이 존재하지 않습니다."