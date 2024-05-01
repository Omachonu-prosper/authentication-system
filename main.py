from fastapi import FastAPI, status

app = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK)
async def root():
    return {
        'message': 'Authentication module v1',
        'status': True
    }


@app.post('/signup', status_code=status.HTTP_201_CREATED)
async def signup():
    return {
        'message': 'New user signup successful',
        'status': True
    }


@app.post('/login', status_code=status.HTTP_200_OK)
async def login():
    return {
        'message': 'User login successful',
        'status': True
    }


@app.get('/protected', status_code=status.HTTP_200_OK)
async def protected():
    return {
        'message': 'User authorized to access protected route',
        'status': True
    }