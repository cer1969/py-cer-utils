# CRISTIAN ECHEVERRÍA RABÍ

from sshtunnel import SSHTunnelForwarder

#---------------------------------------------------------------------------------------------------

def get_tunnel(host, user, password, remote_addr, local_addr):
    return SSHTunnelForwarder(host, ssh_username=user, ssh_password=password,
        remote_bind_address=remote_addr, local_bind_address=local_addr)


def get_wf_tunnel(web, user, password, remote_port, local_port):
    host = ("%s.webfaction.com" % web, 22)
    remote_addr = ("127.0.0.1", remote_port)
    local_addr = ("127.0.0.1", local_port)
    return get_tunnel(host, user, password, remote_addr, local_addr) 


class WFTunnel:
    def __init__(self, web, user, password, remote_port, local_port):
        self._web = web
        self._user = user
        self._password = password
        self._remote_port = remote_port
        self._local_port = local_port
        self._tunnel = None
    
    def run(self):
        self._tunnel = get_wf_tunnel(self._web, self._user, self._password, self._remote_port, 
            self._local_port)
    
    def start(self):
        self._tunnel.start()
    
    def stop(self):
        self._tunnel.stop()

