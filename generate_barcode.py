import barcode
from barcode.writer import ImageWriter
import random

def generate_ean13(
        code,
        output_path,
        format='PNG',
        module_width=0.3,
        module_height=15.0,
        quiet_zone=6.0,
        font_size=10,
        text_distance=5.0,
        background='white',
        foreground='black',
        add_text=True,
        custom_text=None
):


    global ean_code
    if len(code) == 13:
        ean_code = code
    elif len(code) == 12:
        ean_code = code + _calculate_check_digit(code)


    options = {
        'module_width': module_width,
        'module_height': module_height,
        'quiet_zone': quiet_zone,
        'font_size': font_size,
        'text_distance': text_distance,
        'background': background,
        'foreground': foreground,
        'write_text': add_text,
        'text': custom_text if custom_text else ean_code
    }

    if format.upper() in ('PNG', 'JPEG'):
        options['format'] = format.upper()

    ean = barcode.get('ean13', ean_code, writer=ImageWriter())
    filename = ean.save(output_path, options)
    return ean_code

def _calculate_check_digit(code_12):
    sum_odd = sum(int(code_12[i]) for i in range(0, 12, 2))
    sum_even = sum(int(code_12[i]) for i in range(1, 12, 2))
    total = sum_odd + sum_even * 3
    check = (10 - (total % 10)) % 10
    return str(check)

def _is_valid_ean13(code_13):
    if len(code_13) != 13 or not code_13.isdigit():
        return False
    calculated = _calculate_check_digit(code_13[:12])
    return code_13[12] == calculated

def generate_valid_ean12():

    first = random.randint(400, 499)
    second = random.randint(1000, 9999)
    third = random.randint(10000, 99999)
    code_12 = f"{first}{second}{third}"
    return code_12

code_12 = generate_valid_ean12()

filename = generate_ean13(
    code=code_12,
    output_path='barcode_test',
    format='PNG',
    background='white',
    foreground='black'
)
