from subprocess import getoutput 
from json import loads
from os import readlink , getppid

class Horus():
    """
    Horus, The son of Isis & Osiris (The one who is above).
    The class refers to the core of the fetcher script.
    """    

    def __init__(self) -> None:
        self.get_data()
        self.line = len(self.user + self.host) + 1 

    def _get_user_data(self) -> None :
        """
        Gets username & hostname

        Returns:
            A string represnting user name.
        """    
        self.user =  getoutput("whoami")

    def _get_uptime(self) -> None :
        """
        Gets uptime. 

        Returns:
            A string represnting uptime.
        """    
        self.uptime = getoutput("uptime -p")[3:].replace("," , " &")

    def _get_ram(self) -> None :
        """
        Get memory status

        Returns:
            A tuple having total and used memory.
        """    
        self.ram = getoutput("free --mega | awk 'NR == 2 { print $3\" / \"$2\" MB\" }'")

    def _get_shell(self) -> None:
        """
        Determine which shell invoked the script.

        Returns:
            A string represnting shell name.
        """    
        self.shell = readlink(f"/proc/{getppid()}/exe").rsplit("/")[-1].capitalize()

    def _get_OS(self) -> None :
        """
        Determine some OS data like, host name , kernel name , kernel version and OS name.

        Returns:
            A dictionary repersenting the mentioned data.
        """        
        data = "{" + getoutput("hostnamectl --json=pretty | grep -e 'KernelName' -e 'KernelRelease' -e 'Hostname' -e 'OperatingSystemPrettyName' -w").replace("\n" , "").replace("\t",'')[:-1] + "}" 
        data = loads(data)
        self.host = data['Hostname']
        self.kernel_name = data['KernelName']
        self.kernel_release = data['KernelRelease']
        self.os = data['OperatingSystemPrettyName']

    def _get_pkgs(self) -> None : 
        """
        Get Number of pacman's Packages
        #! Note : it only checks pacman for now.

        Returns:
            An integer that represents pacman Pkgs.
        """        
        self.pkgs =  int(getoutput('pacman -Q | wc -l'))

    def _get_cpu(self) -> None : 
        """
        Gets CPU model name and its frequency. 
        """        
        cpu = getoutput("cat /proc/cpuinfo | grep -e 'model name' -e 'cpu MHz'").splitlines()[0:2]
        self.cpu_model  = cpu[0].split(':')[-1].strip()
        self.cpu_freq  = round(float(cpu[1].split(':')[-1])/1000,1)
        
    def get_data(self) -> None :
        """
        The driver code for the class.
        """        
        self._get_user_data()
        self._get_uptime()
        self._get_ram()
        self._get_shell()
        self._get_OS()
        self._get_pkgs()
        self._get_cpu()

if __name__ == "__main__": 
    pass