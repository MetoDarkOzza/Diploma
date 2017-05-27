import cv2
import time
import sys
import os
import signature

def stream():
    cap = cv2.VideoCapture(0)
    fps = 20.0
    keylength = 160
    timepiece = 1
    numFrames = fps * timepiece
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    count = 0
    os.chdir('C:/Users/Кирилл/Desktop/video')
    keys = signature.genKeys(keylength)
    while(cap.isOpened()):
        count += 1
        filename = 'vid' + str(count) + '.avi'
        signature.writekeytofile(filename, keys[1])
        out = cv2.VideoWriter(filename,fourcc, fps, (640,480))
        for i in range(int(numFrames)):
            ret, frame = cap.read()
            if ret==True:
                # write the flipped frame
                out.write(frame)
                cv2.imshow('frame',frame)
                if cv2.waitKey(40) & 0xFF == ord('q'):
                    out.release()
                    exit()
            else:
                break
        out.release()
        signature.createSignature(filename, keys[0])
        keys = signature.genKeys(keylength)




    cap.release()
    cv2.destroyAllWindows()

def playvideo():
    mas = ['1.avi', '5.avi']
    for i in range(len(mas)):
        cap = cv2.VideoCapture('./vidos/' + str(mas[i]))

        while True:

            ret, frame = cap.read()

            if ret == True:

                # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                cv2.imshow('frame', frame)

            if cv2.waitKey(30) & 0xFF == ord('q'):
                 break

            else:
                break


        cap.release()

    cv2.destroyAllWindows()

def playvideo2(name):
    cap = cv2.VideoCapture('./vidos/' + str(name))

    while True:

        ret, frame = cap.read()

        if ret == True:

            #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cv2.imshow('frame', frame)

            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

        else:
            break

    cap.release()
    cv2.destroyAllWindows()

def sort_col(i):
    return int(i[3:-4:1])

def concatinate():
    # this two lines are for loading the videos.
    # in this case the video are named as: cut1.mp4, cut2.mp4, ..., cut15.mp4
    videofiles = [n for n in os.listdir('./vidos') if n[0] == 'v' and n[-4:] == '.avi']
    print(videofiles)
    videofiles = sorted(videofiles, key=lambda item: int(item.partition('.')[0][3:]))
    print(videofiles)
    video_index = 0
    cap = cv2.VideoCapture('./vidos/' + str(videofiles[0]))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # video resolution: 1624x1234 px
    out = cv2.VideoWriter("video.avi",
                          fourcc,
                          15, (640, 480), 1)

    while (cap.isOpened()):
        videofiles = [n for n in os.listdir('./vidos') if n[0] == 'v' and n[-4:] == '.avi']
        print(videofiles)
        videofiles = sorted(videofiles, key=lambda item: int(item.partition('.')[0][3:]))
        ret, frame = cap.read()
        if frame is None:
            print("end of video " + str(video_index) + " .. next one now")
            video_index += 1
            if video_index >= len(videofiles):
                break
            cap = cv2.VideoCapture('./vidos/'+ videofiles[video_index])
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


def concatinate1():
    # this two lines are for loading the videos.
    # in this case the video are named as: cut1.mp4, cut2.mp4, ..., cut15.mp4
    os.chdir('C:/Users/Кирилл/Desktop/video')
    videofiles = [n for n in os.listdir('.') if n[0] == 'v' and n[-4:] == '.avi']
    print(videofiles)
    videofiles = sorted(videofiles, key=lambda item: int(item.partition('.')[0][3:]))
    print(videofiles)
    video_index = 0
    cap = cv2.VideoCapture(str(videofiles[0]))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # video resolution: 1624x1234 px
    out = cv2.VideoWriter("./newvid/video.avi",
                          fourcc,
                          15, (640, 480), 1)

    while (cap.isOpened()):
        videofiles = [n for n in os.listdir('.') if n[0] == 'v' and n[-4:] == '.avi']
        print(videofiles)
        videofiles = sorted(videofiles, key=lambda item: int(item.partition('.')[0][3:]))
        ret, frame = cap.read()
        if frame is None:
            print("end of video " + str(video_index) + " .. next one now")
            video_index += 1
            if video_index >= len(videofiles):
                break
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