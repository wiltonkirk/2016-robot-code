2016 Robot Code
===============

## Extending

To make the robot do interesting things. Objects from
[wpilib](http://robotpy.readthedocs.org/en/latest/wpilib.html) can be
instantiated and used.

## Use

[RobotPy](http://robotpy.readthedocs.org/en/latest/getting_started.html) is
used to run Python3 on the RoboRIO.

### Requirements

RobotPy is developed with [pyfrc](http://pyfrc.readthedocs.org/en/latest/),
which only works with Python 3 (not Python 2). Python 3 is provided by the
python3 package.

pip3 can be used to install development tools using
```
pip install -r requirements.txt
```

#### Virtual Environment

A virtual environment should be used, and can be created using
`virtualenv -p python3 venv`. The entire setup (after installing Python 3)
looks like.
```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

### Testing and Deploying

Both testing and deploying require an active virtual environment
(`source venv/bin/activate`). 

To test, run `python robot.py sim`.

To deploy, run `python robot.py deploy`, when connected to the same network
as the RoboRIO.
