from time import process_time

symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127

def clock(label, cmd):
    start_time = process_time()
    for i in range(100000):
        eval(cmd)
    end_time = process_time()
    print(label + f"ellapsed {end_time-start_time} sec")

clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')