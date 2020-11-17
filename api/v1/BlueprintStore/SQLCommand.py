from datetime import datetime as dt
from uuid import uuid4
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
        update = []
        for k in data:
            if k == "productCode": # key
                continue
            if type(data[k]) == str:
                update.append(f"{k} = '{data[k]}'")
            elif type(data[k]) == float:
                update.append(f"{k} = {data[k]:.2f}")
            else:
                update.append(f"{k} = {data[k]}")
        update = ', '.join(update)
        return f"""UPDATE products SET {update} WHERE productCode = '{data['productCode']}'"""
        # quantityInStock = data['quantityInStock']; buyPrice = f"{float(data['buyPrice']):.2f}"
        # MSRP = f"{float(data['MSRP']):.2f}"
        # return f"""UPDATE products SET productName = '{data['productName']}', productLine = '{data['productLine']}',
        # productScale = '{data['productScale']}', productVendor = '{data['productVendor']}', productDescrtiption = '{data['productDescrtiption']}',
        # quantityInStock = {quantityInStock}, buyPrice = {buyPrice}, MSRP = {MSRP} WHERE productCode = '{data['productCode']}'"""

    @staticmethod
    def insertProduct(data):
        insert = []
        keyData =[]
        for k in data:
            if k == "productCode": # key
                continue
            if type(data[k]) == str:
                insert.append(f"'{data[k]}'")
            elif type(data[k]) == float:
                insert.append(f"{data[k]:.2f}")
            elif type(data[k]) == int:
                insert.append(f"{data[k]}")
            else:
                insert.append(f"{data[k]}")
        if not data.get('productScale', None):
            insert.append('productScale')
            data['productScale'] = ':'
        scale = data['productScale'].split(':')[1]
        insert = (", " if len(data) else "") + ", ".join(insert)
        keyData = (", " if len(data) else "") + ", ".join(data)
        return f"""INSERT INTO products(productCode{keyData}) SELECT 'S{scale}_'||printf('%04d', ifnull(max(CAST(substr(productCode, -4) as INTEGER)) + 1, 1)){insert}
        FROM products WHERE productCode like 'S{scale}_%'"""

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
        update = []
        for k in data:
            if k == "customerNumber": # key
                continue
            if type(data[k]) == str:
                update.append(f"{k} = '{data[k]}'")
            elif type(data[k]) == float:
                update.append(f"{k} = {data[k]:.2f}")
            else:
                update.append(f"{k} = {data[k]}")
        update = ', '.join(update)
        return f"""UPDATE customers SET {update} WHERE customerNumber = {data['customerNumber']}"""
        # old
        # creditLimit = f"{float(data['creditLimit']):.2f}"; salesRepEmployeeNumber = int(data['salesRepEmployeeNumber'])
        # return f"""UPDATE customers SET customerName = '{data['customerName']}', contactLastName = '{data['contactLastName']}', contactFirstName = '{data['contactFirstName']}',
        # phone = '{data['phone']}', addressLine1 = '{data['addressLine1']}', addressLine2 = '{data['addressLine2']}',
        # city = '{data['city']}', state = '{data['state']}', postalCode = '{data['postalCode']}', country = '{data['country']}',
        # salesRepEmployeeNumber = {salesRepEmployeeNumber}, creditLimit = {creditLimit}
        # WHERE customerNumber = {data['customerNumber']}"""

    @staticmethod
    def insertCustomer(data):
        insert = []
        for k in data:
            if k == "customerNumber": # key
                continue
            if type(data[k]) == str:
                insert.append(f"'{data[k]}'")
            elif type(data[k]) == float:
                insert.append(f"{data[k]:.2f}")
            else:
                insert.append(f"{data[k]}")
        insert = (", " if len(data) else "") + ", ".join(insert)
        keyData = (", " if len(data) else "") + ", ".join(data)
        return f"""INSERT INTO customers(customerNumber{keyData}) SELECT max(customerNumber)+1{insert} from customers;"""

    @staticmethod
    def deleteCustomer(customerNumber):
        return f"""DELETE FROM customers WHERE customerNumber = {customerNumber};"""

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
        update = []
        for k in data:
            if k == "employeeNumber": # key
                continue
            if type(data[k]) == str:
                update.append(f"{k} = '{data[k]}'")
            elif type(data[k]) == float:
                update.append(f"{k} = {data[k]:.2f}")
            elif type(data[k]) == int:
                update.append(f"{data[k]}")
            else:
                update.append(f"{k} = {data[k]}")
            update = ', '.join(update)
        return f"""UPDATE employees SET {update} WHERE employeeNumber = {data['employeeNumber']}"""
        # return f"""UPDATE employees SET lastName = '{data['lastName']}', firstName = '{data['firstName']}',
        # extension = '{data['extension']}', email = '{data['email']}', officeCode = {data['officeCode']},
        # reportsTo = {data['reportsTo']}, jobTitle = '{data['jobTitle']}' WHERE employeeNumber = {data['employeeNumber']}"""

    @staticmethod
    def deleteEmployee(employeeNumber):
        return f"""DELETE FROM employees WHERE employeeNumber = {employeeNumber}"""
    
    @staticmethod
    def insertEmployee(data):
        keyData = []
        insert = []
        for k in data:
            if k == "employeeNumber": # key
                continue
            if type(data[k]) == str:
                insert.append(f"'{data[k]}'")
            elif type(data[k]) == float:
                insert.append(f"{data[k]:.2f}")
            elif type(data[k]) == int:
                insert.append(f"{data[k]}")
            else:
                insert.append(f"{data[k]}")
        insert = (", " if len(data) else "") + ", ".join(insert)
        keyData = (", " if len(data) else "") + ", ".join(data)
        return f"""INSERT INTO employees(employeeNumber{keyData}) SELECT max(employeeNumber)+1{insert} from employees"""

    # --------------------------------------------------------------------------------------------------------------------------------
    #                                                         Bill
    # --------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def getAllBill():
        return f"""SELECT * FROM orders"""

    @staticmethod
    def getDetailBill(orderNumber):
        return f"""SELECT * FROM orderdetails WHERE orderNumber={orderNumber} """

    @staticmethod
    def editBill(data, cursor, connector):
        if data['status'] == 'Cancelled':
            rows = cursor.execute(SQLCommand.getDetailBill(data['orderNumber']))
            col = []
            for c in cursor.description:
                if c[0] in col:
                    col.append(c[0])
                else:
                    col.append(c[0])
            rows = [dict(zip(col, row)) for row in rows.fetchall()]
            price = 0
            for r in rows:
                price += r['quantityOrdered'] * r['priceEach']
            cursor.execute(f"""UPDATE customers SET creditLimit=creditLimit+{price} WHERE customerNumber={data['customerNumber']};""")
            connector.commit()
        update = []
        for k in data:
            if k == "orderNumber": # key
                continue
            if type(data[k]) == str:
                update.append(f"{k} = '{data[k]}'")
            elif type(data[k]) == float:
                update.append(f"{k} = {data[k]:.2f}")
            elif type(data[k]) == int:
                update.append(f"{k} = {data[k]}")
            else:
                update.append(f"{k} = {data[k]}")
        update = ', '.join(update)
        return f"""UPDATE orders SET {update} WHERE orderNumber = {data['orderNumber']}"""

    @staticmethod
    def insertBill(data, cursor, connector):
        customerNumber = data['customerNumber']
        requiredDate = data['requiredDate']
        comments = data['comments']
        cart = data['cart']
        dateNow = dt.now().strftime('%Y-%m-%d')
        command = f"""INSERT INTO orders(orderNumber, orderDate, requiredDate, status, comments, customerNumber)
        SELECT max(orderNumber)+1, '{dateNow}', '{requiredDate}', 'In Process', '{comments}', {customerNumber} from orders;
        """
        cursor.execute(command)
        for i, c in enumerate(cart, 1):
            command = f"""
            INSERT INTO orderdetails(orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber) SELECT max(o.orderNumber), '{cart[c]['productCode']}', {cart[c]['value']}, {cart[c]['buyPrice']}, {i} from orders as o;
            """
            cursor.execute(command)
            print(cart[c]['value'])
            command2 = f"""UPDATE products SET quantityInStock=quantityInStock-{cart[c]['value']} WHERE productCode LIKE '{cart[c]['productCode']}';"""
            cursor.execute(command2)
        command = f"""UPDATE customers SET creditLimit=creditLimit-{data['price']} WHERE customerNumber={customerNumber};"""
        cursor.execute(command)
        checkNumber = str(uuid4()).split('-')[0].upper()
        command = f"""INSERT INTO payments(customerNumber, checkNumber, paymentDate, amount) SELECT {customerNumber}, '{checkNumber}', '{dateNow}', {data['price']};"""
        cursor.execute(command)
        connector.commit()

    # --------------------------------------------------------------------------------------------------------------------------------
    #                                                      Stock-in System
    # --------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def getAllStockIn():
        return f"""SELECT * FROM stockIn"""

