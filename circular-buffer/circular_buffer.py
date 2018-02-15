class BufferFullException(Exception):
    def __init__(self, message=""):
        self.message = message


class BufferEmptyException(Exception):
    def __init__(self, message=""):
        self.message = message


class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [[] for _ in range(capacity)]
        self.pointer = -1

    def write(self, value):
        if self.capacity + self.pointer < 0:
            raise BufferFullException("Buffer is full")
        self.buffer[self.pointer] = value
        self.pointer -= 1

    def read(self):
        if self.pointer == -1:
            raise BufferEmptyException("Buffer is empty")
        self.buffer.insert(0, [])
        self.pointer += 1
        return self.buffer.pop()

    def overwrite(self, value):
        if abs(self.pointer) > self.capacity:
            self.buffer.pop()
            self.buffer.insert(0, value)
        else:
            self.buffer[self.pointer] = value
            self.pointer -= 1

    def clear(self):
        for index in range(len(self.buffer)):
            self.buffer[index] = None
        self.pointer = -1
