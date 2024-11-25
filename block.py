from mitmproxy import http

def request(flow: http.HTTPFlow):
    # Check if the request is to YouTube
    if "youtube.com" in flow.request.pretty_host:
        video_id = "sUKwTVAc0Vo" # Video ID here

        # Check for YouTube watch URLs with the specific video ID
        if f"v={video_id}" in flow.request.query or f"/watch?v={video_id}" in flow.request.pretty_url:
            
            flow.response = http.HTTPResponse.make(
                403,  # HTTP status code for Forbidden
                b"Blocked by mitmproxy",
                {"Content-Type": "text/plain"}
            )
