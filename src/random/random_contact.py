import random

class RandomContact:
    input_data = None

    def prefix(self, num):
        prefixes = [
            '071',
            '072',
            '073',
            '077'
        ]

        index = random.randrange(0, len(prefixes))
        out = prefixes[index] + str(num)
        return int(out)

    def random(self):
        random_contact = random.randrange(99999999)
        random_contact = self.prefix(random_contact)

        # return id
        return random_contact