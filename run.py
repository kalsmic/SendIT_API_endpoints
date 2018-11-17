# run.py
"""This file contains set up for running app in development mode"""
from app import app

app.config.from_object('config.DevelopmentConfig')

if __name__ == "__main__":
    app.run()
