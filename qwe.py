import cv2
import os
import numpy as np
import time


def cpd():  # 현재 디렉토리 확인
    return os.getcwd()  # 현재 파이썬프로젝트 폴더 위치 표시


def pro(origin_data, rmbg_data, bgnd_data):  # Processing : 추출한 프레임 이미지 합성 (frame == data != image file)

    height, width, channel = origin_data.shape  # 높이, 넓이, 색채널 추출
    proc_data = bgnd_data  # 처리용 이미지 데이터 선언
    hi_cnt, wd_cnt = 0, 0  # 높이, 넓이 카운터용 변수 선언

    while hi_cnt < height:  # 높이 반복
        while wd_cnt < width:  # 넓이 반복

            r_blk = rmbg_data[hi_cnt, wd_cnt]  # rmbg는 흑백값만 추출

            if (r_blk != 0):  #
                proc_data[hi_cnt, wd_cnt] = origin_data[hi_cnt, wd_cnt]
                proc_data[hi_cnt + 1, wd_cnt] = origin_data[hi_cnt + 1, wd_cnt]
                proc_data[hi_cnt, wd_cnt + 1] = origin_data[hi_cnt, wd_cnt + 1]
                proc_data[hi_cnt + 1, wd_cnt + 1] = origin_data[hi_cnt + 1, wd_cnt + 1]

            wd_cnt = wd_cnt + 2

        hi_cnt = hi_cnt + 2
        wd_cnt = 0

    return proc_data


def cam(bgnd_name):  # video processing function (영상 처리 함수)
    start_time = time.time()

    bgnd_video = bgnd_name

    cap_input = cv2.VideoCapture(0)  # 동영상 캡처 객체 생성
    cap_bgnd = cv2.VideoCapture(bgnd_video)  # 동영상 캡처 객체 생성

    fps = cap_input.get(cv2.CAP_PROP_FPS)  # 초당 프레임
    fwt = round((1 / fps) * 1000)  # 프레임당 재생시간 설정 & 입력단위가 ms 이므로 *1000 & 정수입력으로 round 처리

    cbs = cv2.createBackgroundSubtractorKNN()  # 배경제거 객체생성함수 선언

    if cap_input.isOpened() and cap_bgnd.isOpened():  # 캡쳐객체 초기화 확인 (동영상을 불러올 수 있는지 확인하는듯)

        while cap_input.isOpened():  # 초기화 되는동안 영상재생
            ret_input, frame_input = cap_input.read()  # 프레임 추출가능(T/F), 추출한프레임
            ret_bgnd, frame_bgnd = cap_bgnd.read()

            if ret_input and ret_bgnd:  # run = True (캡쳐 객체 호출가능) : 동영상 재생시작
                orgn_frame = cv2.resize(frame_input, (480, 320))  # 프레임이미지 크기 변환 480*320
                bgnd_frame = cv2.resize(frame_bgnd, (480, 320))
                rmbg_frame = cbs.apply(orgn_frame)  # 배경제거한 프레임 생성

                proc_frame = pro(orgn_frame, rmbg_frame, bgnd_frame)

                cv2.imshow('cam_video', orgn_frame)  # 입력비디오의 프레임 이미지를 보여줌
                cv2.imshow('proc_video', proc_frame)

                if cv2.waitKey(fwt) == ord('q'):  # fps 만큼 재생하다가 'q' 입력되면 동작 종료
                    cap_input.release()
                    cap_bgnd.release()
                    cv2.destroyAllWindows()
                    print("Stop video")
                    break

            else:  # run = False (캡쳐 객체 호출불가능) : 동영상 자동 종료
                cap_input.release()
                cap_bgnd.release()
                cv2.destroyAllWindows()  # 창종료
                print("End of playback")
                print("Time : ", time.time() - start_time)

    else:
        print("Can't open")