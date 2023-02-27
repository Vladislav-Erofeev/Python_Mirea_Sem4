def main(array):
    x = {1997: {
        "OZ": {
            "REXX": 0,
            "ADA": 1,
            "HY": 2
        },
        "SHELL": 3,
        "QMAKE": {
            "REXX": 4,
            "ADA": 5,
            "HY": 6
        }
    },
        1967: {
            "MASK": {
                "REXX": 7,
                "ADA": 8,
                "HY": 9
            },
            "ABAP": 10,
            "PIKE": 11
        },
        1999: 12}

    while not (isinstance(x, int)):
        for i in array:
            if i in x.keys():
                x = x[i]
                break
    return x


print(main(['ABAP', 1999, 'SHELL', 'ADA']))
