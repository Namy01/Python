def mygreeting(name):
    print("hello"+ name)

def sum(a,b):
    res = a+b
    print("sum:", res)
    return res
def diff(a,b):
    res = a-b
    print("diff:", res)
    return res
def mul(a,b):
    res = a*b
    print("mul:", res)
    return res
def div(a,b):
    res = a/b
    print("div:", res)
    return res

print("This is an calculator .. it will be executed if we run the file that have imported this file")
if __name__ == "__main__":
    print("It wont be executed from the file that imported this file")

person = {
    "name" : "Namrata",
    "age": 36,
    "country" : "Norway"
}