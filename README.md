# Youtube Downloader

Youtube Downloader with pytube and tkinter GUI

### Requirements :
    pytube
    tkinter tk
    tkinter tkk

### Troubleshooting :
    pytube :
    if you get this error
    pytube.exceptions.RegexMatchError: __init__: could not find match for ^\w+\W
    
    _open pytube library_
    venv/Lib/site-packages/pytube/cipher.py
    
    _file and replace line 30_ 
    
    var_regex = re.compile(r"^\w+\W")
    
    _with this_

    var_regex = re.compile(r"^\$*\w+\W")

    _don't forget to save..._

    Have fun :)

    



