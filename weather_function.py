def unpack_data(inc_data):
    dep_data = inc_data.split()
    dep_data[1] = float(dep_data[1])
    dec_data = {dep_data[0]: dep_data[1]}
    return dec_data

def media_data(dict0, dict1, dict2):
    media_temp = ((dict0.get("T:")) + (dict1.get("T:")) + (dict2.get("T:")))/3
    media_umi = ((dict0.get("L:")) + (dict1.get("L:")) + (dict2.get("L:")))/3
    media_lum = ((dict0.get("U:")) + (dict1.get("U:")) + (dict2.get("U:")))/3
    return media_lum, media_temp, media_umi


def avg_list(list):
    avg_list = (sum(list))/len(list)
    avg_list_out = float(format(avg_list, '.2f'))
    return avg_list_out


def decode_format(data):
    decode_data = data.decode("utf-8")
    out_data = decode_data[0:][:-2]
    return out_data



