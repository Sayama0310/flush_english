import curses

# スクリーンの初期化
screen = curses.initscr()

# カーソルを非表示にする
curses.curs_set(0)

# 文字列を表示する座標を計算する
x = screen.getmaxyx()[1] // 2 - len("Flush") // 2
y = screen.getmaxyx()[0] // 2

# 文字列を表示する
screen.addstr(y, x, "Flush")

# 変更を反映する
screen.refresh()

# キー入力待ち
screen.getch()

# スクリーンの終了処理
curses.endwin()
