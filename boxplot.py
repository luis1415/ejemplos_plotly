import plotly as py
import numpy as np
import pandas as pd


def box_plotly(file_name, cols):
    """
    Esta funcion saca un boxplot de algunas variables de un dataframe
    :param file_name: el dataframe con la informacion para el boxplot
    :param cols: las columnas que se quieren graficar
    :return: no devuelve nada, pero genera un archivo temporal html con la grafica.
    """

    df = pd.read_csv(file_name, dtype=object)

    colors = ['hsl(' + str(h) + ',50%' + ',50%)' for h in np.linspace(0, 360, len(cols))]

    data = [{
        'y': df[cols[i]].values,
        'name': cols[i],
        'type': 'box',
        'marker': {'color': colors[i]}
    } for i in range(int(len(cols)))]

    # format the layout
    layout = {'xaxis': {'showgrid': True, 'zeroline': False, 'tickangle': 60, 'showticklabels': True},
              'yaxis': {'showgrid': True, 'zeroline': False},
              'paper_bgcolor': 'rgb(233,233,233)',
              'plot_bgcolor': 'rgb(233,233,233)',
              }

    py.offline.plot(data, layout)


if __name__ == '__main__':
    numericas_1 = ['CSMO_REACT', 'CSMO_FACT_PUNTA',
                   'CSMO_FACT_VALLE', 'CSMO_FACT_LLANO', 'CSMO_FACT_AVALLE', 'CSMO_REACT_PUNTA',
                   'CSMO_REACT_VALLE', 'CSMO_REACT_AVALLE', 'CSMO_FACT_PPUNTA', 'CSMO_ACTIVA_ZE',
                   'CSMO_PUNTA_ZE', 'CSMO_VALLE_ZE']

    numericas_2 = ['CSMO_FACT_HORA6', 'CSMO_FACT_HORA7', 'CSMO_REACT_LLANO', 'CSMO_REACT_PPUNTA',
                   'CSMO_REACT_HORA6', 'CSMO_REACT_HORA7', 'CSMO_AVALLE_ZE', 'CSMO_PPUNTA_ZE',
                   'CSMO_HORA6_ZE', 'CSMO_HORA7_ZE']

    box_plotly('facturacion_consolidado.csv', numericas_1)
