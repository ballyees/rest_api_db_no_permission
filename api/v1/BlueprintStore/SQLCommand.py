class SQLCommand:
    @staticmethod
    def getUser(username):
        return f"""SELECT * FROM users WHERE username like '{username}'"""
    
    @staticmethod
    def getAllProducts():
        return f"""SELECT * FROM products"""

    @staticmethod
    def getProduct(productCode):
        return f"""SELECT * FROM products WHERE productCode = '{productCode}'"""

    @staticmethod
    def deleteProduct(productCode):
        return f"""DELETE FROM products WHERE productCode = '{productCode}'"""

    @staticmethod
    def editProduct(data):
        quantityInStock = int(data['quantityInStock']); buyPrice = float(f"{float(data['buyPrice']):.2f}")
        MSRP = float(f"{float(data['MSRP']):.2f}")
        return f"""UPDATE products SET productName = '{data['productName']}', productLine = '{data['productLine']}',
        productScale = '{data['productScale']}', productVendor = '{data['productVendor']}', productDescrtiption = '{data['productDescrtiption']}',
        quantityInStock = {quantityInStock}, buyPrice = {buyPrice}, MSRP = {MSRP} WHERE productCode = '{data['productCode']}'"""

    @staticmethod
    def getAllCustomers():
        return f"""SELECT * FROM customers LEFT JOIN employees ON salesRepEmployeeNumber = employeeNumber"""

    @staticmethod
    def insertUser(user, typeData='common'):
        return f"""INSERT INTO users (username, hashedPassword, salt, type) VALUES ('{user['username']}', '{user['hashedPassword']}', '{user['salt']}', '{typeData}')"""