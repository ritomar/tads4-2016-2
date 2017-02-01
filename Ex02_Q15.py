def udc(cdu):
    u = cdu % 10
    cdu = cdu // 10
    d = cdu % 10
    cdu = cdu // 10
    c = cdu % 10
    return (u * 100) + (d * 10) + c

print(udc(123))
