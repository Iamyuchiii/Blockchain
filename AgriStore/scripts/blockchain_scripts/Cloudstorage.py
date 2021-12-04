import dropbox
import logging
import os


class Dropbox_cloudstorage:
    def __init__(self, access_token):
        self.access_token = access_token

    def download_file(self):
        pass

    def file_move(self, file_from, file_to):
        """move a file to dropbox"""
        dropbox_client = dropbox.Dropbox(self.access_token)

        with open(file_from, "rb") as f:
            dropbox_client.files_upload(f.read(), file_to)

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox"""
        dropbox_client = dropbox.Dropbox(self.access_token)

        with open(file_from, "rb") as f:
            dropbox_client.files_upload(f.read(), file_to)


class Google_drive:
    pass
