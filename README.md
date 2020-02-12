# Controlling the Panda arm using ros_dmp

To run panda arm with Moveit controllers:
`roslaunch panda_moveit_config demo.launch`

To run ros_dmp: 
`roslaunch ros_dmp dmp_sim.launch`

Run rviz to visualize learned and demonstrated path published on following topics which can be visualized in rviz. 
* Select frame "panda_link0" in rviz to view the generated paths (changes made in ros_dmp)
- `/learn_dmp_service_node/demonstrated_path`
- `/learn_dmp_service_node/cartesian_path`
- `/learn_dmp_service_node/imitated_path`


Go to ros_dmp/example folder and run the Learn_client script:
`python learn_client.py`

Start the planning script:
`python planning_script_traj.py`

Now generate motion_client: (Dont forget to change the path to weights/example.yaml)
`python motion_generation_client.py` 


