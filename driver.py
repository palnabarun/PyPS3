from ps3lib import PS3

p = PS3()

try:
    while 1:
        p.update()
        p.print_values()
        p.print_analog()
        p.print_pressures()
        p.print_orientation()
	break
except KeyboardInterrupt:
    print("Keyboard interrupt")
