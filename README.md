# SOD-Viewer

<a href="https://github.com/AsulconS/SOD-Viewer/releases/tag/v0.1.0"><img src="https://img.shields.io/github/v/release/AsulconS/SOD-Viewer"></a>
<a href="#"><img src="https://img.shields.io/github/last-commit/AsulconS/SOD-Viewer"></a>
<a href="#"><img src="https://img.shields.io/github/commit-activity/y/AsulconS/SOD-Viewer"></a>
<a href="https://github.com/AsulconS/SOD-Viewer/issues"><img src="https://img.shields.io/github/issues/AsulconS/SOD-Viewer"></a>
<a href="https://github.com/AsulconS/SOD-Viewer/pulls"><img src="https://img.shields.io/github/issues-pr/AsulconS/SOD-Viewer"></a>
<a href="#"><img src="https://img.shields.io/github/stars/AsulconS/SOD-Viewer"></a>

 SOD-Viewer is a graphical tool based on CTk and written in Python aimed at the visualization of a Second Order Dynamics numerical approach by parameter tuning.

 ## How to run it?

 ### Option 1: Executing the binaries:
  - Just go the lastest release <a href="https://github.com/AsulconS/SOD-Viewer/releases/tag/v0.1.0"><img src="https://img.shields.io/github/v/release/AsulconS/SOD-Viewer"></a>, download and run the `sod.exe` executable.

 ### Option 2: Using a Python Virtual Environment:
  1. Create a python virtual environment usign the following command:
     ```
     python -m venv venv
     ```
  2. Then, with an open terminal, activate your venv:

     - For **Windows PowerShell**:
       ```
       venv\Scripts\activate.ps1
       ```
     - For **Windows Cmd**:
       ```
       venv\Scripts\activate.bat
       ```
     - For **Linux**:
       ```
       source venv/bin/activate
       ```
  3. Finally, install the requirements:
     ```
     pip install -r requirements.txt
     ```
  4. With that done, you can run the app by running:
     ```
     python app.py
     ```
