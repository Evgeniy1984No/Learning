# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
# representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
# must be rounded to the closest valid value.
#
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
#
# Examples (input --> output):
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"

def rgb(r, g, b):
    # your code here :)
    # cache = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    # print(cache)
    # h = []
    # for i in [r, g, b]:
    #     if i < 0:
    #         h.append((0, 0))
    #     elif i > 255:
    #         h.append((15, 15))
    #     else:
    #         h.append(divmod(i, 16))
    # print(h)
    # return ''.join(map(lambda elem: cache[elem[0]] + cache[elem[1]], h))
    #

    h = lambda x: min(255, max(x, 0))
    print(h(r), h(g), h(b))
    return ("{:02X}" * 3).format(h(r), h(g), h(b))

print(rgb(-20, 275, 125))
