import dropbox
import os

class TransferData:
    def __init__(self, passcode):
        self.passcode = passcode

    def upload_file(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.passcode)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)


def main():
    passcode="sl.A0bUItI3IjIbPZrguuAJtfe4hBSN_X1WT4WKkK-9FL_H5Wq4z3FbMuAGI9eLYKDNLvY5SqEN8O6CfMfZ7jyCETNz5FNIrYAYtila0G6qcXROl3XDoIwEo1QySrqn0gNJlpVMJ_U"
    transferData = TransferData(passcode)

    file_from = input("PLEASE GIVE THE PATH OF YOUR 'FILE' OR 'FOLDER' :")
    file_to = input("PLEASE ENTER THE PATH FOR DROPBOX :") 
    
    transferData.upload_file(file_from, file_to)
   # print("YOU HAVE SUCESSFULLY MOVED YOUR FILE!")

main()                
