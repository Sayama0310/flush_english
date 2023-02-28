import curses

# from pages.home import home_screen


def exam_screen():
    # スクリーンの初期化
    screen = curses.initscr()
    # カーソルを非表示にする
    curses.curs_set(0)
    # キー入力を有効にする
    screen.keypad(True)
    # 画面をクリアする
    screen.clear()
    screen.refresh()

    ### Examページ ###
    exam = "this page is exam"
    x = screen.getmaxyx()[1] // 2 - len(exam) // 2
    y = screen.getmaxyx()[0] // 2
    screen.addstr(y, x, exam)

    screen.refresh()

    ### : でページ遷移 ###
    key = screen.getch()
    input = ":"
    if key == ord(':'):
        screen.addstr(screen.getmaxyx()[0], 0, input)
        screen.refresh()
        while True:
            key = screen.getch()
            if key == curses.KEY_ENTER or key in [10, 13]:
                if input.strip(':').lower == "home":
                    # home_screen()
                    pass
                break
            input += chr(key)
            screen.addstr(screen.getmaxyx()[0], 0, input)
            screen.refresh()

    # スクリーンの終了処理
    curses.endwin()
