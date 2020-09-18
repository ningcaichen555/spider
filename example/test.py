import hashlib


def md5_convert(value):
    try:
        # md5_value = hashlib.md5(b"$value").hexdigest()
        md5_value = hashlib.md5(value.encode('utf-8')).hexdigest()
    except Exception as e:
        md5_value = 0
    return md5_value


def title_convert(value):
    try:
        if (len(value) >= 50):
            value = value[0:49]
    except Exception as e:
        value
    return value


print(md5_convert("1234"))
print(md5_convert("7887578-2c6f081ccceac788"))
