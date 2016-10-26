#!/usr/bin/env python
import pygame, sys, time ,os
from pygame.locals import *

class ps3:
	joystick=0
	joystick_count=0
	numaxes=0
	numbuttons=0

	def __init__(self):
		sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

		pygame.init()
		pygame.joystick.init()
		ps3.joystick = pygame.joystick.Joystick(0)
		ps3.joystick.init()
		ps3.joystick_count = pygame.joystick.get_count()
		ps3.numaxes = ps3.joystick.get_numaxes()
		ps3.numbuttons = ps3.joystick.get_numbuttons()

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

		self.a_right			=button_analog[9]
		self.a_up				=button_analog[8]
		self.a_down				=button_analog[10]
		self.a_l1				=button_analog[14]
		self.a_l2				=button_analog[12]
		self.a_r1				=button_analog[15]
		self.a_r2				=button_analog[13]
		self.a_triangle			=button_analog[16]
		self.a_circle			=button_analog[17]
		self.a_square			=button_analog[19]
		self.a_cross			=button_analog[18]

		self.a_joystick_left_x	=button_analog[0]
		self.a_joystick_left_y	=button_analog[1]
		self.a_joystick_right_x	=button_analog[2]
		self.a_joystick_right_y	=button_analog[3]
		self.acc_x				=button_analog[23]
		self.acc_y				=button_analog[24]
		self.acc_z				=button_analog[25]

		for i in range(0,self.numbuttons):
			button_state[i]=self.joystick.get_button(i)

		self.select			=button_state[0]
		self.joystick_left	=button_state[1]
		self.joystick_right	=button_state[2]
		self.start			=button_state[3]
		self.up				=button_state[4]
		self.right			=button_state[5]
		self.down			=button_state[6]
		self.left			=button_state[7]
		self.l2				=button_state[8]
		self.r2				=button_state[9]
		self.l1				=button_state[10]
		self.r1				=button_state[11]
		self.triangle		=button_state[12]
		self.circle			=button_state[13]
		self.cross			=button_state[14]
		self.square			=button_state[15]
		self.ps				=button_state[16]

		os.dup2(oldstdout_fno, 1)
		os.close(oldstdout_fno)

		pygame.event.get()
		return button_analog
