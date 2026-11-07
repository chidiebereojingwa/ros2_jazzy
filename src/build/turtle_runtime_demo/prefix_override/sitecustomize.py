import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ojingwa/ros2_jazzy/src/install/turtle_runtime_demo'
