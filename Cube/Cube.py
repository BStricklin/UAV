import math, pygame, time
from operator import itemgetter

import rospy
from std_msgs.msg import Float32


def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    print(data.data)

def Cube():

    rospy.init_node('Cube', anonymous=True)

    rospy.Subscriber("/attitude", Float32, callback) # Subscribe to /attitude topic

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    Cube()


