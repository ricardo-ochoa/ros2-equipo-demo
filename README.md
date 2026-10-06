# ros2-equipo-demo

Demo de trabajo en equipo con **ROS 2 Humble + Docker + GHCR**.

El nodo `saludo` publica cada segundo en `/saludo` un mensaje con la **arquitectura**
donde corre (`x86_64` en la Mac, `aarch64` en la Jetson) y la **versión** de la imagen.

## Desarrollo (en tu máquina)

```bash
docker compose -f compose.dev.yaml up --build
```

## Publicar una versión

Solo GitHub Actions publica. Crea y sube un tag:

```bash
git tag v0.1.0
git push origin v0.1.0
```

Se publica `ghcr.io/ricardo-ochoa/ros2-equipo-demo:0.1.0` para `amd64` y `arm64`.

## Desplegar en el robot

Solo se necesitan `compose.yaml` y un `.env`:

```bash
echo "TAG=0.1.0" > .env
docker compose pull
docker compose up -d
docker compose logs -f
```
