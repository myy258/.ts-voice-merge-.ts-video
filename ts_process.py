# -*- coding: utf-8 -*-
"""
Created on Tue May 25 15:04:35 2021

@author: Yiyu.Mo
"""

import subprocess
import requests
import os

# 处理url并生成文件
def save_url_list(video_urls,save_path,voice_urls=None):
    
    list_video = []
    list_voice = []
    
    # 判断音频入参是否存在
    if voice_urls is not None:
        
        for video_url in video_urls:
            video_name = video_url.split('/',30)[-1]
            video_path = "file" + " '" + save_path + "/video_" + video_name + "'"
            list_video.append(video_path)
            with open(save_path + "/video_" + video_name , 'wb') as f:
                resp1 = requests.get(video_url)
                f.write(resp1.content)
                f.close()
                
        # 生成ts视频文件路径列表，合并用       
        video_filelist_path = save_path + '/video_filelist.txt'        
        with open(video_filelist_path,'w') as f:
            for line in list_video:
                f.write(line+'\n')
            f.close()
        
        for voice_url in voice_urls:
            voice_name = voice_url.split('/',30)[-1]
            voice_path = "file" + " '" + save_path + "/voice_" + voice_name + "'"
            list_voice.append(voice_path)
            with open(save_path + "/voice_" + voice_name , 'wb') as f:
                resp2 = requests.get(voice_url)
                f.write(resp2.content)
                f.close()
                
        # 生成ts音频文件路径列表 ，合并用        
        voice_filelist_path = save_path + '/voice_filelist.txt'
        with open(voice_filelist_path,'w') as f:
            for line in list_voice:
                f.write(line+'\n')
            f.close()
            
    else:
        
        for video_url in video_urls:
            video_name = video_url.split('/',30)[-1]
            video_path = "file" + " '" + save_path + "/video_" + video_name + "'"
            list_video.append(video_path)
            with open(save_path + "/video_" + video_name , 'wb') as f:
                resp1 = requests.get(video_url)
                f.write(resp1.content)
                f.close()
                
        video_filelist_path = save_path + '/video_filelist.txt'        
        with open(video_filelist_path,'w') as f:
            for line in list_video:
                f.write(line+'\n')
            f.close()
            
        voice_filelist_path = None    
        
    return video_filelist_path, voice_filelist_path

# 视频和音频合并转成MP4格式
def video_add_mp4(file_name,mp4_file,save_path):

    os.chdir(save_path)    
    
    outfile_name = save_path + '/final_ts.mp4'
    
    # 设置视频合并命令
    cmd = f'ffmpeg -i {mp4_file} -i {file_name} -acodec copy -vcodec copy {outfile_name}'
    print(cmd)
    subprocess.call(cmd,shell=True)
     
    # 删除生成的文件
    list = os.listdir(save_path)
    for name in list:
        if name.endswith(".ts"):
            os.remove(save_path + '/' + name)
        elif name.endswith(".txt"):
            os.remove(save_path + '/' + name)
            
    # 返回二进制
    with open(outfile_name, 'rb') as f:
        binary_data = f.readlines()
    
    os.remove(outfile_name)
    
    return binary_data
    
# 合并多段ts视频
def mix_video(filelist,save_path):
    
    os.chdir(save_path)
    
    output_ts_mix = save_path + '/mix_video.ts'
    
    # 设置视频合并命令
    cmd = f'ffmpeg -f concat -safe 0 -i {filelist} -c copy {output_ts_mix}'
    print(cmd)
    subprocess.call(cmd,shell=True)
    
    return output_ts_mix

# 合并多段ts音频
def mix_voice(filelist,save_path):
    
    os.chdir(save_path)
    
    output_ts_mix = save_path + '/mix_voice.ts'
    
    # 设置视频合并命令
    cmd = f'ffmpeg -f concat -safe 0 -i {filelist} -c copy {output_ts_mix}'
    print(cmd)
    subprocess.call(cmd,shell=True)
    
    return output_ts_mix

# 合并带有音频的ts视频
def video_mp4(filelist,save_path):
    
    os.chdir(save_path)
    
    output_ts_mix = save_path + '/mix_video.mp4'
    
    # 设置视频合并命令
    cmd = f'ffmpeg -f concat -safe 0 -i {filelist} -c copy {output_ts_mix}'
    print(cmd)
    subprocess.call(cmd,shell=True)
    
    # 删除生成的文件
    list = os.listdir(save_path)
    for name in list:
        if name.endswith(".ts"):
            os.remove(save_path + '/' + name)
        elif name.endswith(".txt"):
            os.remove(save_path + '/' + name)
            
    # 返回二进制
    with open(output_ts_mix, 'rb') as f:
        binary_data = f.readlines()
    
    os.remove(output_ts_mix)
      
    return binary_data    

        
        
    


    