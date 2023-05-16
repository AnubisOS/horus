from subprocess import getoutput 
from json import loads
from os import readlink , getppid


class Horus():
    """
    Horus, The Son of Isis & Osiris (The one who is above).
    The class refers to the core of the fetcher script.
    """    

    def __init__(self) -> None:
        self.user = self.get_user_data()
        self.uptime = self.get_uptime()
        self.ram = self.get_ram()
        self.shell = self.get_shell()
        self.host ,  \
        self.kernel_name , \
        self.kernel_release , \
        self.os = self.get_OS()
        self.line = len(self.user + self.host) +1 

    def get_user_data(self) -> str :
        """
        Gets username & hostname

        Returns:
            A string represnting user name.
        """    
        return getoutput("whoami")

    def get_uptime(self) -> str :
        """
        Gets uptime. 

        Returns:
            A string represnting uptime.
        """    
        return getoutput("uptime -p")[3:].replace("," , " &")

    def get_ram(self) -> str :
        """
        Get memory status

        Returns:
            A tuple having total and used memory.
        """    
        return getoutput("free --mega | awk 'NR == 2 { print $3\" / \"$2\" MB\" }'")

    def get_shell(self) -> str:
        """
        Determine which shell invoked the script.

        Returns:
            _description_
        """    
        return readlink(f"/proc/{getppid()}/exe").rsplit("/")[-1].capitalize()

    def get_OS(self) -> dict :
        """
        Determine some OS data like, host name , kernel name , kernel version and OS name.

        Returns:
            A dictionary repersenting the mentioned data.
        """        
        data = "{" + getoutput("hostnamectl --json=pretty | grep -e 'KernelName' -e 'KernelRelease' -e 'Hostname' -e 'OperatingSystemPrettyName' -w").replace("\n" , "").replace("\t",'')[:-1] + "}" 
        data = loads(data)
        return data.values()


if __name__ == "__main__": 
    pass