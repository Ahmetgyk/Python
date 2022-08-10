import cv2
from PIL import Image
import matplotlib.pyplot as plt

imgs = []
reimgs = []



  
def main():
    try:
        vidcap = cv2.VideoCapture('Pexels Videos 1572321.mp4')
        def getFrame(sec):
            vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
            hasFrames,image = vidcap.read()
            if hasFrames:
                cv2.imwrite("resimler\image"+str(count)+".jpg", image)

                imgs.append(image)

                reimg = Image.open("resimler\image9.jpg")
                reimg.thumbnail((100, 100))

                reimgs.append(reimg)
        
            return hasFrames
        sec = 0
        frameRate = 0.1
        count=1
        success = getFrame(sec)
        while success:
            count = count + 1
            sec = sec + frameRate
            sec = round(sec, 2)
            success = getFrame(sec)

        plt.imshow(cv2.cvtColor(imgs[2], cv2.COLOR_BGR2RGB))
        plt.title("imgs: 2")
        plt.show()
        plt.imshow(cv2.cvtColor(reimgs[2], cv2.COLOR_BGR2RGB))
        plt.title("reimgs: 2")
        plt.show()
    except IOError:
        pass
  
if __name__ == "__main__":
    main()