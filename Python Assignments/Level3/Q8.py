import re

def parse(encstr):
    parsed = re.split("0+", encstr)
    res = {}
    res["first_name"] = parsed[0]
    res["last_name"] = parsed[1]
    res["id"] = parsed[2]
    return res


encoded_str = "Robert000Smith000123"
print(parse(encoded_str))