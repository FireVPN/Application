import socket, sys, threading

LOCALVPN = ("localhost", 6220)
INT = ("localhost", 6221)

class Proxy():
    def __init__(self, punched_sock, partner, server):
        self.server = server
        self.partner = partner
        self.vpn_client_port = 0
        self.socket_int = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket_int.bind(INT)
        self.socket_int.settimeout(1)

        self.socket_ext = punched_sock
        self.socket_ext.settimeout(1)

    def int_to_ext(self):
        try:
            data, addr = self.socket_int.recvfrom(4096)
            if(not self.server):
                self.vpn_client_port = addr[1]
            print (self.partner)
            self.socket_ext.sendto(data, self.partner)
            print("int to ext")
        except:
            pass

    def ext_to_int(self):
        try:
            data, addr = self.socket_ext.recvfrom(4096)
            if not self.server:
                self.socket_int.sendto(data, ("localhost", self.vpn_client_port))
            else:
                self.socket_int.sendto(data, LOCALVPN)
            print("ext to int")
        except:
            pass

