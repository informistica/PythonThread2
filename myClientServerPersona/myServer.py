

import socket
from threading import Thread
from myPerson import Persona

class Server(Persona):
    """
    Questa classe rappresenta una persona che opera come server
    """
    def __init__(self, nome, cognome, etica=None,valori=None,opinioni=None,motivazioni=None,consapevolezza=None):
        super().__init__(nome, cognome, etica,valori,opinioni,motivazioni)
        self.consapevolezza = consapevolezza
        self.address='127.0.0.1'
        self.port=22224


    def __repr__(self):
        return f"{self.nome} {self.cognome} {self.consapevolezza} "

    def profilo_studente(self):
        profilo_s = f"""
        Consapevolezza: {self.consapevolezza}
        """
        return super().profilo_personale() + profilo_s

    def avvia_server(self):
        """
        Metodo per aprirsi e mettersi in ascolto aspettando richieste da servire 
        """
        sock_listen = socket.socket()
        sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock_listen.bind((self.address, self.port))
        sock_listen.listen(5)
        print("Server in ascolto su %s." % str((self.address, self.port)))
        return sock_listen
    
    def ricevi_connessioni(self,sock_listen):
        """
        Metodo per accettare richieste di servizio ed assegnare un Thread ad ognuna di esse
        """
        while True:
            sock_service, addr_client = sock_listen.accept()
            print("\nConnessione ricevuta da " + str(addr_client))
            print("\nCreo un thread per servire le richieste ")
            try:
                Thread(target=self.ricevi_comandi, args=(sock_service,addr_client)).start()
            except:
                print("il thread non si avvia")
                sock_listen.close()
   
    def ricevi_comandi(self,sock_service,addr_client):
        """
        Metodo per ricevere i comandi e servire le richieste ricevute
        """
        print("avviato")
        while True:
            dati = sock_service.recv(2048)
            if not dati:
                print("Fine dati dal client. Reset")
                break
            dati = dati.decode()
            print("Ricevuto: '%s'" % dati)
            if dati=='0':
                print("Chiudo la connessione con " + str(addr_client))
                break 
            risultato=0
            oper,n1,n2= dati.split(";")
            if oper=="piu":
                risultato=int(n1)+int(n2)

            if oper=="meno":
                risultato=int(n1)-int(n2)

            if oper=="per":
                risultato=int(n1)*int(n2)

            if oper=="diviso":
                risultato=int(n1)/int(n2)
            
            dati = f"Risposta a : {str(addr_client)}. Il risultato dell'operazione({n1} {oper} {n2}) è :{risultato} "
            dati = dati.encode()
            sock_service.send(dati)
        sock_service.close()  

s1=Server("nome2","cognome2")
sock_lis=s1.avvia_server()
s1.ricevi_connessioni(sock_lis)
