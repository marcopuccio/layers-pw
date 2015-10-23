def digit_creation(num):
    pattern = (5, 4, 3, 2, 7, 6, 5, 4, 3, 2)
    cuil = num[:9]
    digit = 0
    for x, y in zip(num, pattern):
        digit = digit + (int(x) * y)
    rest = digit % 11
    digit = 11 - rest
    return digit

def digit_validation(num, api):
    a = VerificatorAPI()
    api_resp = str(a.add_one(int(num)))
    print "The Api response is: %s" % api_resp
    created_digit = num[:10] + str(digit_creation(num))
    print "The splitted number with the digit created is: %s" % created_digit
    if created_digit == api_resp:
        return "Cuil Correcto"
    else:
        return "Cuil Incorrecto"        


class VerificatorAPI(object):
    def add_one(self, num):
        num += 1
        return num
