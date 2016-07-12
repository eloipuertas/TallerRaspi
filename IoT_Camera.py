
# coding: utf-8

# https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/

# # Previsualitzant

# In[ ]:

# 10 segons de vídeo.

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview(alpha=200)
sleep(10)
camera.stop_preview()


# # Guardant una imatge

# In[ ]:

# Guardar una imatge

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

# És important posar a dormir com a mínim 2 segons abans  de capturar la imatge.


# In[ ]:

# 5 imatges seguides
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image{}.jpg'.format(i))
camera.stop_preview()


# # GRAVANT UN VIDEO

# In[ ]:

camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()


# # EFECTES
# 
# ## 1. Gravant a màxima ressolució

# In[ ]:

camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/max.jpg')
camera.stop_preview()


# La ressolució mínima és de 64x64, proveu de fer una foto amb aquesta ressolució

# ## 2. Afegint texte
# 
# 

# In[1]:

camera.start_preview()
camera.annotate_text = "Hello world!"
sleep(5)
camera.capture('/home/pi/Desktop/text.jpg')
camera.stop_preview()


# Es pot ajustar la mida del texte així:

# In[ ]:

camera.annotate_text_size = 50


# Les mides vàlides van de 6 a 160. Per defecte és 32.
# 
# També es pot ajustar el color del texte: 
# 

# In[ ]:

from picamera import PiCamera, Color

camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = " Hello world "
sleep(5)
camera.stop_preview()


# ## 3. Ajustant la brillantor i el constrast

# In[ ]:

# brillantor
camera.start_preview()
for i in range(100):
    camera.annotate_text = "Brightness: {}s".format(i)
    camera.brightness = i
    sleep(0.1)
camera.stop_preview()


# In[ ]:

# contrast
camera.start_preview()
for i in range(100):
    camera.annotate_text = "Contrast: {}s".format(i)
    camera.contrast = i
    sleep(0.1)
camera.stop_preview()


# ## 4. Aplicant efectes
# 
# Amb `camera.image_effect`  pots aplicar un determinat efecte a l'imatge. Les opcions són : `none`, `negative`, `solarize`, `sketch`, `denoise`, `emboss`, `oilpaint`, `hatch`, `gpen`, `pastel`, `watercolor`, `film`, `blur`, `saturation`, `colorswap`, `washedout`, `posterise`, `colorpoint`, `colorbalance`, `cartoon`, `deinterlace1`, i `deinterlace2`. Proveu-los!!!

# In[2]:

camera.start_preview()
camera.image_effect = 'colorswap'
sleep(5)
camera.capture('/home/pi/Desktop/colorswap.jpg')
camera.stop_preview()


# Per provar-los tots podem fer:

# In[ ]:

camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: {}".format(effect)
    sleep(5)
camera.stop_preview()


# Amb `camera.awb_mode` podeu tocar els nivells de blanc. Les opcions són: off, auto, sunlight, cloudy, shade, tungsten, fluorescent, incandescent, flash, i horizon. Per defecte el valor és auto.

# In[ ]:

camera.start_preview()
camera.awb_mode = 'sunlight'
sleep(5)
camera.capture('/home/pi/Desktop/sunlight.jpg')
camera.stop_preview()


# Amb `camera.exposure_mode`  podeu tocar el mode d'exposicó. Les opcions són off, auto, night, nightpreview, backlight, spotlight, sports, snow, beach, verylong, fixedfps, antishake, i fireworks. L'opció per defecte és auto.

# In[ ]:

camera.start_preview()
camera.exposure_mode = 'beach'
sleep(5)
camera.capture('/home/pi/Desktop/beach.jpg')
camera.stop_preview()


# # Projecte IoT ->  Fer un piulet amb una foto presa amb la pi-camera:
# 
# 
# 
# ### Requeriments
# 
# * Twython: 
# > pip3 install twython
# 
# * Per configurar l'accés a twitter mireu aquest link:
# 
# https://www.raspberrypi.org/learning/getting-started-with-the-twitter-api/

# In[ ]:

from twython import Twython
from picamera import PiCamera
from time import sleep
from datetime import datetime
import random
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

camera = PiCamera()

timestamp = datetime.now().isoformat()
photo_path = '/home/pi/tweeting-babbage/photos/{}.jpg'.format(timestamp)
    sleep(3)
    camera.capture(photo_path)

    with open(photo_path, 'rb') as photo:
        twitter.update_status_with_media(status=message, media=photo)


