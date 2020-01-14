# opencv_compile
OpenCV compiler


Install git and virtualenv

``` sudo apt-get install git virtualenv ```

Clone repository at home folder

``` 
cd ~
git clone https://github.com/gaichikov/opencv_compile.git 
cd opencv_compile
```

Add user pi for passwordless access at /etc/sudoers

``` echo "pi      ALL=(ALL) NOPASSWD: ALL" | sudo tee -a /etc/sudoers ```

To compile for python3 - create virtual environment and activate: 

```
virtualenv -p python3 venv_3
source venv_3/bin/activate
```

Launch the script:

```
python opencv_compile.py --cv_ver 3.4.7
```

To compile for python2.7 
```
virtualenv -p python2 venv_2
source venv_2/bin/activate
python opencv_compile.py --cv_ver 3.4.7
```

Make a link in virtualenv to a cv2.so module, depending on python version.

```
cd ~/opencv_compile/venv_3/lib/python3.5/site-packages
ln -s /usr/local/lib/python3.5/site-packages/cv2/python-3.5/cv2.cpython-35m-arm-linux-gnueabihf.so cv2.so
```

cv2 module should be available for import in this virtualenv after this.


```
script usage: opencv_compile.py [-h] [--cv_ver CV_VER] [--py_ver PY_VER]

Script for compiling opencv from source.

optional arguments:
  -h, --help       show this help message and exit
  --cv_ver CV_VER  Opencv version: 3.4.7, 4.1
  --py_ver PY_VER  Python version: 2.7, 3

```