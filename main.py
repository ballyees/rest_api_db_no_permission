from sanic import Sanic
from api.v1.BlueprintUser.blueprintSQL import bp_v1_user
from api.v1.BlueprintStore.blueprintSQL import bp_v1_store
from sanic_cors import CORS

app = Sanic('projectDB')

app.blueprint(bp_v1_user)
app.blueprint(bp_v1_store)

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 8000
    try:
        app.run(host=host, port=port, auto_reload=True)
        raise Exception('Stop server')
    except (Exception, KeyboardInterrupt, SystemExit) as e:
        print(e)