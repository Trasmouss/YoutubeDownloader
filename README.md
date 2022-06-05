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
    
    open pytube library
    
    venv/Lib/site-packages/pytube/cipher.py
    
    file and replace line 30 
    
    var_regex = re.compile(r"^\w+\W")
    
    with this

    var_regex = re.compile(r"^\$*\w+\W")

    don't forget to save...

    Have fun :)

    



