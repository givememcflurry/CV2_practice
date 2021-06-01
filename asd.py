# 객체지향 과제 :)
# Sample 영상정보 : 24fps, MP4
# 실제로는 카메라 영상으로 해야되기 때문에 동영상 편집&저장 개념보단 영상변환재생에 초점

import cv2
import os


def cpd():  # 현재 디렉토리 확인
    return os.getcwd()  # 현재 파이썬프로젝트 폴더 위치 표시


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


def wtk(image_name):  # waitkey 함수 동작 확인
    input_image = cv2.imread(image_name, cv2.IMREAD_UNCHANGED)
    cv2.imshow('Cyber Punk 2077', input_image)  # 이미지를 화면에 보여준다.
    key = cv2.waitKey(0)  # 키입력 무한대기(0이므로)하면서 입력한 키를 유니코드 값으로 리턴함.
    key_char = chr(key)  # 유니코드 값을 Char로 변환
    print('key : ', key_char)  # 입력한 키의 유니코드 값을 보여줌
    cv2.destroyAllWindows()


def run(video_name):  # CV2로 동영상 재생
    input_video = video_name
    cap = cv2.VideoCapture(input_video)  # 동영상 캡처 객체 생성
    fps = cap.get(cv2.CAP_PROP_FPS)  # 초당 프레임
    fwt = round((1 / fps) * 1000)  # 프레임당 재생시간 설정 & 정수입력으로 round처리

    if cap.isOpened():  # 캡쳐객체 초기화 확인 (동영상을 불러올 수 있는지 확인하는듯)

        while cap.isOpened():  # 초기화 되는동안 영상재생
            ret, frame = cap.read()  # Run-able, Frame

            if ret:  # run = True (캡쳐 객체 호출가능) : 동영상 재생시작
                cv2.imshow(input_video, frame)  # Show captured frame of input_video
                cv2.waitKey(fwt)  # 재생시간 입력 -> waitkey만 쓰면 단순대기 동작

            else:  # run = False (캡쳐 객체 호출불가능) : 동영상 자동 종료
                cap.release()  # 캡쳐 자원 반납
                cv2.destroyAllWindows()  # 창종료
                print("End of playback")

    else:
        print("can't open")


def fip(video_name):  # fore image processing (움직이는 영상만 따기 - 배경제거)
    input_video = video_name
    cap = cv2.VideoCapture(input_video)  # 동영상 캡처 객체 생성
    fps = cap.get(cv2.CAP_PROP_FPS)  # 초당 프레임
    fwt = round((1 / fps) * 1000)  # 프레임당 재생시간 설정 & 정수입력으로 round처리

    rmbg = cv2.createBackgroundSubtractorMOG2()  # 배경제거 객체생성

    if cap.isOpened():  # 캡쳐객체 초기화 확인 (동영상을 불러올 수 있는지 확인하는듯)

        while cap.isOpened():  # 초기화 되는동안 영상재생
            ret, frame = cap.read()  # Run-able, Frame

            if ret:  # run = True (캡쳐 객체 호출가능) : 동영상 재생시작
                rmbg_frame = rmbg.apply(frame)  # 배경제거한 프레임 생성
                cv2.imshow(input_video, frame)  # 입력비디오의 프레임 이미지를 보여줌
                cv2.imshow(input_video + "_rmbg", rmbg_frame)  # 배경제거된 프레임 이미지를 보여줌

                if cv2.waitKey(fwt) == ord('q'):  # fps만큼 재생하다가 q입력되면 동작 종료
                    cap.release()
                    cv2.destroyAllWindows()
                    print("Stop video")
                    break

            else:  # run = False (캡쳐 객체 호출불가능) : 동영상 자동 종료
                cap.release()  # 캡쳐 자원 반납
                cv2.destroyAllWindows()  # 창종료
                print("End of playback")

    else:
        print("Can't open")
