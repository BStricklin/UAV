from ServerSocket import *
from CMD_LINE import *

command_dict = {
    'Altitude': '0.0',
    'Roll': '0.0',
    'Pitch' : '0.0',
    'Yaw' : '0.0'
}


if __name__ == "__main__":
    quadTcpThread = MyTcpServerThread()
    quadTcpThread.initialize(command_dict)
        
    quadCmdLine = TurtleShell()
    quadCmdLine.commThread = quadTcpThread
    quadCmdLine.command_dict = command_dict
    
    quadTcpThread.start()
    quadCmdLine.cmdloop()

