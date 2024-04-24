from config.config import Config
from utils.VideoCapture.videoCapture import videoCapture

# utils / VideoCapture/ videoCapture.py

# main
def main():
    if Config.DEGUG == True:
        print('Debug mode is enabled')
    else:
        print('Debug mode disabled')
    
    # Capture video
    videoCapture()





if __name__ == '__main__':
    main()

