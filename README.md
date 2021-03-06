# VTD Data Pre-process

This program is an assistance of complex work using [VTD (VIRES Virtual Test Drive)](https://vires.mscsoftware.com/)  


## Description

In particular, it process the raw csv data generated by RDB Sniffer, a runtime tool of VTD, by removing, filling, sorting, mapping values, joining, etc.  

This program runs for each scenario: it processes and aggregates all the data our team require from different raw csv (currently 5).  

Finally, it saves the file locally and also sends it to server (using socket), which is another computer in our lab waiting for this final csv as the direct input for next step Evaluation system.

## Getting Started

### Dependencies

* Language dependent: python / jupyter notebook  
* OS independent: MacOS, Windows, Linux (Ubuntu)  
* Stdlib packages: socket, os, threading, time, etc. 
* Additional: easygui (easier filepath), pyinstaller (.py to executable), pandas and numpy (data process), jupyter (deal with ipynb above all).
* Anaconda-navigator is strongly recommended (I know it's buggy) to edit the code based on your need. If you choose not to use it, some other packages also need your installation.  
```
pip install <PACKAGE_NAME>
```

### Installing

* Basically, just clone the repo to each of 2 computers and everything is set.
* Just make sure don't modify the file structure or ANY folder name.

### Executing program

Remind again, the program is designed for 2 computers, one does process and sends, the other receive.  

* Choose the way you want to run: .ipynb, .py, executable.
* The code was originally written in jupyter notebook (.ipynb format).
* To turn a notebook into python script, use nbconvert:
```
jupyter nbconvert --to script big_app.ipynb
```
* To get a executable (most of time linux executable, because VTD only runs on Ubuntu, and thus the raw data are generated there), you need to execute the following on a computer with same OS. First you get a python script following previous step. Then you run:
```
pyinstaller --onefile big_app.py
```

## Help

* All features in the program have been tested functionally correct.  
* But the exception handling is still in develop. (i.e. The user don't follow the instruction during the execution of program)
* Some exceptions are detected and handled, the program will print custom message and exit.
* For those I haven't thought of or included in the program, some will cause the exit, some may cause infinite loop. Anyway, use ctrl+c to shutdown the program.


## Authors

Thomas Wang  
[My github-page](https://github.com/Thomaswang0822)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments
* [README-Template.md](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)