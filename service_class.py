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
        list_files = subprocess.run(["ls", "-1", music_folder_path])
        print("The exit code was: %d" % list_files.returncode)
        return "get_local_music_list"

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