import subprocess

def convert_480p(source: str):
    name = 0
    extention = 1
    target = source.split('.')
    target = target[name]+ "_480p" + target[extention]
    cmd = 'ffmpeg -i ' "{}" ' -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "{}'.format(source, target)