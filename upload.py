import os
from google.cloud import storage

def upload_folder_to_gcs(bucket_name, local_folder_path, destination_folder_name):
    """Uploads all files in a folder to the Google Cloud Storage bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    for root, dirs, files in os.walk(local_folder_path):
        for file_name in files:
            local_file_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(local_file_path, local_folder_path)
            destination_blob_name = os.path.join(destination_folder_name, relative_path)

            blob = bucket.blob(destination_blob_name)
            blob.upload_from_filename(local_file_path)

            print(f"File {local_file_path} uploaded to {destination_blob_name} in {bucket_name}.")

if __name__ == "__main__":
    # Replace these values with your own
    bucket_name = "data-banks-bucket"
    local_folder_path = "data/Cloud Upload/Yelp"
    destination_folder_name = "Yelp"

    upload_folder_to_gcs(bucket_name, local_folder_path, destination_folder_name)
