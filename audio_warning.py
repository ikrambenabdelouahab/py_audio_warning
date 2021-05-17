# -*- coding: utf-8 -*-
"""audio_warning.ipynb

Warning sound urls:
*  https://actions.google.com/sounds/v1/alarms/digital_watch_alarm_long.ogg
*  https://upload.wikimedia.org/wikipedia/commons/0/05/Beep-09.ogg
*  https://actions.google.com/sounds/v1/alarms/spaceship_alarm.ogg


Source :
*  https://developers.google.com/assistant/tools/sound-library

Méthode 1
"""

# Play an audio warning
from google.colab import output
output.eval_js('new Audio("https://actions.google.com/sounds/v1/alarms/bugle_tune.ogg").play()')

"""Méthode 2"""

import IPython.display as display
display.Audio(url="https://actions.google.com/sounds/v1/alarms/digital_watch_alarm_long.ogg", autoplay=True)
