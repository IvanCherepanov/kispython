from pprint import pprint 

from struct import unpack


type_dict = {
    "int8": "b",
    "uint8": "B",
    "int16": "h",
    "uint16": "H",
    "int32": "i",
    "uint32": "I",
    "int64": "q",
    "uint64": "Q",
    "float": "f",
    "double": "d",
    "char[]": "s",
}


def gen_d():
    d = type_dict

    return (
        d["int8"] + d["uint16"] + d["double"] + 6 * d["uint16"] +
        d["uint8"] + d["uint8"] + d["uint32"] + d["uint16"]
    )


def gen_c():
    d = type_dict

    return d["uint8"] + d["float"] + d["int8"] + d["int64"] +\
    d["uint16"] + d["uint16"]


def gen_b():
    d = type_dict

    return gen_c() + d["int16"] + d["int8"] + d["float"] +\
    d["uint32"] + d["uint32"]


def gen_a():
    d = type_dict

    return gen_b() + d["int8"] + d["uint64"] +\
    d["uint16"] + d["uint32"] + d["int64"]


def gen_total():
    d = type_dict

    return ">xxx" + gen_a()  # "<" + 4 * d["char[]"] +


def main(arg):
    d = type_dict

    total = gen_total()

    obj = unpack(total, arg[:59])

    a_dict = {
        "A1": {
            "B1": {
                "C1": obj[0],
                "C2": obj[1],
                "C3": obj[2],
                "C4": obj[3],
                "C5": [],  # 4-5
            },
            "B2": obj[6],
            "B3": obj[7],
            "B4": obj[8],
            "B5": [],  # 9-10
        },
        "A2": obj[11],
        "A3": obj[12],
        "A4": [],  # 13-14
        "A5": obj[15],
    }

    first_c_struct_c5_size = obj[4]
    first_c_struct_c5_addr = obj[5]

    first_c_struct_c5_total = ">" + first_c_struct_c5_size * gen_d()

    first_c_struct_c5 = unpack(
        first_c_struct_c5_total,
        arg[first_c_struct_c5_addr: first_c_struct_c5_addr + 62]
    )

    second_c5_struct_c7_size = first_c_struct_c5[11]
    second_c5_struct_c7_addr = first_c_struct_c5[12]

    second_c5_struct_c7_total = ">" + second_c5_struct_c7_size * d["int8"]

    second_c5_struct_c7_c2 = unpack(
        second_c5_struct_c7_total,
        arg[
            second_c5_struct_c7_addr: second_c5_struct_c7_addr +
            second_c5_struct_c7_size
        ],
    )
    listOf = []
    for i in range(second_c5_struct_c7_size):
        listOf.append(second_c5_struct_c7_c2[i])

    third_c_struct_c2_size = first_c_struct_c5[24]
    third_c_struct_c2_addr = first_c_struct_c5[25]

    third_c_struct_c2_total = ">" + third_c_struct_c2_size * d["int8"]

    third_c_struct_c2_c2 = unpack(
        third_c_struct_c2_total,
        arg[third_c_struct_c2_addr: third_c_struct_c2_addr +
            third_c_struct_c2_size],
    )

    listOfof = []
    for i in range(third_c_struct_c2_size):
        listOfof.append(third_c_struct_c2_c2[i])

    d_dict = {
        "D1": first_c_struct_c5[0],
        "D2": first_c_struct_c5[1],
        "D3": first_c_struct_c5[2],
        "D4": [
            first_c_struct_c5[3],
            first_c_struct_c5[4],
            first_c_struct_c5[5],
            first_c_struct_c5[6],
            first_c_struct_c5[7],
            first_c_struct_c5[8],
        ],
        "D5": first_c_struct_c5[9],
        "D6": first_c_struct_c5[10],
        "D7": listOf,
    }

    d2_dict = {
        "D1": first_c_struct_c5[13],
        "D2": first_c_struct_c5[14],
        "D3": first_c_struct_c5[15],
        "D4": [
            first_c_struct_c5[16],
            first_c_struct_c5[17],
            first_c_struct_c5[18],
            first_c_struct_c5[19],
            first_c_struct_c5[20],
            first_c_struct_c5[21],
        ],
        "D5": first_c_struct_c5[22],
        "D6": first_c_struct_c5[23],
        "D7": listOfof,
    }

    a_dict["A1"]["B1"]["C5"].append(d_dict)
    a_dict["A1"]["B1"]["C5"].append(d2_dict)

    first_b_struct_size = obj[9]
    first_b_struct_addr = obj[10]

    first_b_struct_c2_total = ">" + first_b_struct_size * d["float"]

    first_b_struct_c2 = unpack(
        first_b_struct_c2_total,
        arg[first_b_struct_addr: first_b_struct_addr +
            first_b_struct_size * 4],
    )

    listOf = []
    for i in range(first_b_struct_size):
        listOf.append(first_b_struct_c2[i])
    a_dict["A1"]["B5"] = listOf

    first_a_struct_size = obj[13]
    first_a_struct_addr = obj[14]

    first_a_struct_c2_total = ">" + first_a_struct_size * d["int16"]

    first_a_struct_c2 = unpack(
        first_a_struct_c2_total,
        arg[first_a_struct_addr: first_a_struct_addr +
            first_a_struct_size * 4],
    )

    listOf = []
    for i in range(first_a_struct_size):
        listOf.append(first_a_struct_c2[i])
    a_dict["A4"] = listOf

    return a_dict

 
 


