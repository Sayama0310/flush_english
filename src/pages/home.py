import curses
from typing import List


def max_len(strings: List[str]) -> int:
    length = 0
    for s in strings:
        if len(s) > length:
            length = len(s)
    return length


def home_screen():
    # スクリーンの初期化
    screen = curses.initscr()
    # カーソルを非表示にする
    curses.curs_set(0)
    # キー入力を有効にする
    screen.keypad(True)

    ### タイトルの表示 ###
    # 文字列を表示する座標を計算する
    title = """\
 _______ __               __
|    ___|  |.--.--.-----.|  |--.
|    ___|  ||  |  |__ --||     |
|___|   |__||_____|_____||__|__|
"""
    splitted_title = title.split('\n')
    x = screen.getmaxyx()[1] // 2 - max_len(splitted_title) // 2
    y = screen.getmaxyx()[0] // 4
    # タイトルを表示する
    for i in range(len(splitted_title)):
        screen.addstr(y + i, x, splitted_title[i])

    # 変更を反映する
    screen.refresh()
    screen.getch()

    # スクリーンの終了処理
    curses.endwin()


if __name__ == '__main__':
    home_screen()
