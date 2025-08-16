from dataclasses import asdict, is_dataclass

def to_camel_case(snake_str: str) -> str:
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def dto_to_camel_case_dict(dto) -> dict:
    if not is_dataclass(dto):
        raise TypeError("dto_to_camel_case_dict() only accepts dataclasses")
    
    dto_dict = asdict(dto)
    
    camel_case_dict = {}
    for k, v in dto_dict.items():
        if v is not None:
            camel_case_dict[to_camel_case(k)] = v
            
    return camel_case_dict

def add_item(target:dict, item_name:str, item_value):
    if item_value is not None:
        target[item_name] = item_value