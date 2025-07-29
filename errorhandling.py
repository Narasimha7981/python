# try except - error handling
# 0
# try : 
#     num = int(input("enter a number : "))
#     result = 100/num
#     print (result)

# except ValueError :
#     print("Enter only numbers > 0")

# except ZeroDivisionError :
#     print("It is not divisible by zero")

# try:
#     num = int(input("Enter a num : "))
#     result = 100/num
#     print(result)
# except Exception as e:
#     print(f"Exception : {e}")


class NegativeNumErr(Exception):
    pass

try:
    num = int(input("Enter a num : "))
    if num < 0:
        raise NegativeNumErr("Negative Numbers not accepted!!")
    result = 100/num
    print(result)
except Exception as e:
    print(f"Exception : {e}")