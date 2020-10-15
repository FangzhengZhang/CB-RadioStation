""" This class will be the service class"""
import os
import subprocess

class service:

    music_folder_path='/home/pi/Music'

    def __init__(self):
        pass

    def debug_print(self):
        """
        Print debugger massage 
        """
        return "The service class is reachable."

    def get_pi_sys_info(self):
        pass

    def get_local_music_list(self):
        cmd = ['ls', '-1', music_folder_path]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        o, e = proc.communicate()

        print('Output: ' + o.decode('ascii'))
        print('Error: '  + e.decode('ascii'))
        print('code: ' + str(proc.returncode))

        return o.decode('ascii')

    def play_music(self,music_name):
        pass

    def play_all(self,music_list):
        pass

    def is_playing(self):
        pass

    def stop_play(self):
        pass

    def curr_song_name(self):
        pass