# Virtual environment em Python (venv)
# A virtual environment carries all your Python installation to another folder on the choose path.
# When you start a virtual environment, its installation will be used. 
# venv is the module name that you are going to use to create virtual environments.
# You can name it as whatever you want, but the most common are venv env .venv .env.
#
# How to create virtual environments
# Open your project's folder on terminal and type:
# python -m venv venv
#
# Starting and stopping my virtual environment
# Windows: .\venv\Scripts\activate
# Linux and Mac: source venv/bin/activate
# To stop: deactivate
#
# pip - installing packages and libraries
# To install the last version:
# pip install package_name
# To install a specific version
# (there's also another not mentioned ways)
# pip install package_name==0.0.0
# To uninstall a package
# pip uninstall package_name
# Freeze (list packages)
# pip freeze
#
# Creating and using a requirements.txt
# pip freeze > requirements.txt
# Installing everything from the requirements.txt
# pip install -r requirements.txt