#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(data):
    print len(data.ranges)

def main():
    rospy.init_node("readscan",anonymous=True)
    rospy.Subscriber("/robot/laser/rightscan", LaserScan, callback)


if __name__ == '__main__':
    main()
    rospy.spin()
    