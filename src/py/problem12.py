from util import cartesian_factors, triangulate

def problem12():
    # 25158721770
    start_threshold = 25158721770
    for answer in triangulate(start_threshold):
        cart = cartesian_factors(answer[0], answer[1])
        # print(f"N:{answer[0]}: carts: {cart}")
        if len(cart[1]) > 300: print(f"N:{answer[0]}: cartlen: {len(cart[1])}")


problem12()
