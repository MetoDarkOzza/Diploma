import cv2
import time
import sys
import os
import signature

def recieve():
        # this two lines are for loading the videos.
        # in this case the video are named as: cut1.mp4, cut2.mp4, ..., cut15.mp4
    os.chdir('C:/Users/Кирилл/Desktop/video')
    videofiles = [n for n in os.listdir('.') if n[0] == 'v' and n[-4:] == '.avi']

    videofiles = sorted(videofiles, key=lambda item: int(item.partition('.')[0][3:]))
    #print(videofiles)
    video_index = 0
    openkey = signature.readopenkey(videofiles[0])
    print(openkey)
    signa = signature.readsignature(videofiles[0])
    if(signature.verify(signa,openkey, videofiles[0]) == 1):

        cap = cv2.VideoCapture(str(videofiles[0]))
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        # video resolution: 1624x1234 px
        out = cv2.VideoWriter("./newvid/video.avi",
                              fourcc,
                              15, (640, 480), 1)

        while (cap.isOpened()):
            videofiles = [n for n in os.listdir('.') if n[0] == 'v' and n[-4:] == '.avi']
            videofiles = sorted(videofiles, key=lambda item: int(item.partition('.')[0][3:]))

            ret, frame = cap.read()
            if frame is None:
                print("end of video " + str(video_index) + " .. next one now")
                video_index += 1
                openkey = signature.readopenkey(videofiles[video_index])
                signa = signature.readsignature(videofiles[video_index])
                if video_index >= len(videofiles):
                    break
                if (signature.verify(signa, openkey, videofiles[video_index]) == 0):
                    print('Video is under attack in part ' + str(video_index+1))
                    exit()

                cap = cv2.VideoCapture(videofiles[video_index])
                ret, frame = cap.read()
            cv2.imshow('stream', frame)
            out.write(frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()

        print
        "end."
    else:
        print('smth is wrong')
        exit()
def main():
    # os.chdir('C:/Users/Кирилл/Desktop/video')
    # keys = signature.genKeys(160)
    #
    # signature.createSignature('vid1.avi', keys[0])
    # signature.writekeytofile('vid1.avi', keys[1])
    # opk = signature.readopenkey('vid1.avi')
    # signa = signature.readsignature('vid1.avi')
    # print(signature.verify(signa,opk,'vid1.avi'))



    recieve()

if __name__ == '__main__':
    main()