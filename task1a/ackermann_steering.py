'''
*****************************************************************************************
*
*  ===============================================
*     Niti Vahan (NV) Theme of eYRC 2026-27
*  ===============================================
*
*  This script is intended for implementation of Task 1A of Niti Vahan (NV) Theme.
*
*  Filename:         ackermann_steering.py
*  Created:          2026
*  Last Modified:
*  Author:           e-Yantra Team
*
*  You are ONLY allowed to write your code inside the block marked
*  "ADD YOUR IMPLEMENTATION HERE". Do not change anything outside it - the
*  evaluation script relies on the rest of this file staying as it is.
*
*****************************************************************************************
'''

# Team ID:          < Team-ID >
# Author List:      < Names of the team members who worked on this file, comma separated >
# Filename:         ackermann_steering.py
# Functions:        ackermann_wheel_angles
# Global variables: < List any global variables you add, "None" if you add none >


####################### IMPORT MODULES #######################
import math
import numpy as np
##############################################################


#################### VEHICLE CONSTANTS #######################
WHEELBASE = 0.120           # L: distance between front and rear axle centrelines
TRACK_WIDTH = 0.110         # W: distance between left and right wheel centre
WHEEL_OFFSET = 0.0275       # O: distance between kingpin axis and wheel centre.
##############################################################


##############################################################
############### ADD YOUR IMPLEMENTATION HERE #################
##############################################################


def ackermann_wheel_angles(delta):
    # Agar steering seedha hai (angle zero hai)
    if delta == 0:
        return 0.0, 0.0
    
    # Effective track width calculation
    w_eff = TRACK_WIDTH - (2 * WHEEL_OFFSET)
    
    # Formula components
    cot_delta = 1.0 / math.tan(abs(delta))
    factor = w_eff / (2.0 * WHEELBASE)
    
    cot_inside = cot_delta - factor
    cot_outside = cot_delta + factor
    
    theta_inside = math.atan(1.0 / cot_inside)
    theta_outside = math.atan(1.0 / cot_outside)
    
    # Left turn vs Right turn logic
    if delta > 0:
        left_angle = theta_inside
        right_angle = theta_outside
    else:
        left_angle = -theta_outside
        right_angle = -theta_inside
        
    return left_angle, right_angle


##############################################################
################ END OF YOUR IMPLEMENTATION ##################
##############################################################


#################### DO NOT EDIT BELOW THIS LINE ####################

if __name__ == "__main__":

    test_angles = np.arange(-0.35, 0.35, 0.05)

    for d in test_angles:
        left, right = ackermann_wheel_angles(d)
        print(f"delta={d}  ->  left={left}, right={right}")
