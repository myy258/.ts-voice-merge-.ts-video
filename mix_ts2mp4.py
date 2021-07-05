# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:20:46 2021

@author: Yiyu.Mo
"""

from ts_process import save_url_list, mix_video, mix_voice, video_add_mp4, video_mp4

def ts2mp4(video_urls,save_path,voice_urls=None):
    
    video_filelist_path, voice_filelist_path = save_url_list(video_urls,save_path,voice_urls)
    
    if voice_urls is not None:
    
        video = mix_video(video_filelist_path,save_path)
        
        voice = mix_voice(voice_filelist_path,save_path)
        
        vi_mix_vo = video_add_mp4(voice,video,save_path)
        
        return vi_mix_vo
        
    else:
        
        video = video_mp4(video_filelist_path,save_path)
        
        return video
        


