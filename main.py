from fastapi import FastAPI, status

app = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK)
async def root():
    """The root endpoint"""
    
    return {
        'message': 'Authentication module v1',
        'status': True
    }


@app.post('/auth/signup', status_code=status.HTTP_201_CREATED)
async def signup():
    """Create a new user"""
    return {
        'message': 'New user signup successful',
        'status': True
    }


@app.post('/auth/login', status_code=status.HTTP_200_OK)
async def login():
    """Login with the credentials of an already signed up user"""
    return {
        'message': 'User login successful',
        'status': True
    }


@app.get('/protected', status_code=status.HTTP_200_OK)
async def protected(qparam: str = ""):
    """Protected route only accessible to loged in users"""
    
    return {
        'message': 'User authorized to access protected route',
        'status': True,
        'query-param': qparam
    }