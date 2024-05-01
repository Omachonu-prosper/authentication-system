from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {
        'message': 'Authentication module v1',
        'status': True
    }