# Docker_Correo

## Definición

Es un proyecto simple en python y docker que crea una imagen que envíe correos.

## Clonación

Para clonar el repositorio:

    git clone https://github.com/CarlosDelRosario7/docker_correo/blob/main/.gitignore.git

## Configuración

Entre a la carpeta clonada:

    cd docker_correo

Copie el archivo .env para configurarlo:

    cp ./.env.example ./.env

### Estructura del .env

> EMAIL=example@gmail.com -> Deberá poner su correo correcto.
> 
> PASSWORD=su_clave -> No poner si clave de correo principal; solo la que se le dio para mandar correos.
> 
> SMTP_SERVER=smtp.gmail.com -> Lo puedes dejar así si usará Gmail.
> 
> SMTP_PORT=465 -> Igual, si usará Gmail.
> 
> FAST_ADMIN=admin -> Usuario para docs y redoc de FastAPI
> 
> FAST_CLAVE=admin -> Clave de FastAPI para docs y redoc

## Construcción de la imagen

Para construir la imagen, deberás ejecutar:

    docker build -t dannyhack/correo:v1

Si deseas guardar la imagen como un .tar:

    docker save dannyhack/correo:v1 > ./danny_correo.tar

Para cargar el .tar:

    docker load < ./danny_correo.tar

## Ejecución de la imagen

 Para correr la imagen:

    docker compose up -d

Para detener la imagen:

    docker compose down

## Notas:

- Recuerde modificar correctamente el archivo .env antes de correr la imagen.
- El contenedor usará el puerto 8888. Podrás cambiar esto en el docker-compose.yaml.
- Si el repo está privado:
   

     git clone https://your_token_classic:x-oauth-basic@github.com/CarlosDelRosario7/docker_correo.git

