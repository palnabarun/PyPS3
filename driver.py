from ps3contr import ps3

p = ps3()

try:
    while 1:
        p.update()
        print(p.numaxes)
        print(p.numbuttons)
        print(p.a_triangle)
	break
except KeyboardInterrupt:
    print("Keyboard interrupt")
