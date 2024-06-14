sudo pip3.7 install virtualenvwrapper



After installation, in . bashrc file in current user’s home folder, you need to add several lines:
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.7
export WORKON_HOME=~/venv
. /usr/local/bin/virtualenvwrapper.sh


#Creating new virtual env
$ mkvirtualenv --python=/usr/local/bin/python3.7 pyneng
New python executable in PyNEng/bin/python
Installing distribute........................done.
Installing pip...............done.
(pyneng)$


#Listing virtual env
(pyneng)$ ls -ls venv
total 52
....
4 -rwxr-xr-x 1 nata nata 99 Sep 30 16:41 preactivate
4 -rw-r--r-- 1 nata nata 76 Sep 30 16:41 predeactivat

#Exiting virtual environment
(pyneng)$ deactivate

#Switching to virtual environment
workon pyeng

#Removign virtual environment
rmvirtualenv pyeng