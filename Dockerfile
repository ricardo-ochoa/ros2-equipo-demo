FROM ros:humble-ros-base

SHELL ["/bin/bash", "-c"]
ENV PYTHONUNBUFFERED=1
WORKDIR /ros2_ws

# 1. Compilar el workspace
COPY src/ src/
RUN source /opt/ros/humble/setup.bash \
 && colcon build --event-handlers console_direct+ \
 && rm -rf build log

# 2. Entrada: carga ROS y el workspace antes de cualquier comando
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh \
 && echo 'source /opt/ros/humble/setup.bash' >> /root/.bashrc \
 && echo 'source /ros2_ws/install/setup.bash' >> /root/.bashrc

# 3. Versión: va al final para no invalidar la caché de la compilación
ARG APP_VERSION=dev
ENV APP_VERSION=${APP_VERSION}

STOPSIGNAL SIGINT
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/ros2_ws/install/saludo_robot/lib/saludo_robot/saludo"]
