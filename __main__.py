import os
import platform
import PySimpleGUI as sg
import json
from concurrent.futures import ThreadPoolExecutor
from . import anim


def main():
    if platform.system() == 'Windows':
        os.environ['PATH'] += os.pathsep + os.path.join(os.path.dirname(__file__), 'bin')

    win_width, win_height = 600, 150

    layout = [
        [sg.Text('Input Image or Video'), sg.Input(key='input'), sg.FileBrowse(file_types=(('Image or Video', '*.jpg *.jpeg *.png *.gif *.mp4 *.mov *.flv *.avi *.webm *.mkv'), ('All Files', '*.*')))],
        [sg.Text('Audio'), sg.Input(key='audio'), sg.FileBrowse(file_types=(('Audio', '*.mp3 *.mpeg *.aiff *.wav *.flac *.ogg *.aac',), ('All Files', '*.*')))],
        [sg.Text('Output Video'), sg.Input(key='output'), sg.FileSaveAs(file_types=(('MP4 Video', '*.mp4'), ('All Files', '*.*')))],
        [sg.Button('Animate')],
    ]
    save_keys = ['input', 'audio', 'output']

    window = sg.Window('music visualizer', layout, size=(win_width, win_height))
    window.finalize()
    
    with ThreadPoolExecutor(1) as executor:
        animation_thread = None

        save_filepath = os.path.join(os.path.dirname(__file__), 'save.json')
        try:
            with open(save_filepath, 'r') as save_file:
                saved_values = json.load(save_file)
            for key in save_keys:
                if key in saved_values:
                    window[key].update(saved_values[key])
            print('Loaded values from previous session')
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
        last_values = {key: None for key in save_keys}

        while True:
            event, values = window.read(timeout=100)

            if event == sg.WIN_CLOSED:
                saved_values = {key: last_values[key] for key in save_keys}
                with open(save_filepath, 'w') as save_file:
                    json.dump(saved_values, save_file)
                break

            if event == 'Animate':
                if not values['output'].endswith('.mp4'):
                    window['output'].update(values['output']+'.mp4')
                    values['output'] += '.mp4'

                animation_thread = executor.submit(anim.create_animation,
                    img=values['input'],
                    audio=values['audio'],
                    output=values['output'],
                )
                window['Animate'].update(disabled=True, text='Running...')

            if animation_thread is not None and animation_thread.done():
                try:
                    animation_thread.result()  # we call this to propagate errors to the main thread
                except Exception as e:
                    print(e)

                animation_thread = None

                window['Animate'].update(disabled=False, text='Animate')

                if platform.system() == 'Windows':
                    os.system(values['output'])
                elif platform.system() == 'Darwin':
                    os.system('open ' + values['output'])
                elif platform.system() == 'Linux':
                    os.system('xdg-open ' + values['output'])

            last_values = values.copy()
                
    window.close()


if __name__ == '__main__':
    main()
