import cv2
import mediapipe as mp
import time
import numpy as np
import pyautogui as mouse
import pandas as pd

import math
import win32gui, win32api, win32con

data_list = ['up_down', 'click', 'press_hold', 'relax', 'circle']
time_list = [15, 15, 10, 10, 10]


def get_data(filename, timepr):
    cap = cv2.VideoCapture(2, cv2.CAP_DSHOW)
    width, height = mouse.size()
    #cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  #设置宽度
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    mpDraw = mp.solutions.drawing_utils
    #mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    # # 帧率统计
    # pTime = 0
    # cTime = 0

    # # mouse.FAILSAFE = False
    # x, y = mouse.position()
    # arr_x = np.array([0, 0, 0], dtype=float)
    # arr_y = np.array([0, 0, 0], dtype=float)
    # arr_F_Z = np.array([0, 0, 0], dtype=float)
    # arr_F_Y = np.array([0, 0, 0], dtype=float)
    # x = 0.0
    # y = 0.0
    start = time.time()
    with mp_hands.Hands(max_num_hands=1,
                        min_detection_confidence=0.8,
                        min_tracking_confidence=0.8) as hands:

        while True:
            success, img = cap.read()
            img = cv2.flip(img, 1)
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #转换为rgb
            results = hands.process(imgRGB)

            #print(results.multi_hand_landmarks)
            if results.multi_hand_landmarks:
                #start = time.time()
                keypoints = []
                # for handLms in results.multi_hand_landmarks:
                #     hand_landmarks = results.multi_hand_landmarks[0]
                #     for data_point in handLms.landmark:
                #         keypoints.append({
                #             'X': data_point.x,
                #             'Y': data_point.y,
                #             'Z': data_point.z,
                #             'Visibility': data_point.visibility,
                #         })
                for handLms in results.multi_hand_landmarks:
                    #hand_landmarks = results.multi_hand_landmarks[0]
                    for _, data_point in enumerate(handLms.landmark):
                        keypoints += [data_point.x, data_point.y, data_point.z]
                        mpDraw.draw_landmarks(img, handLms,
                                              mp_hands.HAND_CONNECTIONS)
                        dataframe = pd.DataFrame(keypoints)
                    #print((keypoints[0:]["x"]))
                    # mean_x = (mean([keypoints[0]["X"],keypoints[5]["X"],keypoints[17]["X"],keypoints[12]["X"]])) #选取几个手指的平均
                    # mean_y = (mean([keypoints[0]["Y"],keypoints[5]["Y"],keypoints[17]["Y"],keypoints[12]["Y"]]))
                    # F_Z = keypoints[8]["Z"]
                    # F_Y = keypoints[8]["Y"]
                    # #keypoints[0]['X']
                    # #print(mean_x,mean_y)

                    # #print((width) * (mean_x), (height) * (mean_y))
                    # x = (width*2) * (mean_x) - width*0.5
                    # y = (height*2) * (mean_y) - height*0.5
                    # F_Z = (height*1.5) * (F_Z) - height*0.2
                    # F_Y = (height*1.5) * (F_Y) - height*0.2

                    # if x < 0:
                    #     x = 0
                    # if y < 0:
                    #     y = 0
                    # if x > width:
                    #     x = width
                    # if y > height:
                    #     y = height

                    # arr_F_Y[2] = arr_F_Y[1]
                    # arr_F_Z[2] = arr_F_Z[1]
                    # arr_F_Y[1] = arr_F_Y[0]
                    # arr_F_Z[1] = arr_F_Z[0]
                    # arr_F_Z[0] = F_Z
                    # arr_F_Y[0] = F_Y

                    # arr_y[2] = arr_y[1]
                    # arr_x[2] = arr_x[1]
                    # arr_y[1] = arr_y[0]
                    # arr_x[1] = arr_x[0]
                    # arr_x[0] = x
                    # arr_y[0] = y

                    # avg_x = np.mean(arr_x)#增加稳定性
                    # avg_y = np.mean(arr_y)
                    # win32api.SetCursorPos((int(avg_x), int(avg_y)))#快的很

                    # print("YY: ",arr_F_Y[2] - arr_F_Y[0])
                    # print("ZZ: ",arr_F_Z[2] - arr_F_Z[0])

                    #老的点击 （弱小
                    # if abs(arr_F_Y[2] - arr_F_Y[0])>160 and abs(arr_F_Z[2] - arr_F_Z[0])>25:
                    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 200, 200, 0, 0)
                    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 200, 200, 0, 0)
                    #     #time.sleep(0.2)

                    #新的点击 （强大
                    # index_finger_top = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    # index_finger_second = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP]

                    # distence = np.sqrt(np.sum(np.square(np.array([index_finger_top.x,index_finger_top.y])-np.array([index_finger_second.x,index_finger_second.y]))))
                    # deep = index_finger_top.z - index_finger_second.z

                    # distence = distence*1980
                    # print(distence)
                    # if distence < 80 and abs(arr_F_Z[2] - arr_F_Z[0])>25:
                    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 200, 200, 0, 0)

                    # if distence > 80 and abs(arr_F_Z[2] - arr_F_Z[0])>25:
                    #     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 200, 200, 0, 0)

                    # mouse.moveTo(int(avg_x), int(avg_y),duration=0)#慢
                    # print(mouse.position())

                    #判断手势

                    # centerPoint_x, centerPoint_y = np.sum(center, axis=0) / 4
                    # for id, lm in enumerate(handLms.landmark):
                    #     print(id, lm)
                    #     # 获取手指关节点
                    #     h, w, c = img.shape
                    #     cx, cy = int(lm.x*w), int(lm.y*h)
                    #     cv2.putText(img, str(int(id)), (cx+10, cy+10), cv2.FONT_HERSHEY_PLAIN,
                    #                 1, (0, 0, 255), 2)
                    mpDraw.draw_landmarks(img, handLms,
                                          mp_hands.HAND_CONNECTIONS)
            else:
                keypoints = [0] * 63
            # 统计屏幕帧率
            # cTime = time.time()
            # fps = 1 / (cTime - pTime)
            # pTime = cTime
            # cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
            #             (255, 0, 255), 3)
            dataframe = pd.DataFrame(keypoints)
            (dataframe.T).to_csv('./' + filename + '.csv',
                                 mode='a',
                                 header=False,
                                 index=False)
            cv2.imshow("FMS", img)
            end = time.time()
            print(end - start)
            if (end - start) > timepr:
                break
            if cv2.waitKey(2) & 0xFF == 27:
                break
        cap.release()


if __name__ == "__main__":
    for i in range(len(data_list)):
        time.sleep(1)
        print(data_list[i], time_list[i])
        get_data(data_list[i], time_list[i])
        print("Next")

    print("お疲れ様です")
