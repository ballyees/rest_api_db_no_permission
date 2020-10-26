class SQLCommand:
    # --------------------------------------------------------------------------------------------------------------------------------
    #                                                         Product
    # --------------------------------------------------------------------------------------------------------------------------------

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

    # --------------------------------------------------------------------------------------------------------------------------------
    #                                                         Customer
    # --------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def getAllCustomers():
        return f"""SELECT * FROM customers LEFT JOIN employees ON salesRepEmployeeNumber = employeeNumber"""
    
    @staticmethod
    def getCustomer(customerNumber):
        return f"""SELECT * FROM customers LEFT JOIN employees ON salesRepEmployeeNumber = employeeNumber WHERE customerNumber = {customerNumber}"""
    
    @staticmethod
    def editCustomer(data):
        creditLimit = float(f"{float(data['creditLimit']):.2f}"); salesRepEmployeeNumber = int(data['salesRepEmployeeNumber'])
        return f"""UPDATE customers SET customerName = '{data['customerName']}', contactLastName = '{data['contactLastName']}', contactFirstName = '{data['contactFirstName']}',
        phone = '{data['phone']}', addressLine1 = '{data['addressLine1']}', addressLine2 = '{data['addressLine2']}',
        city = '{data['city']}', state = '{data['state']}', postalCode = '{data['postalCode']}', country = '{data['country']}',
        salesRepEmployeeNumber = {salesRepEmployeeNumber}, creditLimit = {creditLimit}
        WHERE customerNumber = {data['customerNumber']}"""

    @staticmethod
    def deleteCustomer(customerNumber):
        return f"""DELETE FROM customers WHERE customerNumber = {customerNumber}"""

    # --------------------------------------------------------------------------------------------------------------------------------
    #                                                         Employee
    # --------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def getAllEmployees():
        return f"""SELECT e.employeeNumber, e.lastName, e.firstName, e.extension, e.email, e.officeCode, e.reportsTo, e2.lastName, e2.firstName, e.jobTitle
        FROM employees as e LEFT JOIN employees as e2 ON e.reportsTo = e2.employeeNumber"""
    
    @staticmethod
    def getEmployee(employeeNumber):
        return f"""SELECT e.employeeNumber, e.lastName, e.firstName, e.extension, e.email, e.officeCode, e.reportsTo, e2.lastName, e2.firstName, e.jobTitle
        FROM employees as e LEFT JOIN employees as e2 ON e.reportsTo = e2.employeeNumber WHERE e.employeeNumber = {employeeNumber}"""
    # employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle
    @staticmethod
    def editEmployee(data):
        return f"""UPDATE employees SET lastName = '{data['lastName']}', firstName = '{data['firstName']}',
        extension = '{data['extension']}', email = '{data['email']}', officeCode = {data['officeCode']},
        reportsTo = {data['reportsTo']}, jobTitle = '{data['jobTitle']}' WHERE employeeNumber = {data['employeeNumber']}"""

    @staticmethod
    def deleteEmployee(employeeNumber):
        return f"""DELETE FROM employees WHERE employeeNumber = {employeeNumber}"""

    # --------------------------------------------------------------------------------------------------------------------------------
    #                                                         Bill
    # --------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def insertUser(user, typeData='common'):
        return f"""INSERT INTO users (username, hashedPassword, salt, type) VALUES ('{user['username']}', '{user['hashedPassword']}', '{user['salt']}', '{typeData}')"""