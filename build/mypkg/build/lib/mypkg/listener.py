import rclpy
from rclpy.node import Node
from person_msgs.srv import Query2

def main():
    rclpy.init()
    node = Node("listener")
    client = node.create_client(Query2, 'query2')
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('待機中')

    req = Query2.Request()
    req.birthmonth = 1
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('failed to call')
            else:
                node.get_logger().info(str(req.birthmonth) + "月の誕生石: {}".format(response.birthstone))
            break
    '''
    req = Query2.Request()
    req.birthmonth = 2
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('failed to call')
            else:
                node.get_logger().info(str(req.birthmonth) +"月の誕生石: {}".format(response.birthstone))
            break
    req = Query2.Request()
    req.birthmonth = 3
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('failed to call')
            else:
                node.get_logger().info(str(req.birthmonth) +"月の誕生石: {}".format(response.birthstone))
            break
    req = Query2.Request()
    req.birthmonth = 4
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('failed to call')
            else:
                node.get_logger().info(str(req.birthmonth) +"月の誕生石: {}".format(response.birthstone))
            break
    req = Query2.Request()
    req.birthmonth = 5
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('failed to call')
            else:
                node.get_logger().info(str(req.birthmonth) +"月の誕生石: {}".format(response.birthstone))
            break
    req = Query2.Request()
    req.birthmonth = 6
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('failed to call')
            else:
                node.get_logger().info(str(req.birthmonth) +"月の誕生石: {}".format(response.birthstone))
            break
    req = Query2.Request()
    req.birthmonth = 7
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('failed to call')
            else:
                node.get_logger().info(str(req.birthmonth) +"月の誕生石: {}".format(response.birthstone))
            break
    req = Query2.Request()
    req.birthmonth = 8
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('failed to call')
            else:
                node.get_logger().info(str(req.birthmonth) +"月の誕生石: {}".format(response.birthstone))
            break
    req = Query2.Request()
    req.birthmonth = 9
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('failed to call')
            else:
                node.get_logger().info(str(req.birthmonth) +"月の誕生石: {}".format(response.birthstone))
            break
    req = Query2.Request()
    req.birthmonth = 10
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('failed to call')
            else:
                node.get_logger().info(str(req.birthmonth) +"月の誕生石: {}".format(response.birthstone))
            break
    req = Query2.Request()
    req.birthmonth = 11
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('failed to call')
            else:
                node.get_logger().info(str(req.birthmonth) +"月の誕生石: {}".format(response.birthstone))
            break
    req = Query2.Request()
    req.birthmonth = 12
    future = client.call_async(req)
    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('failed to call')
            else:
                node.get_logger().info(str(req.birthmonth) +"月の誕生石: {}".format(response.birthstone))
            break
            
    '''
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
 main()
