#!/usr/bin/env python
"""Extract images from a rosbag.
"""
import cv2
from cv_bridge import CvBridge
from rosidl_runtime_py.utilities import get_message
import rosbag2_py as rosbag2_py
from rclpy.serialization import deserialize_message


def get_rosbag_options(path, serialization_format='cdr'):
    storage_options = rosbag2_py.StorageOptions(uri=path, storage_id='sqlite3') #sqlite3

    converter_options = rosbag2_py.ConverterOptions(
        input_serialization_format=serialization_format,
        output_serialization_format=serialization_format)

    return storage_options, converter_options

dir='/home/xxxx/gv-bags/outdoor_translation_4/'


# for filename in os.listdir(dir):
img_path="/home/xxxx/gv_ws/outdoor_translation_4/img.png"
print(img_path)
# total_filename=os.path.join(dir,filename)

storage_options, converter_options = get_rosbag_options(dir)

reader = rosbag2_py.SequentialReader()
reader.open(storage_options, converter_options)
i = 0 
topic_types = reader.get_all_topics_and_types()
type_map = {topic_types[i].name: topic_types[i].type for i in range(len(topic_types))}
bridge = CvBridge()
i = 1
while reader.has_next():

    topic, data, _ = reader.read_next()

    if (topic == '/camera/color/image_raw'):
        msg_type = get_message(type_map[topic])
        msg = deserialize_message(data, msg_type)

        cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        
        cv2.imwrite(img_path, cv_img)
        break  

print ("Number of images stored: ",i)




