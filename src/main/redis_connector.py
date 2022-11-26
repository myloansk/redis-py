import redis 

class RedisConnector(object):

    def __init__(self, hostName:str, 
                dbName:str, userName:str, password:str = None,
                port:int = 6379 )->None:
        self.hostName = hostName
        self.port = port 
        self.dbName = dbName
        self.userName = userName
        self.password = password

    def __connect__(self):pass

    def __disconnect__(self)->None:pass 

    def __create_connection__(self)->None:pass




