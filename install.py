import os
import sys
import platform
import subprocess
# Detect the platform
plat = platform.system()
print("Importing libs")

# Check if zbar is installed
try:
    from pyzbar.pyzbar import decode
    print("zbar import success")
except ImportError:
    print('zbar not found. Installing...')
    # Install zbar using the appropriate package manager
    if plat == 'Windows':
        subprocess.call(['pip3', 'install', 'pyzbar'])
        from pyzbar.pyzbar import decode

    elif plat == 'Linux':
        subprocess.call(['sudo', 'apt-get', 'install', 'zbar'])
        from pyzbar.pyzbar import decode
    elif plat == 'Darwin':  # macOS
        try:
            subprocess.run(['brew', '--version'], check=True)
            print("Homebrew is already installed.")
            try:
                subprocess.call(['brew', 'install', 'zbar'])
                subprocess.call(['pip3', 'install', 'pyzbar'])
                os.system('pip3 install -r requirements.txt')
                print('zbar and pyzbar installed successfully.')
                from pyzbar.pyzbar import decode
            except subprocess.CalledProcessError as e:
                print(f"{e}")

            try:
                subprocess.call(['brew', 'install', 'poppler'])
            except:
                print("Couldn't install poppler")


        except subprocess.CalledProcessError:
            print("Homebrew is not installed. Installing...")

            # Install Homebrew
            command = ['/bin/bash', '-c',
                       '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)']
            subprocess.run(command, check=True)

            print("Homebrew has been installed.")
        try:
            subprocess.call(['brew', 'install', 'zbar'])
            subprocess.call(['pip3', 'install', 'pyzbar'])
            os.system('pip3 install -r requirements.txt')
            print('zbar and pyzbar installed successfully.')
            from pyzbar.pyzbar import decode
        except subprocess.CalledProcessError as e:
            print(f"{e}")
    else:
        print('Unsupported platform')
        exit(1)

try:
    from pdf2image import convert_from_path, convert_from_bytes
    from pdf2image.exceptions import (
        PDFInfoNotInstalledError,
        PDFPageCountError,
        PDFSyntaxError
    )
except:
    os.system('pip3 install pdf2image')
    print("Installing PDF utilities")
    from pdf2image import convert_from_path, convert_from_bytes
    from pdf2image.exceptions import (
        PDFInfoNotInstalledError,
        PDFPageCountError,
        PDFSyntaxError
    )

