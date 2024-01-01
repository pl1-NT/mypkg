import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def cb(request,response):
    if request.birthmonth == 1:
        response.birthstone = "garnett"
    elif request.birthmonth == 2:
        response.birthstone = "amethyst"
    elif request.birthmonth == 3:
        response.birthstone = "aquamarine"
    elif request.birthmonth == 4:
        response.birthstone = "diamond"
    elif request.birthmonth == 5:
        response.birthstone = "emerald"
    elif request.birthmonth == 6:
        response.birthstone = "moonstone"
    elif request.birthmonth == 7:
        response.birthstone = "ruby"
    elif request.birthmonth == 8:
        response.birthstone = "peridot"
    elif request.birthmonth == 9:
        response.birthstone = "sapphire"
    elif request.birthmonth == 10:
        response.birthstone = "tourmaline"
    elif request.birthmonth == 11:
        response.birthstone = "topaz"
    elif request.birthmonth == 12:
        response.birthstone = "tanzanite"

    return response

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)
