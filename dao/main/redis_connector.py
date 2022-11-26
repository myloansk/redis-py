from redis import Redis

class RedisConnector(object):

    def __init__(self, hostName:str, 
                dbName:int,  password:str = None,
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
        try:
            self.rdConn = self.__connect__()
            print("Connected")
        except:
            print("Connecting failed")

def main():
    redisConnector =  RedisConnector(hostName="127.0.0.1", dbName = 0)
    redisConnector.__create_connection__()
    

if __name__ == "__main__":
    main()




