def unpack_data(inc_data):
    dep_data = inc_data.split()
    dec_data = {dep_data[0]: float(dep_data[1])}
    return dec_data

