def median(datas):
    length = len(datas)
    if (length % 2) == 0:
        m = int(length / 2)
        result = datas[m]
    else:
        m = int(float(length / 2) - 0.5)
        result = datas[m]
    return result
