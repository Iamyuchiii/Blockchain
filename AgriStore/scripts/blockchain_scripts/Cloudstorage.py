import datetime
import json
from pydoc import cli
from datetime import date
import dropbox
import os
import ipfshttpclient


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


class ipfs:
    def __init__(self):
        self.client = ipfshttpclient.connect(session=True)
        self.rootpath = ""

    def init_maps(self, path, map_name="ifps"):
        map_name = "ipfs"
        map_hash = "hash_info"
        map_storage = "cloud_storage"
        if not os.path.exists(f"{path}\{map_name}"):
            os.makedirs(f"{path}\{map_name}")
        self.rootpath = f"{path}\{map_name}"

        if not os.path.exists(f"{self.rootpath}\{map_storage}"):
            os.makedirs(f"{self.rootpath}\{map_storage}")

    def clientid(self):
        return self.client.id()

    def version(self):
        print(self.client.version())

    def uploadfile(self):
        upload = self.client.add(f"{self.rootpath}\cloud_storage", recursive=True)
        info_save = [dict(info) for info in upload]

        if not os.path.exists(f"{self.rootpath}\hash_info"):
            os.makedirs(f"{self.rootpath}\hash_info")

        info = {
            "date(yy/mm/dd)": str(datetime.date.today()),
            "time": str(datetime.datetime.now().time()),
            "file_info": info_save,
        }
        time = str(datetime.datetime.now()).replace(":", "-").replace(" ", "--")
        # save the info in a file
        with open(f"{self.rootpath}\hash_info\{str(time)}.txt", "w") as file:
            file.write(json.dumps(info))

    def viewfile(self, hash):
        view = self.client.cat(hash).decode("UTF-8")
        print(view)

    def close(self):
        self.client.close()


# client = ipfs()
# client.init_maps("D:\Blockchain")
# client.uploadfile()
# client.viewfile("QmQVZakc4EEmdZpFgP9PgWGPPkyDwphBraf3prLUpi9hgq")
