import os
import requests
from zipfile import ZipFile
def download_images(urls, download_dir='images'):
    os.makedirs(download_dir, exist_ok=True)
for url in urls:
        filename = os.path.basename(url.split('?')[0])  # حذف پارامترهای ادرس
        filepath = os.path.join(download_dir, filename)
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Downloaded {url} to {filepath}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")
def create_zip(zip_name='images.zip', folder='images'):
    with ZipFile(zip_name, 'w') as zipf:
        for root, _, files in os.walk(folder):
            for file in files:
                zipf.write(os.path.join(root, file), arcname=file)
    print(f"Created ZIP file: {zip_name}")
if __name__ == "__main__":
    # لینک‌های نمونه، می‌تونی این رو از ورودی بگیری یا فایل بخونی
    urls = [
        'https://via.placeholder.com/150',
        'https://via.placeholder.com/200'
    ]
    download_images(urls)
    create_zip()
