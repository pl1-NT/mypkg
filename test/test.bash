#!/bin/bash
# SPDX-FileCopyrightText: 2023 Touki Nishi
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"  
source $dir/.bashrc
cd $dir/ros2_ws/src
git clone https://github.com/pl1-NT/person_msgs.git

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 5 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep '4月の誕生石: diamond'
 
