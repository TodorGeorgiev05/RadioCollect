import requests
from bs4 import BeautifulSoup
from pytube import Search, YouTube
import os
import time

def scrape_song_names():
    try:
        url = 'https://onlineradiobox.com/bg/power911/?cs=bg.power911'
        response = requests.get(url)
        response.raise_for_status() 

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', class_='tablelist-schedule')
        
        songs = []
        if table:
            rows = table.find_all('tr')
            for row in rows:
                columns = row.find_all('td')
                if len(columns) > 1:
                    song_info = columns[1].text.strip()
                    songs.append(song_info)
                    print(song_info) # всяка една песен която е в сайта
        return songs
    
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []
    
def get_youtube_link(song_name):
    try:
        search = Search(song_name)
        video = search.results[0]
        return video.watch_url
    except Exception as e:
        print(f"Error finding YouTube link for {song_name}: {e}")
        return None

def download_song(youtube_url, output_path):
    try:
        yt = YouTube(youtube_url)
        
        stream = yt.streams.filter(only_audio=True).first()
        filename = yt.title + ".mp3"
        stream.download(output_path=output_path, filename=filename)
    except Exception as e:
        print(f"Error downloading {youtube_url}: {e}")

if __name__ == "__main__":
    scrape_song_names() #викаме метода за да може да прочетем кои песни са в списъка
