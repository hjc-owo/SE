import os


class Black:

    def __init__(self, id):
        self.cmd = 'cd Black & black_box'
        self.id = id

    # 返回身份证号码是否合法，是为 1，不是为 0
    def exec(self):
        with os.popen(self.cmd + ' ' + str(self.id)) as res:
            return int(res.readlines()[0])
