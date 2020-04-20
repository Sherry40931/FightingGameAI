# Fighting Game AI
## How to run the framework
Run java framework to start the server (On Mac):
```bash
java -XstartOnFirstThread -cp FightingICE.jar:./lib/lwjgl/*:./lib/natives/macos/*:./lib/*  Main --py4j --mute --port 4242
```
Run Python Script for the agent:
```bash
python python/Main_PyAIvsPyAI.py
```
You can modify the python AI agent in `python/Main_PyAIvsPyAI.py`

## How to get screen data and save as image:
Check `python/DisplayInfo.py` line 63-67 for getting and saving the screen data.  
Check `python/byte/byte_to_image.py` for converting the binary file into image.

## Some useful link of from FightingICE
* Screen Data: http://www.ice.ci.ritsumei.ac.jp/~ftgaic/ATKdoc/struct/ScreenData.html
* Frame Data: http://www.ice.ci.ritsumei.ac.jp/~ftgaic/ATKdoc/struct/FrameData.html
