import os
from yt_dlp import YoutubeDL

def download_tiktok_video(video_url, output_dir):
    # ফোল্ডারটি না থাকলে তৈরি করে নেবে
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # ডাউনলোডের কনফিগারেশন (এখানে ফাইলের নাম 'tiktok_' দিয়ে শুরু হবে)
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, 'tiktok_%(id)s.%(ext)s'),
        'format': 'best',
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            # ভিডিও ডাউনলোড
            print("Downloading...")
            ydl.download([video_url])
            
            # মেটাডেটা বা তথ্য নেওয়া
            info_dict = ydl.extract_info(video_url, download=False)
            print("\n--- Video Metadata ---")
            print("Title:", info_dict.get('title'))
            print("Uploader:", info_dict.get('uploader'))
            print("View Count:", info_dict.get('view_count'))
            
    except Exception as e:
        print("Error হয়েছ:", str(e))

# ব্যবহার করার নিয়ম
if __name__ == "__main__":
	
    # আপনার আসল টিকটক ভিডিওর লিংক এখানে দিন
    tiktok_url = "https://vm.tiktok.com/ZS92gyt7u87s2-HspX6/ This post is shared via TikTok Lite. Download TikTok Lite to enjoy more posts: https://www.tiktok.com/tiktoklite"
    
    # আপনার কম্পিউটারের একটি আসল ফোল্ডারের নাম দিন (যেমন: 'downloads')
    download_directory = "tiktok_downloads" 
    
    download_tiktok_video(tiktok_url, download_directory)
