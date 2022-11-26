from redis import Redis

class RedisConnector(object):

    def __init__(self, hostName:str, 
                dbName:str, userName:str, password:str = None,
                port:int = 6379 )->None:
        self.hostName = hostName
        self.port = port 
        self.dbName = dbName
        self.userName = userName
        self.password = password

        self.conn = None

    def __connect__(self):
        return Redis(
            host= self.hostName,
            port = self.port,
            db = self.dbName,
            password = self.password,

        )

    def __disconnect__(self)->None:pass 

    def __create_connection__(self):
        self.conn = self.__connect__()




