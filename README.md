# Controlling the Panda arm using ros_dmp



1. To plan give visual goal positions to the panda arm using Moveit Interface:
`roslaunch panda_moveit_config demo.launch rviz_tutorial:=true`

- Add Motion Planning
- Select panda arm in Planning request tab


2. To run panda arm with Moveit controllers:
`roslaunch panda_moveit_config demo.launch`

To run ros_dmp: 
`roslaunch ros_dmp dmp_sim.launch`

Go to ros_dmp/example folder and run the Learn_client script:
`python learn_client.py`

Start the planning script:
`python planning_script.py` - This attempts each and every point and if the point if not reachable, it will move on to the next.
`python planning_script_traj.py` - This stores all the points in an array and then traces them as a trajectory. (Prefered) But it stops if some point is not reachable.

Now generate motion_client: (Dont forget to change the path to weights/example.yaml)
`python motion_generation_client.py` 

* Select frame "panda_link0" in rviz to view the generated paths (changes made in ros_dmp)
