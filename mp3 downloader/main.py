

# pytube doesnt work ,gives age restriction error
# from pytube import YouTube
# import os
# from moviepy.editor import AudioFileClip


# def download_mp3(url,output_path=r"C:\Users\dell\Desktop\mp3 downloader"):
#     try:
#         os.makedirs(output_path,exist_ok=True)
        
#         yt=YouTube(url,use_oauth=True, allow_oauth_cache=True)
#         audio=yt.streams.filter(only_audio=True).first()
#         print("Downloading audio.....")
#         downloaded_file=audio.download(output_path=output_path)
        
#         print("converting to mp3...")
#         mp3_file=downloaded_file.replace('.mp4','.mp3')
#         audio_clip=AudioFileClip(downloaded_file)
#         audio_clip.write_audiofile(mp3_file)
#         audio_clip.close()
        
#         os.remove(downloaded_file)
#         print(f"Mp3 saved successfully at: {mp3_file}")
        
#     except Exception as e:
#         print(f"An error occured:{e}")

# if __name__=="__main__":
#     url=input("enter the youtube video URL:")
#     download_mp3(url)

            
            
        
        