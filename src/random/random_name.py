import random

class RandomName:
    input_data = None

    def __init__(self, input_data):
        self.input_data = input_data

    def generate(self):
        # generated details
        generated =  []

        # loop through details
        for details in self.input_data:
            generated.append(details['name'])

        # return generated details
        return generated


    def random(self):
        # generate random members
        generated = self.generate()
        index_1 = random.randrange(len(generated))
        index_2 = random.randrange(len(generated))

       # return names
        return {
            'first': generated[index_1].split()[0].upper(),
            'last': generated[index_2].split()[1].upper()
        }

        