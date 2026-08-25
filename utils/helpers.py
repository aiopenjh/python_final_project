def validate_input(user_input, field_name):
    cleaned = user_input.strip()
    if cleaned == "":
        raise ValueError(F"'{field_name}'은 빈칸으로 둘수 없습니다")
    return cleaned

