import rospy
from nav_msgs.msg import Odometry
 
def callback(msg):
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    print("x: {}, y: {}".format(x,y))
    
    
rospy.init_node('check_odometry')
odom_sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()
