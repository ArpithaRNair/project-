import hashlib
x= input("Enter text")

def main():
    tex = x.encode("utf-8")
    hash=hashlib.md5(tex)
    hex=hash.hexdigest()
    print (hex)
    return
main()
