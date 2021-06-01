# 객체지향 과제 :)
# Sample 영상정보 : 24fps, MP4
# 실제로는 카메라 영상으로 해야되기 때문에 동영상 편집&저장 개념보단 영상변환재생에 초점
# OpenCV에선 색을 표현할 경우 BGR 순으로 표현

import cv2
import os
import numpy as np
import operator


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


def bip(video_name):  # background image processing (배경이미지 처리함수)
    input_video = video_name
    cap = cv2.VideoCapture(input_video)  # 동영상 캡처 객체 생성
    fps = cap.get(cv2.CAP_PROP_FPS)  # 초당 프레임
    fwt = round((1 / fps) * 1000)  # 프레임당 재생시간 설정 & 입력단위가 ms이므로 *1000 & 정수입력으로 round처리

    cbs = cv2.createBackgroundSubtractorKNN()  # 배경제거 객체생성함수 선언

    if cap.isOpened():  # 캡쳐객체 초기화 확인 (동영상을 불러올 수 있는지 확인하는듯)

        while cap.isOpened():  # 초기화 되는동안 영상재생
            ret, frame = cap.read()  # 프레임 추출가능(T/F), 추출한프레임

            if ret:  # run = True (캡쳐 객체 호출가능) : 동영상 재생시작
                frame = cv2.resize(frame, (720, 480))  # 프레임이미지 크기 변환 720*480
                rmbg_frame = cbs.apply(frame)  # 배경제거한 프레임 생성
                back_frame = cbs.getBackgroundImage()  # 배경 프레임 생성

                cv2.imshow(input_video, frame)  # 입력비디오의 프레임 이미지를 보여줌
                cv2.imshow("rmbg_" + input_video, rmbg_frame)  # 배경제거된 프레임 이미지를 보여줌
                cv2.imshow("back_" + input_video, back_frame)  # 배경 프레임 이미지를 보여줌

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


def scs(video_name):  # screenshot (영상 이미지 저장)
    input_video = video_name
    cap = cv2.VideoCapture(input_video)  # 동영상 캡처 객체 생성
    fps = cap.get(cv2.CAP_PROP_FPS)  # 초당 프레임
    fwt = round((1 / fps) * 1000)  # 프레임당 재생시간 설정 & 입력단위가 ms이므로 *1000 & 정수입력으로 round처리

    cbs = cv2.createBackgroundSubtractorKNN()  # 배경제거 객체생성함수 선언

    if cap.isOpened():  # 캡쳐객체 초기화 확인 (동영상을 불러올 수 있는지 확인하는듯)

        while cap.isOpened():  # 초기화 되는동안 영상재생
            ret, frame = cap.read()  # 프레임 추출가능(T/F), 추출한프레임

            if ret:  # run = True (캡쳐 객체 호출가능) : 동영상 재생시작
                origin_frame = cv2.resize(frame, (720, 480))  # 프레임이미지 크기 변환 720*480
                rmbg_frame = cbs.apply(origin_frame)  # 배경제거한 프레임 생성
                back_frame = cbs.getBackgroundImage()  # 배경 프레임 생성 (입력값X : 자동으로 현재 출력중인 영상을 처리함)

                cv2.imshow(input_video, origin_frame)  # 입력비디오의 프레임 이미지를 보여줌
                cv2.imshow('rmbg_' + input_video, rmbg_frame)  # 배경제거된 프레임 이미지를 보여줌
                cv2.imshow('back_' + input_video, back_frame)  # 배경 프레임 이미지를 보여줌

                if cv2.waitKey(1) == ord('s'):  # 's'입력시 함수 동작
                    frame_count = cap.get(cv2.CAP_PROP_POS_FRAMES)  # 현재 프레임 번호지정
                    cv2.imwrite('image/' + str(frame_count) + '_origin.jpg', origin_frame)  # 해당 프레임 이미지 저장
                    cv2.imwrite('image/' + str(frame_count) + '_rmbg.jpg', rmbg_frame)
                    cv2.imwrite('image/' + str(frame_count) + '_back.jpg', back_frame)

                if cv2.waitKey(1) == ord('d'):  # 's'입력시 함수 동작
                    print(rmbg_frame[0, 0])
                    print(rmbg_frame[85, 207])

                if cv2.waitKey(fwt - 2) == ord('q'):  # fps만큼 재생하다가 'q'입력되면 동작 종료
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


