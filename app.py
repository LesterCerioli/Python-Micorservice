from flask import Flask, jsonify

import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

app = Flask(__name__)

# Set up the OAuth 2.0 flow for YouTube API
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def authenticate():
    
    # Specify the path to the credentials file obtained from Google Developer Console
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube" 
    api_version = "v3"
    client_secret_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Initialize the OAuth 2.0 flow
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    
    # Build the YouTube API service
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)
    
    return youtube

def like_video(video_id):
    youtube = authenticate()
    try:
        request = youtube.video().rate(
            id=video_id,
            rationf="like"
        )
        response = request.execute()
        return jsonify({"success": True, "message": f"Video with ID {video_id} liked successfully."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    
@app.route('/like_video/<video_id>', methods=['POST'])
def like_video_route(video_id):
    return like_video(video_id)

if __name__ == "__main__":
    app.run(debug=True)