pprint(main(b'HQKh\xbf~bj\x15\xe8\x7f\xb2\xcc\x9a[Z\xd2\x00\x02\x00ET\x05&\xbf\x0c\x0f\xa7'
 b'\x00\x00\x00\x04\x00\x00\x00\x83\x030\xd4\xb4\x19{\x06"&\x00\x06\x00'
 b'\x00\x00\x93\x07S\xa1\xe0aF\xa9A\xb6>\xecQ\xdd\xe1\xd0#\xdfC\xdf5\x99'
 b'?\xdc\x9bhf\xdb\x078\x8bo\xceP`\xc0p\xbaUU\x1d\xc8}\xf5\x00\x00\x00\x06\x00;'
 b'(\xc9\x19?\xecm\xeb>R:l\xef0s\xc0\xa6\xe4\x12\x05\xb6\x9cX\xe3\n'
 b'\x80\x00\x00\x00\x04\x00A?_\xf90\xbf\x08\xbby>\xd8M\x15?\x10\x84\xf1\xeeAiu"'
 b'\xce\xc7v]DG\x07'))


pprint(main(b'HQK/\xbe-\x1a\xfd\xa7\xab\x81R\x83\xa9\x17\x91\r\x00\x02\x00C\x14\xd6+'
 b'\xbe\xd6\xbfP\x00\x00\x00\x04\x00\x00\x00\x81(\xc9=\xcc5y\nz\x9a\x00\x06\x00'
 b'\x00\x00\x91g\xe0\xdc\xb3\x91w?s\xdcU\x7f\xd1\xca\xc8\xec\xddJ0\xb6?\xa5'
 b'\xa9D\xaf\xa4\xe7\x80\xcc&\xfc\xb9G\x9f6\x0c\x91\n\x16B\xcaa\x00\x00\x00\x05'
 b"\x00;4\xad\x9c\xbf\xed\x03\xda\xc1\xb1H\x00\xd3~3T\x08\xa2\xee\xb2\xd5'C"
 b'\xeb7\xd3\x00\x00\x00\x03\x00@\xbf>\x87\xee\xbfL\x93+\xbeR\x03\x9e\xbfr('
 b'\xaf\xdc\xd6P\xeeus\xae,\xfch\xbfi'))

print("\n")

