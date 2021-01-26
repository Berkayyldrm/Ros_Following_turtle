"""
Berkay Yildirim
Robot 2, Jsondan alinan linear ve acisal hiz verilerine gore hareket eder.
Robot 2, calisma sinirlarinda ayna yansimasi gibi hareket eder.
Robot 2'nin baslangic konumu rasgele olarak belirlenir.
"""

import rospy
import math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import turtlesim.srv
import numpy as np
import random
import json

# Data read form JSON file
with open('Odev6.json') as f:
    veri = json.load(f)

pose = Pose()

poseflag = False

def callback(data):
    global pose
    global poseflag
    pose = data
    poseflag = True
   
def move_turtlebot2(speed,angle_speed):
    """
    Robot 2's linear displacement function
    """
    while poseflag == False: # This loop works until the pose info arrives.
        rospy.sleep(0.01)

    vel_msg = Twist()   
    while True:
        
        vel_msg.linear.x= speed
        vel_pub.publish(vel_msg)
        rospy.sleep(1)

        direction_control(angle_speed)

        loop_rate.sleep()  

def rotate(angle_speed,thetta):
    """
    Robot 2's angualar displacement function
    """
    vel_msg = Twist()
    while True:
        diff=abs(pose.theta - thetta)
        
        if diff > 0.1:
            vel_msg.angular.z = angle_speed
            vel_pub.publish(vel_msg)
        else:
            vel_msg.angular.z = 0
            vel_pub.publish(vel_msg)
            break

def direction_control(angle_speed):
    """
    Angle change when Robot-2 hit to wall
    """
    vel_msg = Twist()
    while poseflag == False:
        rospy.sleep(0.01)
    # Hit to left wall and theta 90-180
    if pose.x < 0.1 and pose.theta>0:
        thetta = np.pi - pose.theta
        rotate(angle_speed,thetta)

    # Hit to left wall and theta 180-270    
    elif pose.x <0.1 and pose.theta<0 :
        thetta = -np.pi - pose.theta
        rotate(angle_speed,thetta)

    # Hit to right wall and theta 0-90
    elif pose.x >11 and pose.theta>0:
        thetta = np.pi - pose.theta
        rotate(angle_speed,thetta)

    # Hit to right wall and theta 270-360 
    elif pose.x > 11 and pose.theta<0:
        thetta = -np.pi - pose.theta
        rotate(angle_speed,thetta)

    # Hit to upper wall  
    elif pose.y > 11:
        thetta = -pose.theta
        rotate(angle_speed,thetta)

    # Hit to bottom wall
    elif pose.y < 0.1:
        thetta = -pose.theta
        rotate(angle_speed,thetta)



if __name__=='__main__':
    rospy.init_node('robot2',anonymous=True) 
    
    rospy.Subscriber('/turtle2/pose',Pose,callback,) 

    vel_pub = rospy.Publisher('/turtle2/cmd_vel',Twist,queue_size=5)
    
    loop_rate = rospy.Rate(5)

    #Spawn service
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy("spawn", turtlesim.srv.Spawn)
    spawner(random.randint(1,10),random.randint(1,10),random.uniform(-3.14,3.14),'turtle2')
    
    #Kill service
    rospy.wait_for_service('kill')
    killer = rospy.ServiceProxy("kill",turtlesim.srv.Kill)
    killer('turtle1')
    
    move_turtlebot2(veri[1]["Linear_velocity"],veri[1]["Angular_velocity"])


    rospy.spin()