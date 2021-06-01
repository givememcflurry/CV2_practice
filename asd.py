# 객체지향 과제 :)
# Sample 영상정보 : 24fps, MP4
# 실제로는 카메라 영상으로 해야되기 때문에 동영상 편집&저장 개념보단 영상변환재생에 초점
import cv2
import os


def cpd():  # 현재 디렉토리 확인
    os.getcwd()  # 현재 파이썬프로젝트 폴더 위치 표시


def run(video_name):  # CV2로 동영상 재생
    input_video = video_name

    cap = cv2.VideoCapture(input_video)  # 동영상 캡처 객체 생성
    if cap.isOpened():  # 캡쳐객체 초기화 확인 (동영상을 불러올 수 있는지 확인하는듯)
        while True:  # 무한루프
            able, frame = cap.read()  # Run-able, Frame
            if able:  # run = True (캡쳐 객체 호출가능) : 동영상 재생시작
                cv2.imshow(input_video, frame)  # Show captured frame of input_video
                cv2.waitKey(25)  # 25ms = 40fps

            else:  # run = False (캡쳐 객체 호출불가능) : 동영상 자동 종료
                cap.release()  # 캡쳐 자원 반납
                cv2.destroyAllWindows()  # 창종료
    else:
        print("can't open")


def data(video_name):  # 동영상의 정보를 보여줌 (cap.get)
    input_video = video_name
    cap = cv2.VideoCapture(input_video)

    fps = cap.get(cv2.CAP_PROP_FPS)  # 초당 프레임
    print("Frame : ", fps)

    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 동영상 세로길이
    print("Height : ", height)

    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 동영상 가로길이
    print("Width : ", width)

    cap.release()