from tkinter import *
import random

# ウィンドウの作成
win = Tk()
cv = Canvas(win, width=640, height=480)
cv.pack()

ball_ichi_x = []
ball_ichi_y = []
ball_idou_x = 30
ball_idou_y = -30
ball_size = 10
ball_ichi_x_list = 0
ball_ichi_y_list = 0

for x in range(1, 50):
    ball_ichi_x.append(ball_ichi_x_list)
    ball_ichi_y.append(ball_ichi_y_list)
    ball_ichi_x_list = ball_ichi_x_list + 100
    ball_ichi_y_list = ball_ichi_x_list + 100
# 画面の描画


def draw_screen():
    # 画面クリア
    cv.delete('all')
    # キャンバス（画面）の作成
    cv.create_rectangle(0, 0, 640, 480, fill="white", width=0)


def draw_ball():
    # ボールを描
    for i in range(0, 49):
        cv.create_oval(ball_ichi_x[i] - ball_size, ball_ichi_y[i] - ball_size,
                       ball_ichi_x[i] + ball_size, ball_ichi_y[i] + ball_size, fill="red")

# ボールの移動


def move_ball():
    # 左右の壁に当たったかの判定
    global is_gameover, point, ball_ichi_x, ball_ichi_y, ball_idou_x, ball_idou_y
    for j in range(0, 49):
        if ball_ichi_x[j] + ball_idou_x < 0 or ball_ichi_x[j] + ball_idou_x > 640:
            ball_idou_x *= -1
        # 天井に当たったかの判定
        if ball_ichi_y[j] + ball_idou_y < 0 or ball_ichi_y[j] + ball_idou_y > 480:
            ball_idou_y *= -1
        if 0 <= ball_ichi_x[0] + ball_idou_x <= 640:
            ball_ichi_x[j] = ball_ichi_x[j] + ball_idou_x
        if 0 <= ball_ichi_y[j] + ball_idou_y <= 480:
            ball_ichi_y[j] = ball_ichi_y[j] + ball_idou_y


def game_loop():
    draw_screen()
    draw_ball()
    move_ball()
    win.after(50, game_loop)


# ゲームのメイン処理
game_loop()
win.mainloop()
