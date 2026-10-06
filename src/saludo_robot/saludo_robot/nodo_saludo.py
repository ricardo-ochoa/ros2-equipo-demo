import os
import platform

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

VERSION = os.environ.get("APP_VERSION", "dev")
ARQUITECTURA = platform.machine()


class NodoSaludo(Node):
    def __init__(self):
        super().__init__("nodo_saludo")
        self.publicador = self.create_publisher(String, "saludo", 10)
        self.cuenta = 0
        self.create_timer(1.0, self.publicar)
        self.get_logger().info(f"Arrancando v{VERSION} en {ARQUITECTURA}")

    def publicar(self):
        self.cuenta += 1
        msg = String()
        msg.data = f"Hola desde {ARQUITECTURA} · v{VERSION} · #{self.cuenta}"
        self.publicador.publish(msg)
        self.get_logger().info(msg.data)


def main():
    rclpy.init()
    nodo = NodoSaludo()
    try:
        rclpy.spin(nodo)
    except KeyboardInterrupt:
        pass
    finally:
        nodo.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    main()
