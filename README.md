# Docker_Correo

## Definición

Es un proyecto simple en python y docker que crea una imagen que envíe correos.

## Clonación

Para clonar el repositorio:

    git clone https://github.com/CarlosDelRosario7/docker_correo.git

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
>
> COUN_PORT=80 -> Puerto que usará el contenedor para FastAPI

#### Nota
Para obtener una clave para mandar correo en Gmail, deberá tener la verificación de 2 pasos activa y craer una "contraseña de aplicación" en:
> https://myaccount.google.com/u/0/apppasswords

## Descargar la imagen desde Docker Hub

Para descargar la imagen:
> docker pull carlosdelrosario7/correo

#### Nota
Puedes omitir este paso ejecutando el docker-compose.yaml directamente y la imagen se descargará automáticamente.

## Construcción de la imagen

En caso de, por alguna razón, no pudo descargar la imagen, construya dicha imagen; para hacer esto, deberás ejecutar:

    docker build -t carlosdelrosario7/correo:v1 .

Si deseas guardar la imagen como un .tar:

    docker save carlosdelrosario7/correo:v1 > ./danny_correo.tar

Para cargar el .tar:

    docker load < ./danny_correo.tar

## Ejecución del contenedor

 Para correr el contenedor a partir de la imagen:

    docker compose up -d

Para detener el contenedor:

    docker compose down

#### Notas

Recuerde modificar correctamente el archivo .env antes de correr la imagen.

