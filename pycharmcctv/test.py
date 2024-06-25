import cv2
import datetime
import os
import threading
import time
import math
import datetime

def writeVideo():
    # 현재시간 가져오기
    currentTime = datetime.datetime.now()
    print('time')
    # RTSP를 불러오는 곳
    video_capture = cv2.VideoCapture('rtsp://admin:admin123456@192.168.0.250:554')#cctv ip넣을것 앞에는 아이디 비번
    if not video_capture.isOpened():
        print('video is not open')
        exit(0)
    print('video capture')
    w = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # 캠 설정
    # video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, w//4)  # 영상 가로길이 설정
    # video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, h//4)  # 영상 세로길이 설정
    # w = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    # h = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # print(w, h)  # 640, 480

    fps = 30

    # 현재 시간을 '년도 달 일 시간 분 초'로 가져와서 문자열로 생성
    fileName = str(currentTime.strftime('%Y %m %d %H %M %S'))
    print(fileName)
    # 파일 저장하기 위한 변수 선언
    path = os.path.abspath(os.path.realpath(__file__))+"_"+fileName+'.mp4'
    print(path)
    # DIVX 코덱 적용 # 코덱 종류 # DIVX, XVID, MJPG, X264, WMV1, WMV2
    # 무료 라이선스의 이점이 있는 XVID를 사용
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # 비디오 저장
    # cv2.VideoWriter(저장 위치, 코덱, 프레임, (가로, 세로))
    out = cv2.VideoWriter(path, fourcc, fps, (w, h))

    time_laps = 0
    print('video creating...')
    while True:
        ret, frame = video_capture.read()
        # 촬영되는 영상보여준다. 프로그램 상태바 이름은 'streaming video' 로 뜬다.
        cv2.imshow('streaming video', frame)
        # 영상을 저장한다.
        out.write(frame)
        # print('writing')
        # 1ms뒤에 뒤에 코드 실행해준다.
        k = cv2.waitKey(1) & 0xff
        # 키보드 esc 누르면 종료된다.
        if k == 27:
            break
        # time.sleep(1)
    video_capture.release()  # cap 객체 해제
    out.release()  # out 객체 해제
    cv2.destroyAllWindows()
    print('video saving...')

if __name__ == "__main__":
    writeVideo()