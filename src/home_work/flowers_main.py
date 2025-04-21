

# i  - счетчик символов :     i +=  1
# j0 - счетчик нулей    :    j0 +=  1
# j1 - счетчик единиц   : const  = -1
# jc - счетчик блоков   :     10...01
#  1  1  0  0  0  1  1
# -1 -1 +1 +1 +1 -1 -1
#    -1  0  1  2
def calculat(flow_place):
    result, max_0, i, j0, j1 = 0, 0, 0, 0, 0
    for i in range(len(flow_place)):
        # print(flow_place[i], end="")
        # if flow_place[-1] == '1':
        #     result += -1
        if flow_place[i] == '1':
            if j0 > max_0:     # фиксируем max
                result = j0
            j0 = -1            # счетчик едини
            i += 1
        elif flow_place[i] == '0':
            j0 += 1
            i += 1



        if result < 0:
            result = 0
        # break
    if i == len(flow_place):
        if flow_place[-1] == '1':
            result -= 1

    return result


def us_inp():
    while True:
        flow_place = input("Покажите клумбу:\n")
        if flow_place == "": break
        calculat(flow_place)
        print(f"Требуется {calculat(flow_place)} шт. цветов.")

if __name__ == "__main__":
    us_inp()

