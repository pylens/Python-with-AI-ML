## Python Installation Guide (Windows and macOS)

## For Windows:
1. Go to https://www.python.org/downloads/
2. Click "Download Python 3.x.x" to get the installer.
3. Run the downloaded file.
4. On the installer screen:
    * Check the box that says "Add Python to PATH"
    * Then click "Install Now"
5. Once installed, open Command Prompt and type:
    * python --version
    * pip --version
6. If it shows the version, Python is installed correctly. 
If 'python' is not recognized:
1. Open File Explorer and go to the folder: C:\Users\YourName\AppData\Local\Programs\Python\Python3x 
2. Copy this path and also the Scripts folder path: C:\Users\YourName\AppData\Local\Programs\Python\Python3x\Scripts 
3. Press Start and search "Environment Variables"
4. Click "Edit the system environment variables"
5. In the dialog, click "Environment Variables"
6. Under "System variables", select "Path" and click "Edit"
7. Click "New" and paste both paths copied earlier
8. Click OK and restart Command Prompt
Try again:
* python --version
* pip --version

### For macOS:
1. Go to https://www.python.org/downloads/mac-osx/
2. Download the macOS 64-bit installer (.pkg file)
3. Open the downloaded file and install Python
4. After installation, open Terminal and type:
    * python3 --version
    * pip3 --version
5. You should see the installed version. Python is ready to use. 
