#!/bin/sh
ffmpeg -i sequence.wav -pix_fmt yuv420p -loop 1 -i ./documentation/color_vis2.png -vf fps=1 -vcodec mpeg4 -strict -2 -b:a 384k -acodec aac -c:a aac -shortest sequence.mp4

