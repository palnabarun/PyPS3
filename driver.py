from ps3contr import ps3

p = ps3()

try:
    while 1:
        p.update()
        print(p.a_triangle)
except KeyboardInterrupt:
    print("Keyboard interrupt")
