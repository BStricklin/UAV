import cmd, sys
from turtle import *
import threading

class CmdLineThread(threading.Thread):
    enabled = False

    def __init__(self):
        while not self.enabled:
            try:
                # Create the command line interface
                self.TurtleObject = TurtleShell()
                self.enabled = True
                threading.Thread.__init__(self)
            except:
                self.enabled = False

    def initialize(self, command_dict):
        self.TurtleObject.command_dict = command_dict

    def run(self):
        self.TurtleObject.cmdloop() 

class TurtleShell(cmd.Cmd):
    intro = 'Welcome to QuadSim.   Type help or ? to list commands.\n'
    prompt = '(QuadSim v0.1) '
    file = None
    socket = None
    command_dict = {}
    commThread = None

    # ----- basic turtle commands -----
    def do_bye(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print('Thank you for using Turtle')
        self.commThread.MyServerObject.shutdown()
        bye()
        return True
    def do_altitude(self, arg):
	self.command_dict['Altitude'] = self.parse(arg)[0]
    def do_roll(self, arg):
	self.command_dict['Roll'] = self.parse(arg)[0]
    def do_pitch(self, arg):
	self.command_dict['Pitch'] = self.parse(arg)[0]
    def do_yaw(self, arg):
	self.command_dict['Yaw'] = self.parse(arg)[0]
    def parse(self, arg):
    	'Convert a series of zero or more numbers to an argument tuple'
    	return tuple(map(int, arg.split()))

if __name__ == '__main__':
    TurtleShell().cmdloop()

    
