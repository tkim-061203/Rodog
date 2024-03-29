from adafruit_servokit import ServoKit
# from leg_config import *
import numpy as np
import math as m


class motor_config():
    def __init__(self):
        self.pwm_max = 2400
        self.pwm_min = 370
        self.kit = ServoKit(channels=16) #Defininng a new set of servos uising the Adafruit ServoKit LIbrary
        
        #DefinING servo indices
        ## FRONT LEFT
        self.front_left_hip   = 10
        self.front_left_upper = 9
        self.front_left_lower = 8

        ## FRONT RIGHT
        self.front_right_hip   = 14
        self.front_right_upper = 13
        self.front_right_lower = 12

        ## BACK LEFT
        self.back_left_hip   = 6
        self.back_left_upper = 5
        self.back_left_lower = 4

        ## BACK RIGHT
        self.back_right_hip   = 2
        self.back_right_upper = 1
        self.back_right_lower = 0
        """ SERVO INDICES, CALIBRATION MULTIPLIERS AND OFFSETS
            #   ROW:    which joint of leg to control 0:hip, 1: upper leg, 2: lower leg
            #   COLUMN: which leg to control. 0: front-right, 1: front-left, 2: back-right, 3: back-left.

                #               0                  1                2               3
                #  0 [[front_right_hip  , front_left_hip  , back_right_hip  , back_left_hip  ]
                #  1  [front_right_upper, front_left_upper, back_right_upper, back_left_upper]
                #  2  [front_right_lower, front_left_lower, back_right_lower, back_left_lower]] """

        self.pins = np.array([[14,10,2,6], 
                              [13,9,1,5], 
                              [12,8,0,4]])

        self.right_leg_servo_list = [self.front_right_upper,self.front_right_lower,self.back_right_upper,self.back_right_lower]
        self.left_leg_servos_list = [ self.front_left_upper, self.front_left_lower,self.back_left_upper,self.back_left_lower]
        self.hip_opposite_list = [self.front_right_hip,self.back_left_hip]

        #applying calibration values to all servos
        self.create()

    def create(self):
        for i in range(16):
            self.kit.servo[i].actuation_range = 180
            self.kit.servo[i].set_pulse_width_range(self.pwm_min, self.pwm_max)
    def calibrate_servo(self,servo_number):
        cal = False
        while cal == False:  
            angle = input('InputServo angle: ')
            self.kit.servo[servo_number].angle = float(angle)
            response = input('Is the servo fully vertical? y/n')
            if response == 'y':
                cal = True
                calibration_angle = float( angle)
                print('The calibration angle for servo ',servo_number, ' is ', calibration_angle)
                return
    def moveAbsAngle(self,servo_number,angle):
        
        # Takes 180-angle so that the movement it the same as the right lef
        if servo_number in self.left_leg_servos_list:
            self.kit.servo[servo_number].angle = 180 - angle
        elif servo_number in self.hip_opposite_list: #corrects hip angle such that higher numbers are angles of elevation. Higher hip values fo all lift up
            self.kit.servo[servo_number].angle = 180 - angle
        else:
            self.kit.servo[servo_number].angle = angle
    def relax_all_motors(self):
        """Relaxes desired servos so that they appear to be turned off. 

        Parameters
        ----------
        servo_list : 3x4 numpy array of 1's and zeros. Row = Actuator; Column = leg.
                    If a Given actuator is 0 is 1 it should be deactivated, if it is 0 is should be left on. 
        """

        for i in range(16):
            try:
                self.kit.servo[i].angle = None
            except Exception as e:
                print(f"Error occurred with servo {i}. Error message: {e}")
        
