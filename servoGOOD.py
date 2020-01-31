from __future__ import division
import time
import pygame
from adafruit_servokit import ServoKit
pygame.init()



pwm = ServoKit(channels=16)
leftstick = 0.07
rightstick = 0.07
liftUP = 0.00
liftDOWN = 0.00
print('Initialized')


gamepad = pygame.joystick.Joystick(0)
gamepad.init()

while True:
    
    pygame.event.get()
    
    if abs(gamepad.get_axis(1)) <= 0.1:
        leftstick = 0.1
        
    elif abs(gamepad.get_axis(4)) <= 0.1:
        rightstick = 0.1
    
    elif abs(gamepad.get_button(3)) <= 0.1:
        liftUP = 0.1
        
    elif abs(gamepad.get_button(0)) <= 0.1:
        liftDOWN = 0.1
        
    
    leftstick = gamepad.get_axis(1)
    rightstick = gamepad.get_axis(4)
    liftUP = gamepad.get_button(3)
    liftDOWN = -gamepad.get_button(0)
    
    
    pwm.continuous_servo[1].throttle = leftstick
    pwm.continuous_servo[4].throttle = rightstick
    pwm.continuous_servo[11].throttle = liftUP
    pwm.continuous_servo[11].throttle = liftDOWN
    
    print("rightstick: ", rightstick)
    
    print("leftstick: ", leftstick)
    
    print("lift: ", liftUP)
    
    print("lift: ", liftDOWN)
    
    
    #axis 0 = A
    #axis 3 = Y