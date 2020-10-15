""" This class will be the service class"""
import os
import subprocess
import json

class service:


    def __init__(self):
        self.music_folder_path='/home/pi/Music'
        self.is_song_playing=False

    def debug_print(self):
        """
        Print debugger massage 
        """
        return "The service class is reachable."

    def get_pi_sys_info(self):
        pass

    def get_local_music_list(self):
        json_dic={}
        json_dic["local_music_list"]=self.get_local_music_from_pi()
        return json.dumps(json_dic)

    def get_local_music_from_pi(self):
        cmd = ['ls', '-1', self.music_folder_path]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        o, e = proc.communicate()
        out_list = o.split('\n')
        if out_list[len(out_list)-1] == '':
            del out_list[len(out_list)-1]
        return out_list

    def play_music(self,music_name):
        json_dic={}
        if self.is_song_playing:
            #add song into queer
            pass
        local_music_list = self.get_local_music_from_pi()
        return json.dumps(json_dic)

    def play_all(self,music_list):
        pass

    def is_playing(self):
        json_dic={}
        json_dic["is_song_playing"] = self.is_song_playing
        return json.dumps(json_dic)

    def stop_play(self):
        pass

    def curr_song_name(self):
        pass