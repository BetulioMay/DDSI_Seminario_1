# Setup del proyecto

<blockquote>
	<p>Se supone que se tiene python3 ya instalado. Si no se tiene instalado, lo puede instalar en https://www.python.org/downloads.</p>
	<p>Tambien se supone que se tiene git instalado (esta instalado por defecto en distros Linux). En caso de no ser asi (caso Windows), instalarlo en https://git-scm.com/downloads</p>
</blockquote>

### Clonar repositorio

- Hacer `fork` al repositorio en la parte superior derecha (Boton _fork_).
	- Se creara un repositorio https://github.com/tu_nombre_de_usuario/DDSI_Seminario_1
	- Clonar repositorio.
	- Crear un nuevo repositorio remoto que apunte al repositorio original.
	```bash
	git remote add upstream https://github.com/BetulioMay/DDSI_Seminario_1
	```

### Instalación de dependencias

- Actualizar `pip`
```bash
python3 -m pip install --upgrade pip
```

- Instalar dependencias
```bash
pip3 install -r requirements.txt
```

### Configurar variables de entorno

- Copiar y pegar lo que hay en `.envrc` en `.env`
```bash
touch .env
cp .envrc .env
```

Rellenar en `.env` los campos correspondientes a las variables de entorno locales.

## Ejecución

- Linux
```bash
bash run.sh
```
- Windows
```powershell
.\run.ps1
```

## Contribuir al proyecto

- Actualiza tu repositorio con el repositorio _upstream_
```bash
git pull upstream master
```
- Hacer los cambios que sean oportunos: arreglar bugs, agregar una nueva funcionalidad, etc. Haciendo `commit` de tus cambios (agrega cuantos creas necesarios por el camino, no tengas miedo) con un mensaje que refleje de la mejor manera posible tales cambios.
- Comprobar que los cambios se efectúen de manera correcta.
- Actualizar tus cambios con tu repositorio https://github.com/tu_nombre_de_usuario/DDSI_Seminario_1.
```bash
git push origin master
```
- Finalmente crear un _pull request_ para aportar tu contribución.

## Para noobs de Python
- _Naming convention_ (convención de nombres):
	- Usar siempre _snake_case_, NO _camelCase_.
- Usaremos un paradigma modular:
	- Todo son procedimientos (funciones).
	- Agrupar funciones en ficheros _.py_ (modulos).
	- Nada de clases (No matar moscas a cañonazos).