def pro(origin_data, rmbg_data, back_data):  # Processing : 추출한 프레임 이미지 합성 (frame == data != image file)

    height, width, channel = origin_data.shape  # 높이, 넓이, 색채널 추출
    proc_data = np.full((height, width, 3), (0, 255, 0), dtype=np.uint8)  # 처리용 이미지 데이터 선언
    hi_cnt, wd_cnt = 0, 0  # 높이, 넓이 카운터용 변수 선언

    while hi_cnt < height:  # 높이 반복
        while wd_cnt < width:  # 넓이 반복
            origin_pixel = origin_data[hi_cnt, wd_cnt]  # 픽셀 BGR 리스트 추출
            o_blu, o_grn, o_red = origin_pixel[0], origin_pixel[1], origin_pixel[2]  # BGR 값을 변수로 치환

            r_blk = rmbg_data[hi_cnt, wd_cnt]  # rmbg는 흑백값만 추출

            back_pixel = back_data[hi_cnt, wd_cnt]
            b_blu, b_grn, b_red = back_pixel[0], back_pixel[1], back_pixel[2]

            if (r_blk != 0) or (str(origin_pixel) != str(back_pixel)):  # r_blk가 검은색(0)이 아닐경우 & 빠른 연산을 위해 oprator.is_not
                proc_data[hi_cnt, wd_cnt] = origin_data[hi_cnt, wd_cnt]
                proc_data[hi_cnt + 1, wd_cnt] = origin_data[hi_cnt + 1, wd_cnt]
                proc_data[hi_cnt, wd_cnt + 1] = origin_data[hi_cnt, wd_cnt + 1]
                proc_data[hi_cnt + 1, wd_cnt + 1] = origin_data[hi_cnt + 1, wd_cnt + 1]

            wd_cnt = wd_cnt + 2

        hi_cnt = hi_cnt + 2
        wd_cnt = 0

    return proc_data


def shc(input_image):  # 이미지 처리방식 확인
    input_data = np.full((100, 200, 3), (0, 255, 0), dtype=np.uint8)
    while True:
        cv2.imshow('input_image', input_image)
        cv2.imshow('input_data', input_data)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()  # 창종료


def vdf(video_name):  # video processing function (영상 처리 함수)
    input_video = video_name
    cap = cv2.VideoCapture(input_video)  # 동영상 캡처 객체 생성
    fps = cap.get(cv2.CAP_PROP_FPS)  # 초당 프레임
    fwt = round((1 / fps) * 1000)  # 프레임당 재생시간 설정 & 입력단위가 ms 이므로 *1000 & 정수입력으로 round 처리

    cbs = cv2.createBackgroundSubtractorKNN()  # 배경제거 객체생성함수 선언

    if cap.isOpened():  # 캡쳐객체 초기화 확인 (동영상을 불러올 수 있는지 확인하는듯)

        while cap.isOpened():  # 초기화 되는동안 영상재생
            ret, frame = cap.read()  # 프레임 추출가능(T/F), 추출한프레임

            if ret:  # run = True (캡쳐 객체 호출가능) : 동영상 재생시작
                origin_frame = cv2.resize(frame, (480, 320))  # 프레임이미지 크기 변환 480*320
                rmbg_frame = cbs.apply(origin_frame)  # 배경제거한 프레임 생성
                back_frame = cbs.getBackgroundImage()  # 배경 프레임 생성 (입력값 X : 자동으로 현재 출력중인 영상을 처리함)
                proc_frame = pro(origin_frame, rmbg_frame, back_frame)

                cv2.imshow(input_video, origin_frame)  # 입력비디오의 프레임 이미지를 보여줌
                cv2.imshow('rmbg_' + input_video, rmbg_frame)  # 배경제거된 프레임 이미지를 보여줌
                cv2.imshow('back_' + input_video, back_frame)  # 배경 프레임 이미지를 보여줌
                cv2.imshow('proc_' + input_video, proc_frame)

                if cv2.waitKey(1) == ord('q'):  # fps 만큼 재생하다가 'q' 입력되면 동작 종료
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