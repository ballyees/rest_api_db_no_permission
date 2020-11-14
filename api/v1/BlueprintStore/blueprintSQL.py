from sanic import Blueprint
from sanic.response import json, stream
from .SQLite import SqlApiV1Obj
from ..loggingFile import Logger
from ..configure import ConfigureAPI


bp_v1_store = Blueprint('store_v1', url_prefix='/api/store', version="v1")

@bp_v1_store.listener('after_server_stop')
async def close_connection(app, loop):
    await SqlApiV1Obj.close()

# --------------------------------------------------------------------------------------------------------------------------------
#                                                         Product
# --------------------------------------------------------------------------------------------------------------------------------
# @bp_v1_store.route('/', methods=["POST"])
# async def test(request):
#     data = request.json
#     for k in data:
#         print(type(data[k]), data[k])
#     return json({ConfigureAPI.keyResponseData: True})

@bp_v1_store.route('/product', methods=["GET", "POST"])
async def productAll(request):
    if request.method == "GET":
        res = SqlApiV1Obj.getAllProducts()
        return json({ConfigureAPI.keyResponseData: res})
    elif request.method == "POST":
        res = SqlApiV1Obj.insertProduct(request.json)
        return json({ConfigureAPI.keyResponseData: res})

@bp_v1_store.route('/product/<productCode>', methods=["GET", "PUT", "DELETE"])
async def product(request, productCode):
    if request.method == "GET":
        res = SqlApiV1Obj.getProduct(productCode)
        return json({ConfigureAPI.keyResponseData: res})
    elif request.method == "PUT":
        res = SqlApiV1Obj.editProduct(request.json)
        return json({ConfigureAPI.keyResponseData: res})
    elif request.method == "DELETE":
        res = SqlApiV1Obj.editProduct(productCode)
        return json({ConfigureAPI.keyResponseData: res})

# --------------------------------------------------------------------------------------------------------------------------------
#                                                         Customer
# --------------------------------------------------------------------------------------------------------------------------------
@bp_v1_store.route('/customer', methods=["GET", "POST"])
async def customerAll(request):
    if request.method == "GET":
        res = SqlApiV1Obj.getAllCustomers()
        return json({ConfigureAPI.keyResponseData: res})
    elif request.method == "POST":
        res = SqlApiV1Obj.insertCustomer(request.json)
        return json({ConfigureAPI.keyResponseData: res})

@bp_v1_store.route('/customer/<customerNumber>', methods=["GET", "PUT", "DELETE"])
async def customer(request, customerNumber):
    if request.method == "GET":
        res = SqlApiV1Obj.getCustomer(customerNumber)
        return json({ConfigureAPI.keyResponseData: res})
    elif request.method == "PUT":
        res = SqlApiV1Obj.editCustomer(request.json)
        return json({ConfigureAPI.keyResponseData: res})
    elif request.method == "DELETE":
        res = SqlApiV1Obj.deleteCustomer(customerNumber)
        return json({ConfigureAPI.keyResponseData: res})

# --------------------------------------------------------------------------------------------------------------------------------
#                                                         Employee
# --------------------------------------------------------------------------------------------------------------------------------
@bp_v1_store.route('/employee', methods=["GET"])
async def customerAll(request):
    res = SqlApiV1Obj.getAllEmployees()
    return json({ConfigureAPI.keyResponseData: res})

@bp_v1_store.route('/employee/<employeeNumber>', methods=["GET", "PUT", "DELETE"])
async def customer(request, employeeNumber):
    if request.method == "GET":
        res = SqlApiV1Obj.getEmployee(employeeNumber)
        return json({ConfigureAPI.keyResponseData: res})
    elif request.method == "PUT":
        res = SqlApiV1Obj.editEmployee(request.json)
        return json({ConfigureAPI.keyResponseData: res})
    elif request.method == "DELETE":
        res = SqlApiV1Obj.deleteEmployee(employeeNumber)
        return json({ConfigureAPI.keyResponseData: res})

# --------------------------------------------------------------------------------------------------------------------------------
#                                                         Bill
# --------------------------------------------------------------------------------------------------------------------------------

@bp_v1_store.route('/<officeCode>', methods=["GET", "PUT"])
async def userGET(request, officeCode):
    if request.method == "GET":
        if not request.headers.get(ConfigureAPI.keyTokenHeader, None):
            Logger.write(f'IP {request.socket} [no token]', 'request-data')
            return json({'exception': 'Authentication Failed', 'code': 1, 'description': 'none token'}, status=401) 
        elif TokenizerUser.checkTokenAndName(request.headers['token'], officeCode):
            Logger.write(f'IP {request.socket} [{officeCode} query data]', 'request-data')
            res = SqlApiV1Obj.getUser(officeCode)
            del res[0]['salt']
            return json({
                "responseData": res
            })
        elif not TokenizerUser.checkToken(request.headers[ConfigureAPI.keyTokenHeader]):
            Logger.write(f'IP {request.socket} [unknown token]', 'request-data')
            return json({'exception': 'Authentication Failed', 'code': 2, 'description': 'wrong token'}, status=401)
        else:
            Logger.write(f'IP {request.socket[0]} [{officeCode} use unknown token]', 'request-data')
            return json({'exception': 'Authentication Failed', 'code': 3, 'description': 'permission deined'}, status=401)
            
