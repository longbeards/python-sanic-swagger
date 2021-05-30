from sanic import Sanic
from sanic.request import Request
from sanic.response import json, HTTPResponse
from sanic_openapi import doc, swagger_blueprint

app = Sanic("My Trial App")
app.blueprint(swagger_blueprint)


@app.get('/name/<name>')
@doc.description('This is a sample description for the name endpoint.')
@doc.consumes(doc.String(name='name'), location='path')
@doc.produces({'Hello': doc.String}, content_type='application/json')
async def get_name(request: Request, name):
    return json({'Hello': name}, status=200)


@app.post('/name')
@doc.description('Sample POST Request')
@doc.consumes(doc.JsonBody({'name': doc.String}), location='body', content_type='application/json')
@doc.produces({'request': {'name': doc.String}}, content_type='application/json')
async def post_name(request: Request):
    return json({'request': request.json})


@app.get('/health')
async def health(request: Request) -> HTTPResponse:
    return json({'Status': 'up'}, status=200)


if __name__ == '__main__':
    app.run()
