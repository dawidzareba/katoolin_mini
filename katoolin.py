import os
import sys
import traceback

if os.getuid() != 0:
    print("Sorry. This script requires sudo privledges")
    sys.exit()


def main():
    try:
        print(
            """

 $$\   $$\             $$\                         $$\ $$\           
 $$ | $$  |            $$ |                        $$ |\__|          
 $$ |$$  /  $$$$$$\  $$$$$$\    $$$$$$\   $$$$$$\  $$ |$$\ $$$$$$$\  
 $$$$$  /   \____$$\ \_$$  _|  $$  __$$\ $$  __$$\ $$ |$$ |$$  __$$\ 
 $$  $$<    $$$$$$$ |  \033[1;36mKali linux tools installer\033[1;m |$$ |$$ |$$ |  $$ |
 \033[1;36m$$ |\$$\  $$  __$$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |$$ |$$ |  $$ |
 $$ | \$$\ \$$$$$$$ |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$ |  $$ |
 \__|  \__| \_______|   \____/  \______/  \______/ \__|\__|\__|  \__| V2.0 \033[1;m


 \033[1;32m+ -- -- +=[ Author: LionSec | Homepage: www.neodrix.com\033[1;m
 \033[1;32m+ -- -- +=[ 331 Tools \033[1;m


\033[1;91m[W] Before updating your system , please remove all Kali-linux repositories to avoid any kind of problem .\033[1;m
        """
        )

        def inicio1():
            while True:
                opcion0 = input(
                    """
                1) Add Kali repositories & Update 
                2) Install classicmenu indicator
                3) Install Kali menu
                4) Help
                """
                )

                while opcion0 == "1":
                    repo = input(
                        """
                    1) Add kali linux repositories
                    2) Update
                    3) Remove all kali linux repositories
                    4) View the contents of sources.list file
                    """
                    )
                    if repo == "1":
                        os.system(
                            "apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6"
                        )
                        os.system(
                            "echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali "
                            "kali-rolling main contrib non-free' >> /etc/apt/sources.list"
                        )
                    elif repo == "2":
                        os.system("apt-get update -m")
                    elif repo == "3":
                        infile = "/etc/apt/sources.list"
                        outfile = "/etc/apt/sources.list"

                        delete_list = [
                            "# Kali linux repositories | Added by Katoolin\n",
                            "deb http://http.kali.org/kali kali-rolling main contrib non-free\n",
                        ]
                        fin = open(infile)
                        os.remove("/etc/apt/sources.list")
                        fout = open(outfile, "w+")
                        for line in fin:
                            for word in delete_list:
                                line = line.replace(word, "")
                            fout.write(line)
                        fin.close()
                        fout.close()
                        print("All kali linux repositories have been deleted !\n")
                    elif repo == "back":
                        inicio1()
                    elif repo == "gohome":
                        inicio1()
                    elif repo == "4":
                        file = open("/etc/apt/sources.list", "r")

                        print(file.read())

                    else:
                        print("Sorry, that was an invalid command!")

                if opcion0 == "3":
                    print(
                        """ 
                        ClassicMenu Indicator is a notification area applet (application indicator) for the top panel of Ubuntu's Unity desktop environment.
                        
                        It provides a simple way to get a classic GNOME-style application menu for those who prefer this over the Unity dash menu.
                        
                        Like the classic GNOME menu, it includes Wine games and applications if you have those installed.
                        
                        For more information , please visit : http://www.florian-diesch.de/software/classicmenu-indicator/
                        
                        """
                    )
                    repo = input(
                        "Do you want to install classicmenu indicator ? [y/n]>"
                    )
                    if repo == "y":
                        os.system(
                            "add-apt-repository ppa:diesch/testing && apt-get update"
                        )
                        os.system("sudo apt-get install classicmenu-indicator")

                elif opcion0 == "4":
                    repo = input("Do you want to install Kali menu ? [y/n]>")
                    if repo == "y":
                        os.system("apt-get install kali-menu")
                elif opcion0 == "5":
                    print(
                        """ 
****************** +Commands+ ******************


\033[1;32mback\033[1;m 	\033[1;33mGo back\033[1;m

\033[1;32mgohome\033[1;m	\033[1;33mGo to the main menu\033[1;m

        """
                    )

        inicio1()
    except KeyboardInterrupt:
        print("Shutdown requested...Goodbye...")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)


if __name__ == "__main__":
    main()
