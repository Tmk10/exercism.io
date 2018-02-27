from itertools import cycle


def fence_pattern(rails, message_size):
    cycle_len = 2 * (rails - 1)
    fence = (min(x, cycle_len - x) for x in cycle(range(cycle_len)))
    return sorted(zip(fence, range(message_size)))


def encode(message,rails):
    pattern = fence_pattern(rails, len(message))
    encoded_msg = [message[i] for y, i in pattern]
    return "".join(encoded_msg)


def decode(encoded_message,rails):
    pattern = fence_pattern(rails, len(encoded_message))
    decoded_msg = sorted(enumerate(pattern), key=lambda key: key[1][1])
    return "".join(encoded_message[i] for i, y in decoded_msg)
