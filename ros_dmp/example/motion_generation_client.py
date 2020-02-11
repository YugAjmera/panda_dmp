#!/usr/bin/env python
import numpy as np 
import rospy
from geometry_msgs.msg import PoseStamped
from ros_dmp.srv import *

if __name__ == "__main__":

    rospy.init_node('generate_motion_service_test_client')
    req = GenerateMotionRequest()

    # Compose request message
    req.dmp_name = "/home/yug/catkin_ws/src/panda_dmp/ros_dmp/weights/example.yaml"
    req.tau = 1.0
    req.dt = 0.01
    req.initial_pose = PoseStamped()
    req.initial_pose.header.frame_id = "panda_link0"
    req.initial_pose.pose.position.x = 0.3
    req.initial_pose.pose.position.y = 0.2
    req.initial_pose.pose.position.z = 0.2
    req.initial_pose.pose.orientation.x = 0.5
    req.initial_pose.pose.orientation.y = 0.5
    req.initial_pose.pose.orientation.z = 1.0
    req.initial_pose.pose.orientation.w = 0.5

    req.goal_pose = PoseStamped()
    req.goal_pose.header.frame_id = "panda_link0"
    req.goal_pose.pose.position.x = 0.5
    req.goal_pose.pose.position.y = 0.5
    req.goal_pose.pose.position.z = 0.4
    req.goal_pose.pose.orientation.x = 0.5
    req.goal_pose.pose.orientation.y = 0.5
    req.goal_pose.pose.orientation.z = 1.0
    req.goal_pose.pose.orientation.w = 0.5
    # req.initial_pose.header.frame_id = "panda_link0"

    try:
        service_client = rospy.ServiceProxy('/generate_motion_service', GenerateMotion)
        rospy.loginfo(service_client(req))
    except :
        rospy.loginfo("Service call failed")
    
