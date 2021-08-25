def honorarios_min(salariom, vcondenacao):
    try:
        if vcondenacao <= 200*salariom:
            min = 0.1*vcondenacao
            return "O valor mínimo a ser pago será:", min
        if vcondenacao > 200*salariom and vcondenacao <= 2000*salariom:
            min = 0.1*200*salariom
            novo_vcondenacao = vcondenacao - 200*salariom
            if novo_vcondenacao <= 200*salariom:
                return "O valor mínimo a ser pago será:", min
            else:
                min2 = 0.08*novo_vcondenacao
                return "O valor mínimo a ser pago será:", min + min2
        if vcondenacao > 2000*salariom and vcondenacao <= 20000*salariom:
            min = 0.1*200*salariom
            novo_vcondenacao = vcondenacao - 200*salariom
            if novo_vcondenacao <= 200*salariom:
                return "O valor mínimo a ser pago será:", min
            else:
                min2 = 0.08*2000*salariom
                novo_vcondenacao = novo_vcondenacao - 2000*salariom
                if novo_vcondenacao <= 2000*salariom:
                    return "O valor mínimo a ser pago será:", min + min2
                else:
                    min3 = 0.05 * novo_vcondenacao
                return "O valor mínimo a ser pago será:", min + min2 + min3
        if vcondenacao > 20000*salariom and vcondenacao <= 100000*salariom:
            min = 0.1*200*salariom
            novo_vcondenacao = vcondenacao - 200*salariom
            if novo_vcondenacao <= 200*salariom:
                return "O valor mínimo a ser pago será:", min
            else:
                min2 = 0.08*2000*salariom
                novo_vcondenacao = novo_vcondenacao - 2000*salariom
                if novo_vcondenacao <= 2000*salariom:
                    return "O valor mínimo a ser pago será:", min + min2
                else:
                    min3 = 0.05*20000*salariom
                    novo_vcondenacao = novo_vcondenacao - 20000*salariom
                    if novo_vcondenacao <= 20000*salariom:
                        return "O valor mínimo a ser pago será:", min + \
                            min2 + min3
                    else:
                        min4 = 0.03*novo_vcondenacao
                        return "O valor mínimo a ser pago será:", min + \
                            min2 + min3 + min4
        else:
            min = 0.1*200*salariom
            novo_vcondenacao = vcondenacao - 200*salariom
            if novo_vcondenacao <= 200*salariom:
                return "O valor mínimo a ser pago será:", min
            else:
                min2 = 0.08*2000*salariom
                novo_vcondenacao = novo_vcondenacao - 2000*salariom
                if novo_vcondenacao <= 2000*salariom:
                    return "O valor mínimo a ser pago será:", min + min2
                else:
                    min3 = 0.05*20000*salariom
                    novo_vcondenacao = novo_vcondenacao - 20000*salariom
                    if novo_vcondenacao <= 20000*salariom:
                        return "O valor mínimo a ser pago será:", min + \
                            min2 + min3
                    else:
                        min4 = 0.03*100000*salariom
                        novo_vcondenacao = novo_vcondenacao - 100000*salariom
                        if novo_vcondenacao <= 100000*salariom:
                            return "O valor mínimo a ser pago será:", min + \
                                min2 + min3 + min4
                        else:
                            min5 = 0.01*novo_vcondenacao
                            return "O valor mínimo a ser pago será:", min + \
                                min2 + min3 + min4 + min5
    except TypeError:
        return """Somente números são aceitos e não esqueça de
              usar . no lugar de ,"""
    except SyntaxError:
        return """Somente números são aceitos e
              não esqueça de usar . no lugar de ,"""
    except ZeroDivisionError:
        return "Não divida por 0"
    except NameError:
        return """Somente números são aceitos e não esqueça de
              usar . no lugar de ,"""
    except Exception:
        return """Somente números são aceitos e não esqueça de
              usar . no lugar de ,"""


def honorarios_max(salariom, vcondenacao):
    try:
        if vcondenacao <= 200*salariom:
            max = 0.2*vcondenacao
            return "O valor máximo a ser pago será:", max
        if vcondenacao > 200*salariom and vcondenacao <= 2000*salariom:
            max = 0.2*200*salariom
            novo_vcondenacao = vcondenacao - 200*salariom
            if novo_vcondenacao <= 200*salariom:
                return "O valor máximo a ser pago será:", max
            else:
                max2 = 0.1*novo_vcondenacao
                return "O valor máximo a ser pago será:", max + max2
        if vcondenacao > 2000*salariom and vcondenacao <= 20000*salariom:
            max = 0.2*200*salariom
            novo_vcondenacao = vcondenacao - 200*salariom
            if novo_vcondenacao <= 200*salariom:
                return "O valor máximo a ser pago será:", max
            else:
                max2 = 0.1*2000*salariom
                novo_vcondenacao = novo_vcondenacao - 2000*salariom
                if novo_vcondenacao <= 2000*salariom:
                    return "O valor máximo a ser pago será:", max + max2
                else:
                    max3 = 0.08 * novo_vcondenacao
                return "O valor máximo a ser pago será:", max + max2 + max3
        if vcondenacao > 20000*salariom and vcondenacao <= 100000*salariom:
            max = 0.2*200*salariom
            novo_vcondenacao = vcondenacao - 200*salariom
            if novo_vcondenacao <= 200*salariom:
                return "O valor máximo a ser pago será:", max
            else:
                max2 = 0.1*2000*salariom
                novo_vcondenacao = novo_vcondenacao - 2000*salariom
                if novo_vcondenacao <= 2000*salariom:
                    return "O valor máximo a ser pago será:", max + max2
                else:
                    max3 = 0.08*20000*salariom
                    novo_vcondenacao = novo_vcondenacao - 20000*salariom
                    if novo_vcondenacao <= 20000*salariom:
                        return "O valor mínimo a ser pago será:", max + \
                            max2 + max3
                    else:
                        max4 = 0.05*novo_vcondenacao
                        return "O valor mínimo a ser pago será:", max + \
                            max2 + max3 + max4
        else:
            max = 0.2*200*salariom
            novo_vcondenacao = vcondenacao - 200*salariom
            if novo_vcondenacao <= 200*salariom:
                return "O valor máximo a ser pago será:", max
            else:
                max2 = 0.1*2000*salariom
                novo_vcondenacao = novo_vcondenacao - 2000*salariom
                if novo_vcondenacao <= 2000*salariom:
                    return "O valor máximo a ser pago será:", max + max2
                else:
                    max3 = 0.08*20000*salariom
                    novo_vcondenacao = novo_vcondenacao - 20000*salariom
                    if novo_vcondenacao <= 20000*salariom:
                        return "O valor máximo a ser pago será:", max + \
                            max2 + max3
                    else:
                        max4 = 0.05*100000*salariom
                        novo_vcondenacao = novo_vcondenacao - 100000*salariom
                        if novo_vcondenacao <= 100000*salariom:
                            return "O valor máximo a ser pago será:", max + \
                                max2 + max3 + max4
                        else:
                            max5 = 0.03*novo_vcondenacao
                            return "O valor máximo a ser pago será:", max + \
                                max2 + max3 + max4 + max5

    except TypeError:
        return """Somente números são aceitos e não esqueça de
              usar . no lugar de ,"""
    except SyntaxError:
        return """Somente números são aceitos e
              não esqueça de usar . no lugar de ,"""
    except ZeroDivisionError:
        return "Não divida por 0"
    except NameError:
        return """Somente números são aceitos e não esqueça de
              usar . no lugar de ,"""
    except Exception:
        return """Somente números são aceitos e não esqueça de
              usar . no lugar de ,"""
