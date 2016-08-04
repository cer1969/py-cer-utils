# CRISTIAN ECHEVERRÍA RABÍ

import psycopg2

#---------------------------------------------------------------------------------------------------
# PostgreSQL Connection

#def get_postgresql_connection(user, password, db, host="127.0.0.1", port=5432):
#
#    import psycopg2
#
#    return psycopg2.connect(host=host, port=port, user=user, password=password, database=db)

#---------------------------------------------------------------------------------------------------

class PostgreSQLConnector:
    """
    With Context

    tunnel: Instancia de ssh_tunnel.WFTunnel opcional.
    force_tunnel: Asume que se suministró una instancia en tunnel.
                  Si es falso se tratará de establecer la conexión directa antes de crear el tunnel
                  Si es verdadero se creará el tunnel sin probar conexión dirrecta
    """
    def __init__(self, db, user, password, host="127.0.0.1", port=5432, 
            tunnel=None, force_tunnel=False):
        
        self._db = db
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._tunnel = tunnel
        self._force_tunnel = force_tunnel
        self._cnx = None

    def _start_tunnel(self):
        self._tunnel.run()
        self._tunnel.start()
    
    def _get_cnx(self):
        return psycopg2.connect(host=self._host, port=self._port, user=self._user, 
            password=self._password, database=self._db)

    def __enter__(self):
        if self._tunnel and self._force_tunnel:
            self._start_tunnel()
        
        try:
            self._cnx = self._get_cnx()
        except psycopg2.OperationalError:
            if self._tunnel:
                self._start_tunnel()
            self._cnx = self._get_cnx()
        return self._cnx
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self._cnx: self._cnx.close()
        if self._tunnel: self._tunnel.stop()
