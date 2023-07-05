from moviepy import editor
import os
import config as cfg
from youtube_upload.client import YoutubeUploader
# from writeoauth import write
from imageprocessing import makevideo

def audioimgmixer(image, audio, output):

    #images = editor.ImageClip(img='.\\res\\images\\{path}'.format(path = image))
    processed = makevideo(os.getcwd() + '\\res\\images\\{path}'.format(path = image))
    audiowave = editor.AudioFileClip('.\\res\\audio\\{path}'.format(path = audio))
    images = editor.ImageClip(processed)
    video_clip = images.set_audio(audiowave)
    video_clip.duration = audiowave.duration
    video_clip.write_videofile('.\\output\\{output}.avi'.format(output=output), codec='mpeg4', fps=1, audio_bitrate="1500k")

    return["Mixing done. File: {output}.avi".format(output=output), output]

def _uploadvideo(file_path):
    options = {
        "title": os.path.basename(file_path).replace('.avi', ''),
        "description": cfg.desc + cfg.advertise,
        "tags": [],
        "categoryId": "22",
        "privacyStatus": "public",
        "kids": False,
    }

    file_path_complete = os.getcwd() + '/output/' + file_path + '.avi'
    uploader.upload(file_path_complete, options)
    while True:
        inp = str(input('Delete Output file? (y/n): '))
        if inp.lower() == 'y':
            os.remove(file_path_complete)
            print('Deleted.')
            break
        elif inp.lower() == 'n':
            break

if __name__ == '__main__':

    print('https://github.com/nichind')

    # write()
    uploader = YoutubeUploader(client_id=cfg.clientid, client_secret=cfg.clientsecret)
    uploader.authenticate()
    while True:
        image, audio, output = str(input('Image name.ext in res/images/')), str(input('Audio name.ext in res/audio/')), str(input('Enter name of the output file: '))
        render = (audioimgmixer(image, audio, output))
        print(render[0])
        while True:
            inp = str(input('Upload to YT? (y/n): '))
            if inp.lower() == 'y':
                _uploadvideo(render[1])
                print('Uploaded to YT!')
                break
            elif inp.lower() == 'n':
                break
