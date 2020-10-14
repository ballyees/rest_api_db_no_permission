from sanic import Blueprint
from sanic.response import json, stream
from .SQLite import SqlApiV1Obj
from ..loggingFile import Logger
from ..configure import ConfigureAPI
bp_v1_user = Blueprint('user_v1', url_prefix='/api/user', version="v1")

@bp_v1_user.listener('after_server_stop')
async def close_connection(app, loop):
    SqlApiV1Obj.closeDB()

@bp_v1_user.route('/<username>', methods=["GET", "PUT", "DELETE"])
async def userOne(request, username):
    if request.method == "GET":
        res = SqlApiV1Obj.getUser(username)
        if res:
            del res[0]['salt']
        return json({ ConfigureAPI.keyResponseData: res })
    elif request.method == "PUT":
        data = request.json
        res = SqlApiV1Obj.editUser(username, data)
        return json({ ConfigureAPI.keyResponseData: res }, status=res['status'])
    elif request.method == "DELETE":
        res =SqlApiV1Obj.deleteUser(username)
        return json({ ConfigureAPI.keyResponseData: res })

@bp_v1_user.route('/', methods=["POST", "GET"])
async def userAll(request):
    if request.method == 'POST':
        data = request.json
        res = SqlApiV1Obj.insertUser(data)
        return json({ ConfigureAPI.keyResponseData: res }, status=res['status'])
    elif request.method == 'GET':
        res = SqlApiV1Obj.getUserAll()
        return json({ ConfigureAPI.keyResponseData: res })

@bp_v1_user.route('/login', methods=["POST"])
async def userLogin(request):
    data = request.json
    responseLogin = await SqlApiV1Obj.loginAuthentication(data)
    if responseLogin['Success']:
        Logger.write(f'IP {request.socket[0]} [{data[ConfigureAPI.keyRequestUsername]} login to server successful]', 'Login')
        del responseLogin[ConfigureAPI.keyResponseData][0][ConfigureAPI.keyQueryUsersSalt]
        responseData = responseLogin[ConfigureAPI.keyResponseData]
        responseData[0][ConfigureAPI.keyRequestHeaderLogoutType] = ConfigureAPI.keyResponseLoginType[responseData[0][ConfigureAPI.keyQueryUsersType]]
        return json({ ConfigureAPI.keyResponseData: responseData })
    else:
        Logger.write(f'IP {request.socket[0]} [{data.get(ConfigureAPI.keyRequestUsername, "Unknown")} try login to server]', 'Login')
        return json(responseLogin, status=400)

