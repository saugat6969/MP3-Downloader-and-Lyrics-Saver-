# using beautifulsoup 

import os
import subprocess
import requests
from bs4 import BeautifulSoup
import lyricsgenius

 
GENIUS_ACCESS_TOKEN = 'SAo0c4wQIBde_JYPxl1JO1uH-j3o36Re6X--kYAMYIz5FI9qzqbA4qc2DdERDz99'  
genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)

def fetch_lyrics(song_title):
    try:
        print(f"Fetching lyrics for: {song_title}")
        
   
        song = genius.search_song(song_title)  
        
        if song:
            return song.lyrics
        else:
            return "Lyrics not found."    
    except Exception as e:
        return f"An error occurred while fetching lyrics: {e}"

def download_mp3(url, output_path=r"C:\Users\dell\Desktop\mp3 downloader"):
    try:
        os.makedirs(output_path, exist_ok=True)
        print(f"Downloading from URL: {url}")
        
       
        
        song_title = input("enter the song title for lyrics:")
        audio_file = os.path.join(output_path, "temp_audio.m4a")
        command = [
            "yt-dlp",
            "-f", "bestaudio",
            "--extract-audio",
            '--ffmpeg-location',
            "C:\\Users\\dell\\Documents\\ffmpeg-master-latest-win64-gpl-shared\\bin",
    
            
            "--audio-format", "mp3",
            "-o", f"{output_path}/%(title)s.%(ext)s",
            url
        ]
        subprocess.run(command, check=True)
        
        print("Download and conversion completed!")
        lyrics = fetch_lyrics(song_title)
        # print("Lyrics:\n", lyrics)
        
        
        
        lyrics_file=os.path.join(output_path,f"{song_title}_lyrics.txt") # type: ignore
        with open(lyrics_file,"w") as file:
            file.write(lyrics)
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    download_mp3(url)

# def fetch_lyrics(song_title):
#     try:
#         print(f"fetching lyrics for:{song_title}")
#         query=f"{song_title} lyrics"
#         search_url=f"hhtps://www.google.com/search?q={query}"
        
#         headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        
#         response=requests.get(search_url,headers=headers)
        
#         if response.status_code==200:
#             print("request successful.")
#             print(response.text)
            
#         else:
#             print(f"failed with status code:{response.status_code}")  
            
#         soup=BeautifulSoup(response.text,'html.parser')
#         snippet=soup.find("div", {"class": "BNeawe tAd8D AP7Wnd"})
#         if snippet:
#             return snippet.text.strip() 
#         else:
#             return "lyrics not found."    
#     except Exception as e:
#         return f"an error occured while fetching:{e}"   