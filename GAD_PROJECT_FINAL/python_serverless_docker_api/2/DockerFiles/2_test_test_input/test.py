try:
    f = open("new_input.txt", "r")
    print(f.read())
except:
    f = open("test_input.txt", "r")
    print(f.read())
