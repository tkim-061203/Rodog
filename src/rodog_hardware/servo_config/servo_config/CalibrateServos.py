#!/usr/bin/env python3
# coding: utf-8
import sys
import numpy as np
import math as m

from ServoCalibrationDefinition import motor_config

# FIRST define a new motor class
dog  = motor_config()

'''    HOW TO CALIBRATE THE MOTORS
This is how the robot should look at the calibbration position of [0,0,90]
                            LINKAGE
                          /‾‾‾‾‾‾‾\------------------- q
                         /   _______                   |
                        |   |    o__|___UPPER LEG______/   <---- UPPER LEG AT 0° POINTS HORIZONTALLY BACKWARD
   LOWER LEG SERVO -->  |___|__o    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾/
      AT 90° POINTS         |       |                /
   HORIZONTALLY FORWARD      ‾‾‾‾‾‾‾                /
                            SERVO HUB              / LOWER LEG
                                                  /
                                                 O

CALIBRATION PROCESS
1. Mount servo hubs (without legs) on hip servos at approximately 90 degrees (middle of the servo's range)
2. Ensure all motors are powered and run this script with:
            pos = calibration_pos
                                                and,
            offsets = np.array(
                    [[90, 90, 90, 90],
                     [0 , 0 , 0 , 0 ],
                     [0 , 0 , 0 , 0 ]])
3. Mount upper leg and lower leg servo horn **such that a positive calibration angle will achieve the desired position**.
    So, upper leg should be slightly angled up toward the back of the robot and lower leg servo horn
    should be slightly angled down from the forward horizontal
4. Run this script repeatedly and adjust calibration offsets until the deesired position is reached.
    It is suggested to calibrate hips first.

    HIP   servos: positive angles rotate the hip up
    UPPER servos: positive angles rotate clockwise for left and anticlockwise for right (down on diagram)
    LOWER servos: positive angles rotate clockwise for left and anticlockwise for right (up on diagram)
5. Once calibration offsets have all been found, copy values of "offsets" array to the hardware interface
    and replace values of "self.physical_calibration_offsets"

'''

#-------- MOVING CALIBRATED LEGS TO THE HOME POSITION -------- #
# ## Home position values:
calibration_pos = [0,0,90] # [hip_servo angle, upper leg servo angle,lower leg servo angle]

