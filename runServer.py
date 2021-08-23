from server import MainServer
from mouseController import MouseController


if __name__ == "__main__":
    print("Starting server")
    HOST = "192.168.1.2"
    # HOST = "localhost"
    click_port = 5793
    scroll_port = 5794
    motion_port = 5795
    command_port = 5796

    dt = 1.0 / 60.0
    mouseController = MouseController(dt)

    main_server = MainServer(mouseController,
                             HOST,
                             click_port,
                             scroll_port,
                             motion_port,
                             command_port)
    main_server.run()
