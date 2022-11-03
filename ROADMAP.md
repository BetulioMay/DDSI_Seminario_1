# ROADMAP

### Conexion
- Conexión con base de datos: <strong>HECHO</strong>
	- `src/connection.py:connect()`.

### Funcionalidad

- Creación de nueva tabla STOCK con 10 tuplas predefinidas en el código.
- Borrar tabla STOCK.
- Dar de alta nuevo pedido.
- Mostrar el contenido de las tablas de la BD.
- Salir del programa y cerrar conexión con la BD:
	- Implementado el cierre de conexión: `src/connection.py:close_connection()`

### Interfaz
> NOTA: Todas las interfaces se encuentran en `src/interfaces`.

- Main loop: <strong>HECHO</strong>
- Dar de alta al cliente (interfaz)