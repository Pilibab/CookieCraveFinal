# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import configs
app = FastAPI(
    title="CookieKrave API",
    version="1.0.0"
)

# Define the origins (URLs) that are allowed to talk to your backend
origins = [
    configs.NEXT_PUBLIC_API_FRONTEND_URL.get_secret_value()
    #TODO: add production domain (e.g., "https://cookiekrave.com"), should the app be online
]

# Add the middleware to the FastAPI app instance
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allows requests from your frontend ports
    allow_credentials=True,       # Allows frontend to send cookies/auth headers
    allow_methods=["*"],          # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],          # Allows all HTTP headers
)

# Register your router here

@app.get("/")
def root():
    return {"message": "Welcome to CookieKrave Backend API!"}