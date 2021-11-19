import dropbox

class Dropbox_cloudstorage:
    def __init__(self, access_token):
        self.access_token = access_token

    def download_file(self):
        pass

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox
        """
        dropbox_client = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dropbox_client.files_upload(f.read(), file_to)

# with open("secure_info.txt", "r") as file:
#     token = file.read()
#
# source = "secure_info.txt"
# dropboxpath = "/Privacy of Blockchain/test.txt"
# # dropbox client
# client = dropbox.Dropbox(token)
# with open("secure_info.txt", "rb") as file:
#     client.files_upload(file.read(), dropboxpath)

