import curses


def edit_screen():
    # スクリーンの初期化
    screen = curses.initscr()
    # カーソルを非表示にする
    curses.curs_set(0)
    # キー入力を有効にする
    screen.keypad(True)
    # 画面をクリアする
    screen.clear()
    screen.refresh()

    ### Editページ ###
    exam = "this page is edit"
    x = screen.getmaxyx()[1] // 2 - len(exam) // 2
    y = screen.getmaxyx()[0] // 2
    screen.addstr(y, x, exam)

    screen.refresh()
    screen.getch()

    # スクリーンの終了処理
    curses.endwin()
