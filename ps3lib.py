#!/usr/bin/env python
import pygame, sys, time ,os
from pygame.locals import *
import math

class PS3:
	joystick=0
	joystick_count=0
	numaxes=0
	numbuttons=0

	def __init__(self):
		sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

		pygame.init()
		os.putenv('DISPLAY', ':0.0')
		pygame.display.set_mode((1, 1))
		pygame.joystick.init()
		PS3.joystick = pygame.joystick.Joystick(0)
		PS3.joystick.init()
		PS3.joystick_count = pygame.joystick.get_count()
		PS3.numaxes = PS3.joystick.get_numaxes()
		PS3.numbuttons = PS3.joystick.get_numbuttons()
		self.update()

	def update(self):
		loopQuit = False
		button_state=[0]*self.numbuttons
		button_analog=[0]*self.numaxes
		outstr = ""

		devnull = open('/dev/null', 'w')
		oldstdout_fno = os.dup(sys.stdout.fileno())
		os.dup2(devnull.fileno(), 1)

		for i in range(0,self.numaxes):
			button_analog[i] = self.joystick.get_axis(i)

		for i in range(0,self.numbuttons):
			button_state[i]=self.joystick.get_button(i)

		self.up	= button_state[4]
		self.right = button_state[5]
		self.down = button_state[6]
		self.left = button_state[7]

		self.p_right = button_analog[9]
		self.p_up = button_analog[8]
		self.p_down	= button_analog[10]

		self.acc_x = button_analog[23]
		self.acc_y = button_analog[24]
		self.acc_z = button_analog[25]

		self.select	= button_state[0]
		self.ps	= button_state[16]
		self.start = button_state[3]

		self.l1	= button_state[10]
		self.r1	= button_state[11]
		self.l2	= button_state[8]
		self.r2	= button_state[9]
		self.l3	= button_state[1]
		self.r3	= button_state[2]

		self.p_l1 = button_analog[14]
		self.p_l2 = button_analog[12]
		self.p_r1 = button_analog[15]
		self.p_r2 = button_analog[13]

		self.p_triangle	= button_analog[16]
		self.p_circle = button_analog[17]
		self.p_square = button_analog[19]
		self.p_cross = button_analog[18]

		self.triangle = button_state[12]
		self.circle = button_state[13]
		self.cross = button_state[14]
		self.square	= button_state[15]

		self.a_leftx = button_analog[0]
		self.a_lefty = button_analog[1]
		self.a_rightx = button_analog[2]
		self.a_righty = button_analog[3]

		self.h_left, self.h_right = self.calculate_heading()

		os.dup2(oldstdout_fno, 1)
		os.close(oldstdout_fno)

		pygame.event.get()
		return button_analog

	def calculate_heading(self):
		theta_l =  math.atan2(self.a_lefty, self.a_leftx)
		theta_r =  math.atan2(self.a_righty, self.a_rightx)
		theta_l_d = theta_l * (180 / math.pi)
		theta_r_d = theta_r * (180 / math.pi)
		# theta_l = 90.0 - theta_l_d
		# thera_r = 90.0 - theta_r_d
		return [theta_l_d, theta_r_d]

	def print_values(self):
		print("Up: {0}, Down: {1}, Left: {2}, Right: {3}, Triangle: {4}, Square: {5}, Cross: {6}, Circle: {7}, L1: {8}, L2: {9}, L3: {10}, R1: {11}, R2: {12}, R3: {13}, Select: {14}, Start: {15}, PS: {16}, ".format(
		self.up, self.down, self.left, self.right,
		self.triangle, self.square, self.cross, self.circle,
		self.l1, self.l2, self.l3, self.r1, self.r2, self.r3,
		self.select, self.start, self.ps))

	def print_orientation(self):
		print("Acc_x: {0}, Acc_y: {1}, Acc_z: {2}, ".format(self.acc_x, self.acc_y, self.acc_z))

	def print_pressures(self):
		print("P_Triangle: {0}, P_Square: {1}, P_Cross: {2}, P_Circle: {3}, P_Up: {4}, P_Right: {5}, P_Down: {6}, P_L1: {7}, P_L2: {8}, P_R1: {9}, P_R2: {10}".format(
		self.p_triangle, self.p_square, self.p_cross, self.p_circle,
		self.p_up, self.p_right, self.p_down,
		self.p_l1, self.p_l2, self.p_r1, self.p_r2))

	def print_analog(self):
		print("Left_X: {0}, Left_Y: {1}, Right_X: {2}, Right_Y: {3}".format(self.a_leftx, self.a_lefty, self.a_rightx, self.a_righty))

	def print_heading(self):
		print("Left Heading: {0}, Right Heading: {1}".format(self.h_left, self.h_right))

	def get_values(self):
		return {'up': self.up, 'down': self.down, 'left': self.left, 'right': self.right,
		'triangle': self.triangle, 'square': self.square, 'cross': self.cross, 'circle': self.circle,
		'l1': self.l1, 'l2': self.l2, 'l3': self.l3, 'r1': self.r1, 'r2': self.r2, 'r3': self.r3,
		'select': self.select, 'start': self.start, 'ps': self.ps}

	def get_orientation(self):
		return {'acc_x': acc_x, 'acc_y': acc_y, 'acc_z': acc_z}

	def get_pressures(self):
		return {'p_triangle': self.p_triangle, 'p_square': self.p_square, 'p_cross': self.p_cross, 'p_circle': self.p_circle,
		'p_up': self.p_up, 'p_right': self.p_right, 'p_down': self.p_down,
		'p_l1': self.p_l1, 'p_l2': self.p_l2, 'p_r1': self.p_r1, 'p_r2': self.p_r2}

	def get_analog(self):
		return {'leftx': self.a_leftx, 'leftr': self.a_lefty, 'rightx': self.a_rightx, 'righty': self.a_righty}

	def get_heading(self):
		return {'h_left': self.h_left, 'h_right': self.h_right}

	def get_all(self):
		r = dict()
		r.update(self.get_values())
		r.update(self.get_orientation())
		r.update(self.get_pressures())
		r.update(self.get_analog())
		r,update(self.get_heading())
		return r
