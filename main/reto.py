import os
import locale


def run(input_file_name=None):

    if input_file_name is None:
        return None

    locale.setlocale(locale.LC_ALL, 'es_EC.UTF8')
    file = leerFile(input_file_name, data_dir='input')

    buffer = ""

    while True:
        size_musicos = int(file.readline())
        if not size_musicos:
            break

        size = size_musicos

        if size > 100:
            return ''
        sumaGastos = 0
        lista = []

        while size > 0:
            gastos = locale.atof(file.readline().strip("$"))
            if gastos > 1000:
                return ''
            sumaGastos += gastos
            lista.append(gastos)
            size -= 1

        promedioGastos = precision_decimal(sumaGastos / size_musicos)
        acumulacion = 0

        for gasto in lista:
            diferencia = promedioGastos - gasto
            if diferencia > 0:
                acumulacion += diferencia

        moneda = round(acumulacion, 2)
        if moneda == 0:
            moneda = '${}'.format(moneda)
        else:
            moneda = locale.currency(moneda).replace('.', ',')

        buffer += moneda + '\n'


    buffer = buffer.strip()

    file.close()

    return buffer


def precision_decimal(promedioGastos):
    pgStr = ""
    derechaBool = False
    k = 0

    for d in str(promedioGastos):
        if derechaBool:
            k += 1

        if d == '.':
            derechaBool = True

        if k > 2:
            break
        pgStr += d

    return float(pgStr)


def outputData(output_file_name=None):
    output = leerFile(file_name=output_file_name, data_dir='output')
    data = ""

    while True:
        line = output.readline()
        if not line: # Si la linea esta [vacio] o es [0]
            break
        data +=line

    output.close()

    return data


def leerFile(file_name, data_dir=None):
    ruta = os.path.join(os.path.dirname(os.getcwd()), f"data/{data_dir}/{file_name}")
    return open(ruta, 'r')


# Testing Manual
def testing_manual():
    output = outputData(output_file_name='TestCase.txt')
    resultado = run(input_file_name='TestCase.txt')
    resultado2 = "$10,00\n" \
                "$11,99\n" \
                "$11,99\n" \
                "$0,07\n" \
                "$0"
    print("# Output Original")
    print('----------------------------------')
    print(output)
    print('----------------------------------')
    print("# Mi Output")
    print('----------------------------------')
    print(resultado)
    print('----------------------------------')
    status = output == resultado
    print(f"\nResultado Testing: {status}")


if __name__ == '__main__':
    testing_manual()
    # run(input_file_name='TestCase.txt')
