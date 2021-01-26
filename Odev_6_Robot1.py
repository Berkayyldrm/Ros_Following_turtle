"""
Berkay Yildirim
"""

import rospy
import math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import turtlesim.srv
import numpy as np
import random
import json

with open('Odev6.json') as f:
    veri = json.load(f)

pose1 = Pose()
pose2 = Pose()
vel_msg = Twist()
poseflag1 = False
poseflag2 = False

# Robot-1
def callback1(data):
    global pose1
    global poseflag1
    pose1 = data
    poseflag1 = True
    
# Robot-2
def callback2(data):
    global pose2
    global poseflag2
    pose2 = data
    poseflag2 = True
    

def movement(distance,error_sum):
    """
    Movement func for Robot-1
    """
    while poseflag1 == False and poseflag2 == False: # This loop works until the pose info arrives.
        rospy.sleep(0.01)
    
    while True:
        v_error,theta_error = calculate_error(distance)

        error_sum,linear_vel,angle_vel = PID(error_sum,v_error,theta_error)
            
        vel_msg.linear.x = linear_vel
        vel_msg.angular.z = angle_vel
        vel_pub.publish(vel_msg) 
                
        loop_rate.sleep() 
    

def calculate_error(distance):
    """
    The function that calculates the error from the distance between Robot 1 and Robot 2
    """

    u1 = pose2.x - pose1.x
    u2 = pose2.y - pose1.y
    v_error=np.sqrt((u1)**2+(u2)**2)-distance
    theta_goal = np.arctan2(u2,u1)
    u3 = theta_goal - pose1.theta
    theta_error = np.arctan2(np.sin(u3),np.cos(u3))
    return v_error,theta_error

def PID(error_sum,v_error,theta_error):
    """
    We obtain the speed of the robot using a PID controller.
    """
    Kp = 0.5
    Ki= 0.01
    p = v_error*Kp 
    I = v_error*Ki    
    linear_vel = p+I
    error_sum += v_error
    Kh = 0.7
    angle_vel = Kh*theta_error
    return error_sum,linear_vel,angle_vel

if __name__=='__main__':
    rospy.init_node('robot1',anonymous=True) 

    rospy.Subscriber('/turtle1/pose',Pose,callback1)
    
    rospy.Subscriber('/turtle2/pose',Pose,callback2) 

    vel_pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=5)
    
    loop_rate = rospy.Rate(5)
    
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy("spawn", turtlesim.srv.Spawn)
    spawner(0,0,0,'turtle1')

    movement(veri[0]["Following_distance"],0)
    
    rospy.spin()
