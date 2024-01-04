#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"  
cd $dir/ros2_ws/src
git clone https://github.com/pl1-NT/person_msgs.git
cd $dir/ros2_ws
colcon build
ros2 interface show "person_msgs/srv/Query2"
source $dir/.bashrc

timeout 5 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep '月の誕生石' 
