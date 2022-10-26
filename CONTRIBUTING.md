# Setup del proyecto

> Se supone que se tiene python3 ya instalado.

### Instalacion de dependencias

- Instalar y actualizar `pip`
```bash
sudo apt install python3-pip
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