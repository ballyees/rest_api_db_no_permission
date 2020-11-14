import sqlite3
from os.path import join, dirname, abspath
from .SQLCommand import SQLCommand
from ..model import User
from ..sqlApiV1 import SqlApiV1

class SqlApiStoreV1(SqlApiV1):
    def __init__(self, DBName):
        SqlApiV1.__init__(self, DBName)
        self.__connector = self.getConnector()
        self.__cur = self.getCursor()
    
    # --------------------------------------------------------------------------------------------------------------------------------
    #                                                         Product
    # --------------------------------------------------------------------------------------------------------------------------------
    
    def getAllProducts(self):
        rows = self.__cur.execute(SQLCommand.getAllProducts())
        col = []
        for c in self.__cur.description:
            col.append(c[0])
        return [dict(zip(col, row)) for row in rows.fetchall()]

    def getProduct(self, productCode):
        rows = self.__cur.execute(SQLCommand.getProduct(productCode))
        col = []
        for c in self.__cur.description:
            col.append(c[0])
        return [dict(zip(col, row)) for row in rows.fetchall()]

    def editProduct(self, data):
        self.__cur.execute(SQLCommand.editProduct(data))
        self.__connector.commit()
        return {'Success': True}
    
    def deleteProduct(self, productCode):
        self.__cur.execute(SQLCommand.deleteProduct(productCode))
        self.__connector.commit()
        return {'Success': True}
    
    def insertProduct(self, data):
        self.__cur.execute(SQLCommand.insertProduct(data))
        self.__connector.commit()
        return {'Success': True}

    # --------------------------------------------------------------------------------------------------------------------------------
    #                                                         Customer
    # --------------------------------------------------------------------------------------------------------------------------------
    
    def getAllCustomers(self):
        rows = self.__cur.execute(SQLCommand.getAllCustomers())
        col = []
        for c in self.__cur.description:
            col.append(c[0])
        return [dict(zip(col, row)) for row in rows.fetchall()]

    def getCustomer(self, customerNumber):
        rows = self.__cur.execute(SQLCommand.getCustomer(customerNumber))
        col = []
        for c in self.__cur.description:
            col.append(c[0])
        return [dict(zip(col, row)) for row in rows.fetchall()]

    def editCustomer(self, data):
        self.__cur.execute(SQLCommand.editCustomer(data))
        self.__connector.commit()
        return {'Success': True}

    def insertCustomer(self, data):
        self.__cur.execute(SQLCommand.insertCustomer(data))
        self.__connector.commit()
        return {'Success': True}

    def deleteCustomer(self, customerNumber):
        self.__cur.execute(SQLCommand.deleteCustomer(customerNumber))
        self.__connector.commit()
        return {'Success': True}

    # --------------------------------------------------------------------------------------------------------------------------------
    #                                                         Employee
    # --------------------------------------------------------------------------------------------------------------------------------

    def getAllEmployees(self):
        rows = self.__cur.execute(SQLCommand.getAllEmployees())
        col = []
        for c in self.__cur.description:
            if c[0] in col:
                col.append(c[0]+'_reportTo')
            else:
                col.append(c[0])
        return [dict(zip(col, row)) for row in rows.fetchall()]

    def getEmployee(self, employeeNumber):
        rows = self.__cur.execute(SQLCommand.getEmployee(employeeNumber))
        col = []
        for c in self.__cur.description:
            if c[0] in col:
                col.append(c[0]+'_reportTo')
            else:
                col.append(c[0])
        return [dict(zip(col, row)) for row in rows.fetchall()]

    def editEmployee(self, data):
        self.__cur.execute(SQLCommand.editEmployee(data))
        self.__connector.commit()
        return {'Success': True}

    def deleteEmployee(self, employeeNumber):
        self.__cur.execute(SQLCommand.deleteEmployee(employeeNumber))
        self.__connector.commit()
        return {'Success': True}

    # --------------------------------------------------------------------------------------------------------------------------------
    #                                                         Bill
    # --------------------------------------------------------------------------------------------------------------------------------

    def insertUser(self, data):
        if self.getUser(data['username']):
            return {'Success': False, 'code': 'we have username'}
        else:
            user = User(data['username'], data['password'])
            if not user.checkIsUser():
                return {'Success': False, 'code': 'no username or password'}
            self.__cur.execute(SQLCommand.insertUser(user.getUserJson(), data['type']))
            self.__connector.commit()
            return {'Success': True}

SqlApiV1Obj = SqlApiStoreV1('classicmodels.sqlite')
