import os
import time
import requests

# ================= CONFIGURATION =================
# Replace with your Discord Webhook URL
WEBHOOK_URL = 'discord-webhook-here'

# Folder name where the images are stored
FOLDER_PATH = './image' 

# Delay time (in seconds) between uploads
DELAY = 1
# =================================================

def upload_images():
    # Check if the folder exists
    if not os.path.exists(FOLDER_PATH):
        print(f"[ERROR] Folder '{FOLDER_PATH}' not found!")
        return

    # Filter only image files to be uploaded
    valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp')
    files = [f for f in os.listdir(FOLDER_PATH) if f.lower().endswith(valid_extensions)]
    
    total_files = len(files) # Count total images

    if total_files == 0:
        print("[INFO] No image files found in the folder.")
        return

    print(f"[INFO] Found {total_files} images. Starting the upload process...\n")

    # Use enumerate to track the order (starting from 1)
    for index, filename in enumerate(files, start=1):
        file_path = os.path.join(FOLDER_PATH, filename)
        
        # Calculate remaining images
        remaining_images = total_files - index

        with open(file_path, 'rb') as f:
            files_payload = {
                'file': (filename, f)
            }

            # Display order info, filename, and remaining images
            print(f"> [{index}/{total_files}] Uploading: {filename} ... (Remaining: {remaining_images} images left)")
            
            try:
                response = requests.post(WEBHOOK_URL, files=files_payload)

                if response.status_code in (200, 204):
                    print(f"  [SUCCESS] {filename} sent.")
                else:
                    print(f"  [FAILED] Status Code: {response.status_code} - {response.text}")
                    
            except Exception as e:
                print(f"  [ERROR] An error occurred while uploading {filename}: {e}")
        
        # Add a delay, EXCEPT for the last file
        if remaining_images > 0:
            time.sleep(DELAY)

    print("\n[INFO] All images have been processed!")

if __name__ == '__main__':
    upload_images()