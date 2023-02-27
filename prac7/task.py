def main(x):
    bin_number = bin(x)
    bin_number = "0" * (27 - len(bin_number[2::])) + bin_number[2::]
    bin_number = bin_number[::-1]
    u1 = hex(int(bin_number[:9][::-1], 2))
    u2 = hex(int(bin_number[9:17][::-1], 2))
    u3 = hex(int(bin_number[17:26][::-1], 2))
    u4 = hex(int(bin_number[26:][::-1], 2))
    return {"U1": u1,
            "U2": u2,
            "U3": u3,
            "U4": u4}

print(main(51304280))