# Main
# Starts the PhotoBooth application

from wx import App

from MainController import MainController

if __name__ == "__main__":
    # create the wx app
    app = App(False)
    # pass the app to the controller
    mainController = MainController(app)
    # start the app running
    app.MainLoop()
