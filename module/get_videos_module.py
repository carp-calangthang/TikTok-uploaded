import os

def get_video_files():
    
    script_path = os.path.abspath(__file__) 
    src_directory = os.path.dirname(script_path)
    videos_path = os.path.join(src_directory, '..', 'videos')
    
    video_files = []
    for filename in os.listdir(videos_path):
        if filename.endswith((".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv")):
            video_files.append(filename)
    return video_files