# Youtube Downloader

Youtube Downloader with pytube and tkinter GUI

### Requirements :
    pytube
    tkinter tk
    tkinter tkk

### How to use :
    First of all, you must have python 3.7 installed on your computer.
    Then you have to install pytube.
    
    pip install pytube
    
    Now you can run your script with the python main.py command.

    python main.py

### Use with virtual environment
    You can run your script with the virtual environment by following the commands below.
    
    python -m venv venv
    
    .\venv\Scripts\activate

    python ./main.py


### Troubleshooting :
    pytube :
    if you get this error
    pytube.exceptions.RegexMatchError: __init__: could not find match for ^\w+\W
    
    open pytube library
    
    venv/Lib/site-packages/pytube/cipher.py
   
    file and replace line 30 
    
    var_regex = re.compile(r"^\w+\W")
    
    with this

    var_regex = re.compile(r"^\$*\w+\W")

    don't forget to save.._

### Have fun :)

    



