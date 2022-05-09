#!/usr/bin/env python
import rospy

from std_msgs.msg import Int16
from project1_solution.msg import TwoInts

def callback(data):
    ### YOUR CODE HERE ###
    
def listener():
    rospy.init_node('solution')
    rospy.Subscriber("two_ints", TwoInts, callback)

    rospy.spin()

if __name__=="__main__":
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
