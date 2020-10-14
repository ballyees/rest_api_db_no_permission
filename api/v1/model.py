import uuid, hashlib
class User():
    def __init__(self, username: str, password: str, type: str):
        self.__username = str(username)
        self.__salt = self.__getNewSalt()
        self.__password = password
        self.__hashedPassword = User.getNewHashingPassword(password, self.__salt)
        self.__type = type

    @staticmethod
    def getNewHashingPassword(password, salt):
        return hashlib.sha1(str(password).encode('utf-8') + str(salt).encode('utf-8')).hexdigest()

    def __getNewSalt(self):
        return uuid.uuid4().hex

    def getUserJson(self):
        return {'username': self.__username, 'hashedPassword': self.__hashedPassword, 'salt': self.__salt, 'type': self.__type}

    def checkIsUser(self):
        return (self.__username) and (self.__password) and (self.__type)

    def __str__(self):
        return f'username: {self.__username}, password: {self.__hashedPassword}, token: {self.__type}'

    def NewSalt(self):
        self.__salt = self.__getNewSalt()
        self.__hashedPassword = User.getNewHashingPassword(self.__password, self.__salt)
