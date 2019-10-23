import cell


def create_body(size_1, size_2):
    reply = []
    for x in range(size_1):
        temp = []
        for y in range(size_2):
            temp.append(cell.Cell())
        reply.append(temp)
    return reply


class Field:
    def __init__(self, size_1, size_2):
        self.body = create_body(size_2, size_1)
        self.count_empty = size_1 * size_2
        self.end = False
        self.create_puzzle = True

    def __str__(self):
        res_str = "*" * (len(self.body[0]) + 2) + "\n"
        for line in self.body:
            s = "*"
            for item in line:
                if item.value != -1:
                    s += str(item.value)
                else:
                    s += "-"
            s += "*\n"
            res_str += s
        return res_str + "*" * (len(self.body[0]) + 2)

    def put_value(self, x, y, value):
        if self.body[x][y].value == -1:
            self.count_empty -= 1
        if self.create_puzzle:
            self.body[x][y].locked = True
        self.body[x][y].value = value

    def clear_value(self, x, y):
        if self.create_puzzle:
            self.body[x][y].locked = False
            if self.body[x][y] != -1:
                self.count_empty += 1
            self.body[x][y].value = -1
        elif not self.body[x][y].locked:
            if self.body[x][y] != -1:
                self.count_empty += 1
            self.body[x][y].value = -1

    def start_puzzle(self):
        self.create_puzzle = False

    def check_end(self):
        reply = True
        if self.count_empty == 0:
            for x in range(len(self.body[0])):
                for y in range(len(self.body)):
                    visited = []
                    item_q = x, y
                    count = 0
                    query = [item_q]
                    visited.append(item_q)
                    while len(query) > 0:
                        item_c = query.pop(0)
                        count += 1
                        if item_c[0] == 0 and item_c[0] == len(self.body[0]) - 1:
                            pass
                        else:
                            if item_c[0] == 0:
                                if (visited.count((item_c[0] + 1, item_c[1])) == 0 and
                                        self.body[item_c[0] + 1][item_c[1]].value == self.body[item_q[0]][item_q[1]].value):
                                    query.append((item_c[0] + 1, item_c[1]))
                                    visited.append((item_c[0] + 1, item_c[1]))

                            if item_c[0] == len(self.body[0]) - 1:
                                if (visited.count((item_c[0] - 1, item_c[1])) == 0 and
                                        self.body[item_c[0] - 1][item_c[1]].value == self.body[item_q[0]][item_q[1]].value):
                                    query.append((item_c[0] - 1, item_c[1]))
                                    visited.append((item_c[0] - 1, item_c[1]))

                        if item_c[1] == 0 and item_c[1] == len(self.body) - 1:
                            pass
                        else:
                            if item_c[1] == 0:
                                if (visited.count((item_c[0], item_c[1] + 1)) == 0 and
                                        self.body[item_c[0]][item_c[1] + 1].value == self.body[item_q[0]][item_q[1]].value):
                                    query.append((item_c[0], item_c[1] + 1))
                                    visited.append((item_c[0], item_c[1] + 1))

                            if item_c[1] == len(self.body) - 1:
                                if (visited.count((item_c[0], item_c[1] - 1)) == 0 and
                                        self.body[item_c[0]][item_c[1] - 1].value == self.body[item_q[0]][item_q[1]].value):
                                    query.append((item_c[0], item_c[1] - 1))
                                    visited.append((item_c[0], item_c[1] - 1))

                        if 0 < item_c[0] < len(self.body[0]) - 1:
                            if (visited.count((item_c[0] + 1, item_c[1])) == 0 and
                                    self.body[item_c[0] + 1][item_c[1]].value == self.body[item_q[0]][item_q[1]].value):
                                query.append((item_c[0] + 1, item_c[1]))
                                visited.append((item_c[0] + 1, item_c[1]))

                            if (visited.count((item_c[0] - 1, item_c[1])) == 0 and
                                    self.body[item_c[0] - 1][item_c[1]].value == self.body[item_q[0]][item_q[1]].value):
                                query.append((item_c[0] - 1, item_c[1]))
                                visited.append((item_c[0] - 1, item_c[1]))

                        if 0 < item_c[1] < len(self.body) - 1:
                            if (visited.count((item_c[0], item_c[1] + 1)) == 0 and
                                    self.body[item_c[0]][item_c[1] + 1].value == self.body[item_q[0]][item_q[1]].value):
                                query.append((item_c[0], item_c[1] + 1))
                                visited.append((item_c[0], item_c[1] + 1))

                            if (visited.count((item_c[0], item_c[1] - 1)) == 0 and
                                    self.body[item_c[0]][item_c[1] - 1].value == self.body[item_q[0]][item_q[1]].value):
                                query.append((item_c[0], item_c[1] - 1))
                                visited.append((item_c[0], item_c[1] - 1))

                    if count != self.body[x][y].value:
                        reply = False
        print(reply, self.count_empty)
        if reply:
            self.end = True


