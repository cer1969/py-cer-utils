# CRISTIAN ECHEVERRÍA RABÍ

import pymysql

#---------------------------------------------------------------------------------------------------

class MySQLConnector:
    """
    With Context

    tunnel: Instancia de ssh_tunnel.WFTunnel opcional.
    force_tunnel: Asume que se suministró una instancia en tunnel.
                  Si es falso se tratará de establecer la conexión directa antes de crear el tunnel
                  Si es verdadero se creará el tunnel sin probar conexión dirrecta
    """
    def __init__(self, db, user, password, host="127.0.0.1", port=3306, cursorclass=None, 
        tunnel=None, force_tunnel=False):
        self._db = db
        self._user = user
        self._password = password
        self._host = host
        self._port = port
        self._cursorclass = pymysql.cursors.DictCursor if cursorclass is None else cursorclass
        self._tunnel = tunnel
        self._force_tunnel = force_tunnel
        self._cnx = None

    def _start_tunnel(self):
        self._tunnel.run()
        self._tunnel.start()
    
    def _get_cnx(self):
        return pymysql.connect(host=self._host, port=self._port, user=self._user, 
            password=self._password, db=self._db, cursorclass=self._cursorclass)

    def __enter__(self):
        if self._tunnel and self._force_tunnel:
            self._start_tunnel()
        
        try:
            self._cnx = self._get_cnx()
        except pymysql.err.OperationalError:
            if self._tunnel:
                self._start_tunnel()
            self._cnx = self._get_cnx()
        return self._cnx
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self._cnx: self._cnx.close()
        if self._tunnel: self._tunnel.stop()