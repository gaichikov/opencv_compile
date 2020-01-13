# opencv_compile
OpenCV compiler


usage: opencv_compile.py [-h] [--cv_ver CV_VER] [--py_ver PY_VER]

Script for compiling opencv from source.

optional arguments:
  -h, --help       show this help message and exit
  --cv_ver CV_VER  Opencv version: 3.4.7, 4.1
  --py_ver PY_VER  Python version: 2.7, 3


To compile for python3 - create virtual environment and activate: 

```virtualenv -p python3 venv_3```
```source venv_3/bin/activate```

Then launch the script:

```sudo python opencv_compile.py --cv_ver 3.4.7```


To compile for python2.7 
```virtualenv -p python2 venv_2```
```source venv_2/bin/activate```
```sudo python opencv_compile.py --cv_ver 3.4.7```
