from abc import abstractmethod

class DBClient:
    def __init__(self, db_name, db_user, db_password):
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
    
    @abstractmethod
    def read(self, id):
        pass

    @abstractmethod
    def create(self, info):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def update(self, id, info):
        pass