from .papyri import Horus

class obelisk() :
    """
    This is a insdie joke, Where the obelisk is where ancient egyptians wrote.
    The class refers to the screen area of the script.
    """    
    def __init__(self, BG=(0,0,0) , FG=(235, 203, 139)) -> None:
        self.BG , self.FG= BG , FG  
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

