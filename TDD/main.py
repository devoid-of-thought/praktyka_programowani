import re
def Add(num_str):
    num_str = num_str.replace('\n',',')
    if not isinstance(num_str, str):
        return ValueError
    if num_str.strip() ==1 and num_str.strip("").isnumeric() :
        return int(num_str.strip(" "))
    if len(re.findall("\d+", num_str))!=1+len(re.findall(",", num_str)):
        return ValueError
    valid = num_str.replace(' ', '')
    if len(valid.split(",")) ==1:
        return int(valid)

    split = valid.split(",")
    if len(split) >= 2:
        result = 0
        for i in split:
            result += int(i)
        return result


