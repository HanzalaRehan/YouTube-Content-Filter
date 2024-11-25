
# YouTube Video Blocker with mitmproxy

## Description

This script uses **mitmproxy**, an interactive HTTPS proxy, to block specific YouTube videos by their video IDs. Once installed and set up, the script will intercept and block access to a designated video by returning a `403 Forbidden` response.

---

## Prerequisites

- Python 3.7+ (Ensure you have **Python 3.11** for this script, as per your environment).
- pip (Python package installer).

---

## Installation

1. **Install mitmproxy**:
    ```bash
    pip install mitmproxy
    ```

2. **Clone or Download the Script**:
    Save the script provided in `block.py`.

---

## Setup mitmproxy

1. **Run mitmproxy**:
    Open a terminal and execute the following:
    ```bash
    mitmproxy --listen-port 8080
    ```

2. **Set Up mitmproxy Certificate**:
   - mitmproxy uses a self-signed certificate to intercept HTTPS traffic. Install the mitmproxy CA certificate to avoid security warnings:
   
     - For all host devices select the web proxy (HTTP and HTTPS) to the correct ip and port of the mitmproxy.
     - Start mitmproxy and navigate to `http://mitm.it` in your browser.
     - Download and install the appropriate certificate for your system or browser.

---

## Usage

Once the script and mitmproxy are running:

1. Restart the proxy using:
    ```bash
    mitmproxy --listen-port 8080 -s block.py
    ```
2. Open your browser and navigate to YouTube.
3. Attempt to watch a YouTube video with the ID `1yyRvyNQ5rQ` (e.g., `https://www.youtube.com/watch?v=1yyRvyNQ5rQ`).
4. The video will be blocked.

---

## Customization

To block a different video:

1. Open `block.py`.
2. Replace the `video_id` variable value:
    ```python
    video_id = "new_video_id_here"
    ```

3. Restart mitmproxy to apply the changes.

---

## Troubleshooting

- **Request not blocked?**
  - Ensure `mitmproxy` is running with the script loaded.
  - Check your browser settings to ensure it is using mitmproxy as a proxy.

- **Certificate issues?**
  - Ensure the mitmproxy CA certificate is installed and trusted on your system.

---

## License

This project is licensed under the MIT License.

---

Happy intercepting! 🎉
