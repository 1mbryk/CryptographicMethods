import json


class RSA:
    def __init__(self, path_to_json: str):
        self.path_to_json = path_to_json
        self.p = 0
        self.q = 0
        self.e = 0
        self.d = 0
        self.X = 0
        self.Y = 0

    def __call__(self, operaion: str):
        """
        Doing generation, encryption, decryption

        Parameters:
            - operation = [Gen, Encr, Decr, Exit]

        """
        f = open(self.path_to_json)
        readed_json = f.read()
        f.close()
        match operaion:
            case "Gen":
                params = json.loads(readed_json)['Gen']
                self.p = params['p']
                self.q = params['q']
                self.e = params['e']
                self.__generate()

            case "Encr":
                params = json.loads(readed_json)['Encr']
                self.X = params['X']
                self.e = params['e']
                self.n = params['n']
                self.Y = self.__fast_power(self.X, self.e, self.n)
                print(f"encrypted message: {self.Y}")
            case "Decr":
                params = json.loads(readed_json)['Decr']
                self.Y = params['Y']
                self.e = params['e']
                self.n = params['n']
                self.decr_Y = self.__fast_power(self.Y, self.d, self.n)
                print(f"decrypted message: {self.decr_Y}")
            case "Exit":
                exit()
            case _:
                pass

    def __EEA(self, a: int, b: int):
        """
        Extend Euclid Algorithm 

        x = a^-1(mod b)

        Parameters:
            - a
            - b

        Returns:
            - x
            - y
        """

        r_prev = a
        r_curr = b

        x_prev = 1
        x_curr = 0

        y_prev = 0
        y_curr = 1

        def next_step(prev, curr, q):
            temp = prev - q * curr
            prev = curr
            curr = temp
            return (prev, curr)

        while r_curr != 0:
            q = r_prev // r_curr
            r_prev, r_curr = next_step(r_prev, r_curr, q)
            x_prev, x_curr = next_step(x_prev, x_curr, q)
            y_prev, y_curr = next_step(y_prev, y_curr, q)

        return x_prev, y_prev

    def __generate(self):
        self.n = self.p * self.q
        phi = (self.p - 1)*(self.q - 1)
        self.d, _ = self.__EEA(self.e, phi)

    def __fast_power(self, num, pow, mod):
        u = 1
        v = num
        while pow >= 1:
            bit = pow & 1
            if bit != 0:
                u = (u * v) % mod
            v = (v * v) % mod
            pow >>= 1
        return u

    def x__read_json(self, json_doc, pars):
        """
        Parameters:

            opt: ['Gen', 'Encr', 'Decr']

            pars: ['p', 'q', 'e'] or ['X','e','n'] or ['Y','e','n']

        Yeilds:

            turple of pars

        """
        for item in json_doc:
            yield (item[pars[0]], item[pars[1]], item[pars[2]])


if __name__ == '__main__':
    a = RSA('lab3/data.json')
    f = open('lab3/data.json')
    readed_json = f.read()
    f.close()
    aboba = json.loads(readed_json)
    while True:
        b = input()
        match b:
            case "Gen":
                pars = ['p', 'q', 'e']
            case "Encr":
                pars = ['X', 'e', 'n']
            case "Decr":
                pars = ['Y', 'e', 'n']
        x = a.x__read_json(aboba[b], pars)
        # print(f"{x}\n{y}\n{z}")
