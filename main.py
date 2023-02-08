# This is a mini program to download Youtube Video
import pytube.request
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
    size = 'File Size: ' + str(stream.filesize / 2 ** 20) + "Mb\n"
    title = 'Title: ' + stream.title + '\n'
    Local = "Local Path: " + file_path + '\n'

    txt_list = [comp, size, title, Local]

    for txt in txt_list:
        typewrite(0.01, 0.05, txt)
        print('-' * 60)


def download(url: str, path: str):
    try:
        yt = YouTube(url, on_progress_callback=on_progress, on_complete_callback=completed)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        typewrite(0.01, 0.05, "The Video is found\n")
        typewrite(0.01, 0.05, "Start to download the Video...\n")
        stream.download(output_path=path)

    except:
        print('Something went wrong in function download')

def download_cap(url: str, path: str, lan_code: str):
    typewrite(0.01, 0.05, f"Start to download the Caption of {lan_code}...\n")
    yt = YouTube(url)
    try:
        caption_en = yt.captions[lan_code]
        caption_en.xml_captions
        #print(caption_en.generate_srt_captions())
        caption_en.download(title=yt.title + "_" + lan_code, output_path=path)
    except:
        typewrite(0.01, 0.05, "Not available \n")
        typewrite(0.01, 0.05, "Trying to download auto-generating caption \n")
        try:
            caption_en = yt.captions['a.'+lan_code]
            caption_en.xml_captions
            #print(caption_en.generate_srt_captions())
            caption_en.download(title=yt.title + "_" + lan_code, output_path=path)
        except:
            typewrite(0.01, 0.05, "The auto-generating caption is Not available \n")


if __name__ == '__main__':
    url = input("The URL to the Youtube Video: ")
    path = 'videos'

    # down load video
    #download(url, path)

    # download English Caption
    cap = input("Do you need the caption file(en)? y/n")
    if cap == 'y' or cap == 'Y':
        download_cap(url, path, 'en')


