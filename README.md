# Discord Image Uploader

A simple and automated Python script to upload images sequentially from a local folder directly to a Discord channel using a Webhook. It includes built-in delay handling to prevent Discord API rate-limiting and provides real-time terminal feedback on the upload progress.

## 📁 Repository Structure

The `discord-image-uploader` repository consists of the following components[cite: 2]:

*   **`uploader.py`**: The core Python script responsible for executing the image uploads[cite: 2].
*   **`image/`**: The designated folder where all images intended for upload should be placed[cite: 2].
*   **`image/image_test.jpg`**: A sample image provided for testing the script's functionality[cite: 2].
*   **`LICENSE`**: The open-source license governing the use of this code[cite: 2].
*   **`README.md`**: This documentation file[cite: 2].
*   **`.gitattributes`**: Configuration file for Git attribute settings[cite: 2].

## ⚙️ Prerequisites

Before running the script, ensure you have the following installed:
1.  **Python 3.x**: You can download it from [python.org](https://www.python.org/).
2.  **Requests Library**: The script uses this library to handle HTTP requests.

## 🚀 Installation & Setup

1.  **Clone the Repository**
    Clone this project to your local machine:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/discord-image-uploader.git](https://github.com/YOUR_USERNAME/discord-image-uploader.git)
    cd discord-image-uploader
    ```

2.  **Install Dependencies**
    Install the required Python `requests` module by running:
    ```bash
    pip install requests
    ```

3.  **Configure the Webhook**
    *   Open Discord and go to **Server Settings** > **Integrations** > **Webhooks**.
    *   Create a new webhook and copy the **Webhook URL**.
    *   Open `uploader.py`[cite: 2] in your code editor and paste the URL into the `WEBHOOK_URL` variable:
        ```python
        WEBHOOK_URL = 'paste-your-discord-webhook-url-here'
        ```

## 🛠️ Usage

1.  Place all the images you want to upload (e.g., `.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`) into the `image/` directory[cite: 2]. You can delete the default `image_test.jpg` file if you no longer need it[cite: 2].
2.  Open your terminal or command prompt in the repository's root directory.
3.  Run the script:
    ```bash
    python uploader.py
    ```

### Terminal Output
The script provides a clear, numbered progress indicator in the terminal, letting you know exactly which file is currently being uploaded, if it succeeded or failed, and how many images are left in the queue.

## ⚠️ Important Notes

*   **Rate Limits:** The script includes a configurable `DELAY` variable (default is 1 second). Do not set this to `0`, as uploading too fast will trigger Discord's rate limits and temporarily block your uploads.
*   **File Formats:** By default, the script automatically ignores non-image files (like `.txt` or `.pdf`) placed in the `image/` folder[cite: 2].

## 📄 License

This project is open-source and available under the terms specified in the `LICENSE` file[cite: 2].