## frontend filter  
    # @staticmethod
    # def getProductStock(productCode):
    #     return f"""SELECT * FROM stockIn WHERE productCode = '{productCode}'"""

    # @staticmethod
    # def getDateStock(date):
    #     return f"""SELECT * FROM stockIn WHERE date = '{date}'"""

    # employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle
    # @staticmethod
    # def editStockIn(data):
    #     return f"""UPDATE stockIn SET amount = {data['amount']} WHERE productCode = '{data['productCode']}' AND date = '{data['date']}' """

    # @staticmethod
    # def deleteStockIn(data):
    #     return f"""DELETE FROM stockIn WHERE productCode = '{data['productCode']}' AND date = '{data['date']}';
    #         UPDATE products SET quantityInStock = quantityInStock - {data['amount']} WHERE productCode = '{data['productCode']}';"""

    @staticmethod
    def insertStockIn(data, cursor, connector):
        command = f"""INSERT INTO stockIn(date, productCode, amount) SELECT '{dt.now().strftime('%Y-%m-%d')}', '{data['productCode']}', {data['quantityInStock']};"""
        cursor.execute(command)
        command = f"""UPDATE products SET quantityInStock = quantityInStock + {data['quantityInStock']} WHERE productCode = '{data['productCode']}';"""
        cursor.execute(command)
        connector.commit()

    # --------------------------------------------------------------------------------------------------------------------------------
    #                                                         Promotion
    # --------------------------------------------------------------------------------------------------------------------------------

    @staticmethod
    def insertPromotion(data):
        for d in data:
            f"""INSERT INTO promotion (promoCode, startDate, endDate, discount, description, is1get1) VALUES ('{user['username']}', '{user['hashedPassword']}', '{user['salt']}', '{typeData}')"""
        return