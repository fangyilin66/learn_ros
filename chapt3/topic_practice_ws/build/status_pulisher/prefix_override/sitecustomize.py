import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/nvidia/learn_ros/chapt3/topic_practice_ws/install/status_pulisher'
