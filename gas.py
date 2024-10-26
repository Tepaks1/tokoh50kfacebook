import os
import platform
import time
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

class ColorfulPHPTools:
    def __init__(self):
        self.author = "TOKOH 50K"
        self.contact = "https://whatsapp.com/channel/0029Vab80HT60eBWA6FUvm1M"

    def clear_screen(self):
        os.system("cls" if platform.system() == "Windows" else "clear")

    def display_logo(self):
        print(f"""
{Fore.CYAN}╭────────────────────────────────────╮{Style.RESET_ALL}
{Fore.CYAN}│{Style.BRIGHT}{Fore.RED}         TOOLS TOKOH 50K          {Fore.CYAN}│{Style.RESET_ALL}
{Fore.CYAN}├────────────────────────────────────┤{Style.RESET_ALL}
{Fore.CYAN}│{Fore.YELLOW}      Mempermudah Pekerjaan Anda    {Fore.CYAN}│{Style.RESET_ALL}
{Fore.CYAN}╰────────────────────────────────────╯{Style.RESET_ALL}
        """)

    def display_contact(self):
        print(f"{Fore.GREEN}📱 Contact: {Fore.WHITE}{self.contact}")
        print(f"{Fore.CYAN}{'─' * 40}{Style.RESET_ALL}")

    def get_php_files(self):
        return [f for f in os.listdir() if f.endswith('.php')]

    def display_php_files(self, files):
        if not files:
            print(f"\n{Fore.RED}⚠️ Tidak ada file PHP di direktori ini.{Style.RESET_ALL}")
            time.sleep(1)
            return None

        print(f"\n{Fore.YELLOW}📂 File PHP tersedia:{Style.RESET_ALL}")
        for idx, file in enumerate(files, 1):
            print(f"{Fore.GREEN}  {idx}. {Fore.WHITE}{file}")
        print()

        try:
            choice = input(f"{Fore.YELLOW}Pilih nomor file: {Fore.WHITE}").strip()
            if choice.isdigit() and 0 < int(choice) <= len(files):
                return files[int(choice) - 1]
        except:
            pass
        return None

    def run_php_file(self, file):
        try:
            self.clear_screen()
            self.display_logo()
            print(f"\n{Fore.GREEN}🚀 Menjalankan: {Fore.WHITE}{file}\n")
            print(f"{Fore.CYAN}{'─' * 40}{Style.RESET_ALL}\n")
            os.system(f"php {file}")
            print(f"\n{Fore.CYAN}{'─' * 40}{Style.RESET_ALL}")
            time.sleep(0.5)
        except:
            pass

    def run(self):
        while True:
            try:
                self.clear_screen()
                self.display_logo()
                self.display_contact()
                
                php_files = self.get_php_files()
                selected_file = self.display_php_files(php_files)
                
                if selected_file:
                    self.run_php_file(selected_file)

            except KeyboardInterrupt:
                self.clear_screen()
                exit()
            except:
                pass

if __name__ == "__main__":
    tools = ColorfulPHPTools()
    tools.run()