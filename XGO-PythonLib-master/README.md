# XGO-PythonLib

XGO2 has built-in motion libraries for controlling the movement and various features of the machine dog, including battery level, firmware version, and servo angle. The motion library enables users to control translation and pose movement, as well as single servo and single-leg movement. The education library facilitates camera, screen, key, microphone, and speaker operations, as well as commonly used AI functions such as gesture recognition, face detection, emotional recognition, and age and gender recognition.  The detailed instructions for use of the library are as follows.

PythonLib included xgolib.py and xgoedu.py

[Luwu Dynamics · WIKI](https://www.yuque.com/luwudynamics)


## Install instructions 

1 Burn the latest official image 

2 Run this command:

```
pip install --upgrade xgo-pythonlib
sudo pip install --upgrade xgo-pythonlib
```

## Examples

Perform gesture recognition on the current camera and press the "c" key to exit.

```python
from xgoedu import XGOEDU 
XGO_edu = XGOEDU()

while True:
    result=XGO_edu.gestureRecognition()  
    print(result)
    if XGO_edu.xgoButton("c"):  
        break
```
xgolib library example
```python
from xgolib import XGO
dog = XGO('xgomini')
dog.action(1)
```
## Change Log

### [0.3.5] - 2024-02-23

#### Fixed
- Update xgolib.py to 1.4.1
- Added xgo-rider instruction set and related motion functions

## Change Log

### [0.3.2] - 2024-01-29

#### Fixed

- Update xgolib.py to 1.3.9

### [0.3.1] - 2023-09-16

#### Fixed

- Add .gitignore
- Gesture image flip

### [0.2.8] - 2023-08-22

#### Fixed

- Methods: display_text_on_screen()

### [0.2.7] - 2023-08-20

#### Added

- Methods: posenetRecognition added.

#### Fixed

- Methods: lcd_arc() and lcd_circle() 

### [0.2.5] - 2023-07-19

#### Fixed

- Methods: Change the __init__ in xgolib.py to add delay to resolve some movement irregularities.

### [0.2.4] - 2023-07-13

#### Fixed

- Methods: lcd_clear() was fixed.

### [0.2.3] - 2023-07-04

#### Added

- Methods: cap_color_mask added.

#### Fixed

- CircleRecognition renamed BallRecognition and improved.

### [0.2.2] - 2023-07-03

#### Added

- Five Methods: SpeechRecognition SpeechSynthesis QRRecognition CircleRecognition ColorRecognitio added.

### [0.2.0] - 2023-06-21

#### Fixed

- xgoVideo and xgoVideoRecord method can be used.

### [0.1.9] - 2023-06-20

#### Fixed

- Fixed the issue with the xgoTakePhoto method that was causing abnormal RGB colors in the saved photos.



