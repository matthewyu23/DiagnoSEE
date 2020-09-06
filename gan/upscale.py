'''

Somehow we need to know metadata about the file like FPS, length, resolution...
Converts the video into a series of frames and puts those frames into a folder in frames/video-name/LR/[idx].png
Calls the TecoGAN model on each of those frames and awaits its completion. TecoGAN will output its frames to frames/video-name/HR/[idx].png
We recombine the HR frames into a HR video

Folder Structure:

    videos/
        [name]/
            LR/
            HR/
            original.mp4
            scaled.mp4

'''


import os
import sys
import shutil
import subprocess

folder = "videos/"

def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def gan(video_path):
    if not os.path.exists(video_path):
        print("Invalid path")
        return

    base = os.path.splitext(os.path.basename(video_path))[0]

    if os.path.exists(folder + base):
        shutil.rmtree(folder + base)

    os.mkdir(folder + base)
    os.mkdir(folder + base + "/LR")
    os.mkdir(folder + base + "/HR")

    os.rename(video_path, folder + base + "/original.mp4")

    # convert the low-res video into frames
    os.system(
        f'ffmpeg -i {folder + base + "/original.mp4"} -q:v 1 -qmin 1 -qmax 1 {folder + base + "/LR/%06d.png"}'
    )

    # run the TecoGAN on the frames
    os.system(
        f'python3 main.py --output_dir {folder + base} --summary_dir {folder + base + "/"} --mode inference --input_dir_LR {folder + base + "/LR"} --output_pre HR --num_resblock 16 --checkpoint ./model/TecoGAN --output_ext png'
    )

    os.system(
        f'ffmpeg -i {folder + base + "/HR/output_%06d.png"} {folder + base + "/scaled.mp4"}'
    )

    shutil.rmtree(folder + base + "/LR")
    shutil.rmtree(folder + base + "/HR")


vid_path = sys.argv[1]

gan(vid_path)
