# server/config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Use URL-encoded password (peach#077 => peach%23077)
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:peach%23077@localhost:5432/late_show_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'super-secret-key'  # Replace with a strong, secure key in production
