import curses

# スクリーンの初期化
screen = curses.initscr()

# カーソルを非表示にする
curses.curs_set(0)

# キー入力を有効にする
screen.keypad(True)

# 文字列を表示する座標を計算する
x = screen.getmaxyx()[1] // 2 - len("Flush") // 2
y = screen.getmaxyx()[0] // 2 - 8

# 文字列を表示する
screen.addstr(y, x, "Flush")

# 選択肢のリスト
choices = ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4', 'Choice 5']

# 選択された選択肢のインデックス
current_choice = 0

# 選択肢を表示する座標を計算する
max_y, max_x = screen.getmaxyx()
start_y = max_y // 2 - len(choices) // 2
start_x = max_x // 2 - max([len(choice) for choice in choices]) // 2

# 選択肢を表示する
while True:
    for i, choice in enumerate(choices):
        if i == current_choice:
            # 選択された選択肢は反転表示する
            screen.addstr(start_y+i, start_x, choice, curses.A_REVERSE)
        else:
            screen.addstr(start_y+i, start_x, choice)

    # 変更を反映する
    screen.refresh()

    # キー入力を待つ
    key = screen.getch()

    # 矢印キーで選択肢を移動する
    if key == curses.KEY_UP and current_choice > 0:
        current_choice -= 1
    elif key == curses.KEY_DOWN and current_choice < len(choices)-1:
        current_choice += 1

    # Enterキーで選択する
    elif key == curses.KEY_ENTER or key in [10, 13]:
        chosen = choices[current_choice]
        screen.addstr(max_y-1, 0, f"You chose {chosen}. Press any key to exit.")
        screen.refresh()
        screen.getch()
        break

# 変更を反映する
screen.refresh()

# スクリーンの終了処理
curses.endwin()
