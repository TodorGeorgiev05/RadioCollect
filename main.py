import os
import time
from onlineradio import scrape_song_names, get_youtube_link, download_song

def main():
    output_path = 'C:/.../Desktop/.../folder'
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    songs = scrape_song_names()
    
    if not songs:
        print("No songs found.")
        return
    
    for song in songs:
        print(f"Processing song: {song}")
        retry_count = 0
        while retry_count < 3:   # Опитваме 3 пъти да намерим песента
            youtube_link = get_youtube_link(song)
            if youtube_link:
                print(f"Found YouTube link: {youtube_link}")
                download_song(youtube_link, output_path)
                print(f"Downloaded: {song}")
                break
            else:
                retry_count += 1
                print(f"Retrying ({retry_count}/3)...")
                time.sleep(2)  # Изчакваме 2 секунки между опитите да не предобрим процесора
        
        if retry_count == 3:
            print(f"Failed to process {song} after 3 attempts.")

if __name__ == "__main__":
    main()


