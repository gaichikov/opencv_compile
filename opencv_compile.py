import os
import sys
import argparse

cv_versions = ['3.4.7', '4.1']

parser = argparse.ArgumentParser(description='Script for compiling opencv from source.')
parser.add_argument('--cv_ver', dest='cv_ver', help='Opencv version: {} '.format(', '.join(cv_versions)))
parser.add_argument('--py_ver', dest='py_ver', help='Python version: 2.7, 3')

args = parser.parse_args()
if not args.cv_ver:
    print('Please specify opencv version. \n')
    print(parser.print_help())
    sys.exit()

print('Updating repositories')
os.system('apt-get update && apt-get -y upgrade')

print('Installing required packages..')
os.system('apt-get install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-serial-dev libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5 python-dev python3-dev ')

print('Installing required pip packages')
os.system('pip install numpy')

print('Downloading opencv packages')
os.system('wget -O opencv.zip https://github.com/opencv/opencv/archive/{}.zip && unzip -o opencv.zip && wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/{}.zip && unzip -o opencv_contrib.zip'.format(args.cv_ver, args.cv_ver))

os.chdir('opencv-{}'.format(args.cv_ver))
# try:
#     os.rmdir('build')
# except:
#     pass
try:
    os.mkdir('build')
except:
    pass
os.chdir('build')

print(os.getcwd())

print('Changing swap size..')
os.system('sed -i "s/CONF_SWAPSIZE=100/CONF_SWAPSIZE=2048/g" /etc/dphys-swapfile') 
os.system('/etc/init.d/dphys-swapfile restart')

print('Configuring opencv..')

os.system('cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-{}/modules -D ENABLE_NEON=ON -D ENABLE_VFPV3=ON -D BUILD_TESTS=OFF -D INSTALL_PYTHON_EXAMPLES=OFF -D OPENCV_ENABLE_NONFREE=ON -D CMAKE_SHARED_LINKER_FLAGS="-latomic" -D BUILD_EXAMPLES=OFF -D WITH_GSTREAMER=OFF ..'.format(args.cv_ver))
print('Compiling..')
# made 2 workers instead of 4, to avoid RPi crash. 
os.system('make -j2 && make install && ldconfig')

print('Return back swap size..')
os.system('sed -i "s/CONF_SWAPSIZE=2048/CONF_SWAPSIZE=100/g" /etc/dphys-swapfile') 
os.system('/etc/init.d/dphys-swapfile restart')

print('Done!')