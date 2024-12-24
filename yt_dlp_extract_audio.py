from yt_dlp import YoutubeDL
from google.colab import files
import os

def extract_audio(video_url, enable_local_download=False):
    """
    Extract audio from a YouTube video and optionally download it locally.
    
    Args:
        video_url (str): URL of the YouTube video
        enable_local_download (bool): If True, downloads the audio file to local machine
    """
    # Define file paths
    output_audio = "output_audio.mp3"
    
    # Configure yt-dlp options for audio extraction
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_audio,
    }
    
    # Download and extract audio
    with YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
            print(f"Audio extracted successfully as: {output_audio}")
            
            # Optional local download
            if enable_local_download:
                try:
                    from google.colab import files
                    files.download(output_audio)
                    print("Download initiated. Check your browser's download folder.")
                except Exception as e:
                    print(f"Error during local download: {str(e)}")
        except Exception as e:
            print(f"Error during audio extraction: {str(e)}")

if __name__ == "__main__":
    # Get video URL from user
    video_url = input("Enter YouTube video URL: ")
    
    # Ask if user wants to download locally
    download_choice = input("Do you want to download the audio file locally? (y/n): ").lower()
    enable_download = download_choice == 'y'
    
    # Process the video
    extract_audio(video_url, enable_download)
