from ..configure import ConfigureAPI

class SQLCommand:
    @staticmethod
    def getUser(username):
        return f"""SELECT * FROM users WHERE username like '{username}'"""
    
    @staticmethod
    def getUserAll():
        return f"""SELECT username, type FROM users"""
    
    @staticmethod
    def deleteUser(username):
        return f"""DELETE FROM users WHERE username='{username}'"""

    @staticmethod
    def insertUser(user):
        return f"""INSERT INTO users (username, hashedPassword, salt, type)
        VALUES ('{user[ConfigureAPI.keyRequestUsername]}', '{user[ConfigureAPI.keyQueryUsersHashedPassword]}',
        '{user[ConfigureAPI.keyQueryUsersSalt]}', '{user[ConfigureAPI.keyQueryUsersType]}')"""
    
    @staticmethod
    def editUser(user):
        return f"""UPDATE users SET 
        hashedPassword='{user[ConfigureAPI.keyQueryUsersHashedPassword]}', salt='{user[ConfigureAPI.keyQueryUsersSalt]}',
        type='{user[ConfigureAPI.keyQueryUsersType]}' WHERE username='{user[ConfigureAPI.keyRequestUsername]}'"""

    @staticmethod
    def insertUserFake(user):
        return f"""INSERT INTO fakeUsers (username, hashedPassword, salt) VALUES ('{user['username']}', '{user['hashedPassword']}', '{user['salt']}')"""