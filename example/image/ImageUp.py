from qiniu import Auth, put_file, etag


class ImageUp(object):
    bucket_name = 'pfxxz'

    def __init__(self):
        self.auth()

    def auth(self):
        access_key = 'RHnmjjHzSYiZpqdNP1_y538rp5djyyzZX8SpKIwg'
        secret_key = '3TUGGyFU8Oe_awsdBJE0HD_CPuWuA4yVWfBGBrua'
        self.auth = Auth(access_key, secret_key)

    def upload(self, key, localfile):
        token = self.auth.upload_token(self.bucket_name, key, 3600)
        return put_file(token, key, localfile)
