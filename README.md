# .ts-voice-merge-.ts-video
ts音频视频合并
### 直接用from mix_tsmp4 import ts2mp4
### ts2mp4(video_urls,save_path,voice_urls) 
### 参数1：video_urls是ts视频，必传参数，list方式传入（存放URL）
### 参数2：save_path是文件保存的路径，必传参数，文件临时储存，最终会删掉
### 参数3：voice_urls是ts音频，可选参数，list方式传入（存放URL）
### ts2mp4最终返回一个二进制
### 文件夹中含有一个ffmpeg.exe，用于处理视频，python调用此.exe
### 使用是需要将save_path写为该文件夹（ts_mix_transform）的路径
