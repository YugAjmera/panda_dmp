#! /usr/bin/env python
import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from math import pi
from nav_msgs.msg import Path


def callback(msg):
	i = 0
	
	while True:
		pose_target = geometry_msgs.msg.Pose()

		print msg.poses[i]

		pose_target.orientation.x = msg.poses[i].pose.orientation.x
		pose_target.orientation.y = msg.poses[i].pose.orientation.y
		pose_target.orientation.z = msg.poses[i].pose.orientation.z
		pose_target.orientation.w = msg.poses[i].pose.orientation.w

		pose_target.position.x = msg.poses[i].pose.position.x
		pose_target.position.y = msg.poses[i].pose.position.y
		pose_target.position.z = msg.poses[i].pose.position.z

		plan = group.go(pose_target, wait=True)
		group.stop()

		if msg.poses[i] == msg.poses[-1]:   #Last member of the list
			break
		i = i+1


moveit_commander.roscpp_initialize(sys.argv)

rospy.init_node('planning_node', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("panda_arm")


display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=20)

joint_goal = group.get_current_joint_values()
joint_goal[0] = 0
joint_goal[1] = -pi/4
joint_goal[2] = 0
joint_goal[3] = -pi/2
joint_goal[4] = 0
joint_goal[5] = pi/3
joint_goal[6] = 0

group.go(joint_goal, wait=True)
group.stop()


sub = rospy.Subscriber('/generate_motion_service_node/cartesian_path', Path, callback)
rospy.spin()


	


