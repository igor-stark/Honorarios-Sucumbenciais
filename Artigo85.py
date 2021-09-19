class Artigo85:
    def __init__(self):
        # Porcentagem mín,máx e quantidade de salários mínimos do inciso 1:
        self.i1min = 0.1
        self.i1max = 0.2
        self.q1 = 200
        # Porcentagem mín,máx e quantidade de salários mínimos do inciso 2
        self.i2min = 0.08
        self.i2max = 0.1
        self.q2 = 2000
        # Porcentagem mín,máx e quantidade de salários mínimos do inciso 3
        self.i3min = 0.05
        self.i3max = 0.08
        self.q3 = 20000
        # Porcentagem mín,máx e quantidade de salários mínimos do inciso 4
        self.i4min = 0.03
        self.i4max = 0.05
        self.q4 = 100000
        # Porcentagem mín,máx e quantidade de salários mínimos do inciso 5
        self.i5min = 0.01
        self.i5max = 0.03

    def honorarios_min(self, salmin, vcondenacao):

        # Inciso 1
        if vcondenacao <= self.q1 * salmin:
            min = self.i1min * vcondenacao
            return "O valor mínimo a ser pago será:", min
        # Inciso 2
        if vcondenacao > self.q1 * salmin and vcondenacao <= self.q2 * salmin:
            min = self.i1min * self.q1 * salmin
            novo_vcondenacao = vcondenacao - self.q1 * salmin
            if novo_vcondenacao <= self.q1 * salmin:
                return "O valor mínimo a ser pago será:", min
            else:
                min2 = self.i2min * novo_vcondenacao
                return "O valor mínimo a ser pago será:", min + min2
        # Inciso 3
        if vcondenacao > self.q2 * salmin and vcondenacao <= self.q3 * salmin:
            min = self.i1min * self.q1 * salmin
            novo_vcondenacao = vcondenacao - self.q1 * salmin
            if novo_vcondenacao <= self.q1 * salmin:
                return "O valor mínimo a ser pago será:", min
            else:
                min2 = self.i2min * self.q2 * salmin
                novo_vcondenacao = novo_vcondenacao - self.q2 * salmin
                if novo_vcondenacao <= self.q2 * salmin:
                    return "O valor mínimo a ser pago será:", min + min2
                else:
                    min3 = self.i3min * novo_vcondenacao
                return "O valor mínimo a ser pago será:", min + min2 + min3
        # Inciso 4
        if vcondenacao > self.q3 * salmin and vcondenacao <= self.q4 * salmin:
            min = self.i1min * self.q1 * salmin
            novo_vcondenacao = vcondenacao - self.q1 * salmin
            if novo_vcondenacao <= self.q1 * salmin:
                return "O valor mínimo a ser pago será:", min
            else:
                min2 = self.i2min * self.q2 * salmin
                novo_vcondenacao = novo_vcondenacao - self.q2 * salmin
                if novo_vcondenacao <= self.q2 * salmin:
                    return "O valor mínimo a ser pago será:", min + min2
                else:
                    min3 = self.i3min * self.q3 * salmin
                    novo_vcondenacao = novo_vcondenacao - self.q3 * salmin
                    if novo_vcondenacao <= self.q3 * salmin:
                        return "O valor mínimo a ser pago será:", min + min2 + min3
                    else:
                        min4 = self.i4min * novo_vcondenacao
                        return (
                            "O valor mínimo a ser pago será:",
                            min + min2 + min3 + min4,
                        )
        # Inciso 5
        else:
            min = self.i1min * self.q1 * salmin
            novo_vcondenacao = vcondenacao - self.q1 * salmin
            if novo_vcondenacao <= self.q1 * salmin:
                return "O valor mínimo a ser pago será:", min
            else:
                min2 = self.i2min * self.q2 * salmin
                novo_vcondenacao = novo_vcondenacao - self.q2 * salmin
                if novo_vcondenacao <= self.q2 * salmin:
                    return "O valor mínimo a ser pago será:", min + min2
                else:
                    min3 = self.i3min * self.q3 * salmin
                    novo_vcondenacao = novo_vcondenacao - self.q3 * salmin
                    if novo_vcondenacao <= self.q3 * salmin:
                        return "O valor mínimo a ser pago será:", min + min2 + min3
                    else:
                        min4 = self.i4min * self.q4 * salmin
                        novo_vcondenacao = novo_vcondenacao - self.q4 * salmin
                        if novo_vcondenacao <= self.q4 * salmin:
                            return (
                                "O valor mínimo a ser pago será:",
                                min + min2 + min3 + min4,
                            )
                        else:
                            min5 = self.i5min * novo_vcondenacao
                            return (
                                "O valor mínimo a ser pago será:",
                                min + min2 + min3 + min4 + min5,
                            )

    def honorarios_max(self, salmin, vcondenacao):
        # Inciso 1
        if vcondenacao <= self.q1 * salmin:
            max = self.i1max * vcondenacao
            return "O valor máximo a ser pago será:", max
        # Inciso 2
        if vcondenacao > self.q1 * salmin and vcondenacao <= self.q2 * salmin:
            max = self.i1max * self.q1 * salmin
            novo_vcondenacao = vcondenacao - self.q1 * salmin
            if novo_vcondenacao <= self.q1 * salmin:
                return "O valor mínimo a ser pago será:", max
            else:
                max2 = self.i2max * novo_vcondenacao
                return "O valor máximo a ser pago será:", max + max2
        # Inciso 3
        if vcondenacao > self.q2 * salmin and vcondenacao <= self.q3 * salmin:
            max = self.i1max * self.q1 * salmin
            novo_vcondenacao = vcondenacao - self.q1 * salmin
            if novo_vcondenacao <= self.q1 * salmin:
                return "O valor máximo a ser pago será:", max
            else:
                max2 = self.i2max * self.q2 * salmin
                novo_vcondenacao = novo_vcondenacao - self.q2 * salmin
                if novo_vcondenacao <= self.q2 * salmin:
                    return "O valor máximo a ser pago será:", max + max2
                else:
                    max3 = self.i3max * novo_vcondenacao
                return "O valor máximo a ser pago será:", max + max2 + max3
        # Inciso 4
        if vcondenacao > self.q3 * salmin and vcondenacao <= self.q4 * salmin:
            max = self.i1max * self.q1 * salmin
            novo_vcondenacao = vcondenacao - self.q1 * salmin
            if novo_vcondenacao <= self.q1 * salmin:
                return "O valor máximo a ser pago será:", max
            else:
                max2 = self.i2max * self.q2 * salmin
                novo_vcondenacao = novo_vcondenacao - self.q2 * salmin
                if novo_vcondenacao <= self.q2 * salmin:
                    return "O valor máximo a ser pago será:", max + max2
                else:
                    max3 = self.i3max * self.q3 * salmin
                    novo_vcondenacao = novo_vcondenacao - self.q3 * salmin
                    if novo_vcondenacao <= self.q3 * salmin:
                        return "O valor máximo a ser pago será:", max + max2 + max3
                    else:
                        max4 = self.i4max * novo_vcondenacao
                        return (
                            "O valor máximo a ser pago será:",
                            max + max2 + max3 + max4,
                        )
        # Inciso 5
        else:
            max = self.i1max * self.q1 * salmin
            novo_vcondenacao = vcondenacao - self.q1 * salmin
            if novo_vcondenacao <= self.q1 * salmin:
                return "O valor máximo a ser pago será:", max
            else:
                max2 = self.i2max * self.q2 * salmin
                novo_vcondenacao = novo_vcondenacao - self.q2 * salmin
                if novo_vcondenacao <= self.q2 * salmin:
                    return "O valor máximo a ser pago será:", max + max2
                else:
                    max3 = self.i3max * self.q3 * salmin
                    novo_vcondenacao = novo_vcondenacao - self.q3 * salmin
                    if novo_vcondenacao <= self.q3 * salmin:
                        return "O valor máximo a ser pago será:", max + max2 + max3
                    else:
                        max4 = self.i4maxself.q4 * salmin
                        novo_vcondenacao = novo_vcondenacao - self.q4 * salmin
                        if novo_vcondenacao <= self.q4 * salmin:
                            return (
                                "O valor máximo a ser pago será:",
                                max + max2 + max3 + max4,
                            )
                        else:
                            min5 = self.i5min * novo_vcondenacao
                            return (
                                "O valor máximo a ser pago será:",
                                max + max2 + max3 + max4 + min5,
                            )
