from typing import List


class Problem:

    def __init__(
        self,
        japanese: str,
        english: str,
        description: str,
    ) -> None:
        self.japanese = japanese
        self.english = english


problems: List[Problem] = [
    Problem(
        japanese='Pythonのインタプリタがあると便利ですが、すべての例は自己完結しているので、オフラインでも読むことができます。',
        english='It helps to have a Python interpreter handy for hands-on experience, but all examples are self-contained, so the tutorial can be read off-line as well.',
        description='',
    ),
    Problem(
        japanese='一度、本当にハマってしまうと',
        english='Once you are really hooked,',
        description='',
    ),
]
