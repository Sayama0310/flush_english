import curses
from util import max_len


class FlushApp:

    def __init__(self) -> None:
        pass

    def home_screen(self):
        # スクリーンの初期化
        screen = curses.initscr()
        # カーソルを非表示にする
        curses.curs_set(0)
        # キー入力を有効にする
        screen.keypad(True)
        # 画面をクリアする
        screen.clear()
        screen.refresh()

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

        ### ページ遷移選択肢を表示 ###
        current_index = 0
        EXAM = 'Exam'
        EDIT = 'Edit'
        REPORT = 'Report'
        PADDING = 10
        edit_start = screen.getmaxyx()[1] // 2 - len(EDIT)
        exam_start = edit_start - PADDING - len(EXAM)
        report_start = edit_start + len(EDIT) + PADDING
        pages = [EXAM, EDIT, REPORT]
        pages_start = [exam_start, edit_start, report_start]
        y = 3 * screen.getmaxyx()[0] // 4

        while True:
            self._refresh_pages(pages, pages_start, current_index, y, screen)

            # キー入力を待つ
            key = screen.getch()

            # 矢印キーで選択肢を移動する
            if key == curses.KEY_LEFT and current_index > 0:
                current_index -= 1
            elif key == curses.KEY_RIGHT and current_index < len(pages) - 1:
                current_index += 1

            # Enterキーで選択する
            elif key == curses.KEY_ENTER or key in [10, 13]:
                chosen = pages[current_index]
                if chosen == EXAM:
                    self.exam_screen()
                elif chosen == EDIT:
                    self.edit_screen()
                elif chosen == REPORT:
                    self.report_screen()
                break

        # スクリーンの終了処理
        curses.endwin()

    def _refresh_pages(self, pages, pages_start, current_index, y, screen):
        for page, page_start in zip(pages, pages_start):
            if pages[current_index] == page:
                screen.addstr(y, page_start, page, curses.A_REVERSE)
            else:
                screen.addstr(y, page_start, page)
        screen.refresh()

    def exam_screen(self):
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
            screen.addstr(screen.getmaxyx()[0]-1, 0, input)
            screen.refresh()
            while True:
                key = screen.getch()
                if key == curses.KEY_ENTER or key in [10, 13]:
                    if input.strip(':').lower == "home":
                        self.home_screen()
                        pass
                    break
                input += chr(key)
                screen.addstr(screen.getmaxyx()[0], 0, input)
                screen.refresh()

        # スクリーンの終了処理
        curses.endwin()

    def edit_screen(self):
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

    def report_screen(self):
        # スクリーンの初期化
        screen = curses.initscr()
        # カーソルを非表示にする
        curses.curs_set(0)
        # キー入力を有効にする
        screen.keypad(True)
        # 画面をクリアする
        screen.clear()
        screen.refresh()

        ### Reportページ ###
        exam = "this page is report"
        x = screen.getmaxyx()[1] // 2 - len(exam) // 2
        y = screen.getmaxyx()[0] // 2
        screen.addstr(y, x, exam)

        screen.refresh()
        screen.getch()

        # スクリーンの終了処理
        curses.endwin()


if __name__ == '__main__':
    FlushApp().home_screen()
