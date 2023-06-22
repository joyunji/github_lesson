def decimal_to_hex(decimal_num):
    """
    10진수를 16진수 문자열로 변환하는 함수

    Args:
        decimal_num (int): 10진수 정수

    Returns:
        str: 16진수 문자열
    """
    hex_digits = "0123456789abcdef"
    if decimal_num == 0:
        return "0"
    hex_num = ""
    while decimal_num > 0:
        remainder = decimal_num % 16
        hex_digit = hex_digits[remainder]
        hex_num = hex_digit + hex_num
        decimal_num //= 16
    return hex_num
print(decimal_to_hex(10))
print(decimal_to_hex(257))