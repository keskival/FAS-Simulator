#!/bin/sh
ffmpeg -i sequence.wav -pix_fmt yuv420p -loop 1 -framerate 10 -i "output/%5d.png" -vf fps=10 -vcodec mpeg4 -strict -2 -b:a 384k -b:v 800k -acodec aac -c:a aac -shortest fas2.mp4

