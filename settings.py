import os 
from pathlib import Path
import environ

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = env('SCRETA_KEY')
DEBUG = env('DEBUG', default=False)