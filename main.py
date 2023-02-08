# This is a mini program to download Youtube Video

from pytube import YouTube
from pytube.cli import on_progress
import time
import random


def typewrite(num1, num2, text):
    for c in text:
        r = random.uniform(num1, num2)
        time.sleep(r)
        print(c, end='', flush=True)


def completed(stream, file_path):
    comp = '\nDownload Completed\n'
    size = 'File Size: ' + str(stream.filesize / 2 ** 30) + "Mb\n"
    title = 'Title: ' + stream.title + '\n'
    Local = "Local Path: " + file_path + '\n'

    txt_list = [comp, size, title, Local]

    for txt in txt_list:
        typewrite(0.05, 0.1, txt)
        print('-' * 60)


def download(url: str, path: str):
    try:
        yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=completed)

        stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        typewrite(0.05, 0.1, "Download is starting\n")
        stream.download(output_path=path)
    except:
        print('Something went wrong in function download')


if __name__ == '__main__':
    url = input("The URL to the Youtube Video: ")
    path = '.'
    download(url, path)