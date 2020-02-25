# Python-multitasking-assistant
Python multitasking assistant with voice and much more function

Install requrements.

Use manage.py to run the application

If you have problems with PyAudio:
  
    1.Downloaded the .tgz of portaudio file from here http://www.portaudio.com/download.html
    2.Then Extract the downloaded file.
    3.cd to the extracted folder.
    4.Then ./configure && make
    5.Now do sudo make install
    6.Then upgrade pyaudio by sudo pip install pyaudio --upgrade
    7. sudo apt-get install portaudio19-dev 

Apps of Assistant:

  GUI {
    1. __init__.py
    2. manage.py
    3. views.py
    4. settings.py
    5. models.py
    6. tests.py
    """ Work with kivy pakage """
  }
  
  VOICE{
    1. __init__.py
    2. voice.py
    3. device.py
    4. device2.py
    """ Work with PyAudio, Speech Recognition pakage """
  }
  
  WEB{
    1. __init__.py
    """ """
  }
