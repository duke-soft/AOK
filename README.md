# AOK
A Python program for analyzing YouTube watch history as JSON.
---
First, go to [Google Takeout](https://takeout.google.com/), deselect all, and select YouTube and YouTube Music.
Click 'Multiple formats', find 'history' and select JSON instead of HTML. Proceed to download.
Search through the folders until you find watch-history.json. This is the file that can be analyzed. Copy it to your working directory and run the following command:
```
python3 aok.py watch-history.json
```
Because the introduction of YouTube shorts skews the data massively, you can put `-s` at the end of the command to analyze it with YT Shorts in mind, if you know you watch them often (or have in the past).
The program will print out your video count per year, total views, and estimated time watched (for both Shorts and non-Shorts if you choose `-s`).
