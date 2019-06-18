import os
import sys

# Function to open app
def openApp(app):
    try:
        # Change the directory to desktop which contains app
        os.chdir('C:\\Users\\sjonl\\Desktop')
        # open the app
        os.startfile(app)
    
    except Exception as e:
        print(str(e))


# Take the name of app from command line argument
script, app_to_open = sys.argv
# Give the app name as argument to opefile function
openApp(app_to_open)
