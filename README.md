# pyros_voice_identify
基于ros的语音识别，使用python与科大讯飞语音听写api实现实时的语音识别，并利用话题控制进程。  
## 环境要求：  
* ros，python3.x  
- 声卡：sudo apt install libasound2-dev
* requirement：  
    *
## 节点说明：  
* main_node.py是主程序，承担语音识别模块。只运行该节点不会直接开始语音识别  
- open_switch_node.py用于开启主程序语音识别  
- close_switch_node.py用于关闭主程序语音识别  
* reset_node.py用于重置整个进程，使其恢复到休眠状态。此时可以通过open_switch_node再次开启语音识别  
## 使用步骤 
终端一：   
`cd your_path_to_ROS_workspace/src/`  
`catkin_create_pkg your_package_name std_msgs rospy roscpp`  
`git clone https://github.com/Picaun/pyros_voice_identify.git`  
`gedit pyros_voice_identify/scripts/main_node.py`(修改你的科大讯飞APPID，APIKey，APISecret)  
`cd pyros_voice_identify`  
`mv scripts your_path_to_ROS_workspace/src/your_package_name/`  
`cd your_path_to_ROS_workspace`  
`catkin_make`  
终端二：  
`roscore`  
终端三：  
`rosrun your_package_name main_node.py`  
终端四：  
`rosrun your_package_name open_switch_node.py`  
终端五：  
`rosrun your_package_name close_switch_node.py`  
终端六：  
`rosrun your_package_name reset_node.py`  
  
* 在终端三中查看语音识别情况，使用终端四五来开启与关闭语音识别，使用终端六停止open_switch_node与close_switch_node，然后重新使用终端四五开启与关闭语音识别。  
* ___直接终止open_switch_node不会关闭语音识别___
