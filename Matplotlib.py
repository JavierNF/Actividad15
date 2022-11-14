
import pandas as pd
import matplotlib.pyplot as plt

def cargar_archivo():
    datos = pd.read_csv("C:\\Users\\Tecnicos\\Desktop\\Campus\\programacion\\Programacion\\proyectos\\excel\\casasboston.csv")
    # datos = datos[["RM","CRIM", "MEDV", "TOWN", "CHAS", "INDUS", "LSTAT"]]
    df = datos[["RM", "CRIM", "MEDV", "TOWN", "CHAS"]]

    df = datos.rename(columns={
        "TOWN": "CIUDAD",
        "CRIM": "INDICE_CRIMEN",
        "INDUS": "PCT_ZONA_INDUSTRIAL",
        "CHAS": "RIO_CHARLES",
        "RM": "N_HABITACIONES_MEDIO",
        "MEDV": "VALOR_MEDIANO",
        "LSTAT": "PCT_CLASE_BAJA"
    })

    #print(df.sample(5))



    #grafico circular
    df.RIO_CHARLES.value_counts().plot.pie()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     #print_hi('PyCharm')
     cargar_archivo()