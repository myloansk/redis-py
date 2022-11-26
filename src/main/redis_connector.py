from redis import Redis

class RedisConnector(object):

    def __init__(self, hostName:str, 
                dbName:str, userName:str, password:str = None,
                port:int = 6379 )->None:
        self.hostName = hostName
        self.port = port 
        self.dbName = dbName
        self.password = password

        self.rdConn = None

    def __connect__(self):
        return Redis(
            host= self.hostName,
            port = self.port,
            db = self.dbName,
            password = self.password,

        )

    def __disconnect__(self)->None:
        self.rdConn.close()

    def __create_connection__(self):
        self.rdConn = self.__connect__()




