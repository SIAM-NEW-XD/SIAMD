import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # 👈 এই লাইনটি নতুন যোগ হয়েছে
from yt_dlp import YoutubeDL

app = Flask(__name__)
CORS(app)  # 👈 এই লাইনটি আপনার CORS সমস্যা ১০০% ফিক্স করে দেবে

@app.route('/download', methods=['GET'])
def download_tiktok():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({"error": "URL missing"}), 400

    ydl_opts = {
        'format': 'best',
        'noplaylist': True,
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            
            video_download_url = info_dict.get('url') 
            title = info_dict.get('title', 'TikTok Video')
            uploader = info_dict.get('uploader', 'Unknown')
            
            return jsonify({
                "status": "success",
                "download_url": video_download_url,
                "title": title,
                "uploader": uploader
            })
            
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
