2016 Robot Code
===============

## Buttons
On the drivers controller:
* Left joystick is forward/reverse, right joystick is left/right.
* Button 8 converts to tank drive

On the lift joystick:
* Button 3 tilts the shooter up
* Button 4 tilts the shooter down
* Button 5 runs the pickup wheels in
* Button 6 runs the pickup wheels out at full speed
  * Simultaneously pressing button 8 slows them down to half speed
* Button 7 forces a single revolution on the kick wheel

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

To deploy, run `python robot.py deploy --nc`, when connected to the same network
as the RoboRIO.
