def test():
        print("---in test func ---")

test()
ret = test

print(id(ret))
print(id(test))