from .papyri import Horus
from configparser import ConfigParser 
from os import environ as env

class obelisk() :
    """
    This is a insdie joke, Where the obelisk is where ancient egyptians wrote.
    The class refers to the screen area of the script.
    """    
    def __init__(self) -> None:
        self.BG , self.FG = self._config()
        self.horus = Horus()


    def carve(self) -> None :
        """
        Carving ( because pf obelisk, get it ? ) the system requirments on the screen. 
        """        
        print(f"\t{self.horus.user}@{self.horus.host}")
        print(f"\t{'-' * self.horus.line}")
        print(f"\t OS     : {self.horus.os}")
        print(f"\t󰌢 Kernel : {self.horus.kernel_name} {self.horus.kernel_release}")
        print(f"\t󱑏 Uptime : {self.horus.uptime}")
        print(f"\t Shell  : {self.horus.shell}")
        print(f"\t Ram    : {self.horus.ram}")
        
    def make_background(self) -> None :
        """
        Prints the ANSI background color code.
        """        
        print("\x1b[48;2;{};{};{}m".format(*self.BG),end="")

    def make_foreground(self) -> None :
        """
        Prints the ANSI font color code.
        """        
        print("\x1b[38;2;{};{};{}m".format(*self.FG))

    def destruct(self) -> None : 
        """
        Prints the ANSI reset code.
        """        
        print("\x1b[0m")

    def _config(self , config_path = "".join((env.get("HOME"),'/.config/horus/papyri.cfg'))) -> dict :
        """
        Gets the configurations from the cfg file

        Keyword Arguments:
            config_path -- path to cf file  (default: {"".join((env.get("HOME"),'/.config/horus/papyri.cfg'))})

        Returns:
            Tuple of Background Color and Foreground Color
        """        
        config = ConfigParser()
        config.read(config_path)
        current_config = config.sections()
        BG = self._str_to_tuple(config[current_config[0]]['BG'])
        FG = self._str_to_tuple(config[current_config[0]]['FG'])
        
        return (BG , FG)
    
    def _str_to_tuple(self , string:str) -> tuple[int] : 
        """
        Helper metthod to format the color string into a RGB tuple. 

        Arguments:
            string -- tuple in form of string

        Returns:
            Tuple of integers. 
        """        
        string = string.strip("()")
        return tuple(map(int, string.split(",")))
