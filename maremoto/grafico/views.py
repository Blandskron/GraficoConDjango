import plotly.graph_objects as go
import numpy as np
from django.shortcuts import render

def visualizar_maremoto(request):
    # Datos del maremoto
    distancia = np.linspace(0, 100, 100)
    magnitud = np.linspace(7.0, 9.0, 100)
    x, y = np.meshgrid(distancia, magnitud)
    z = np.sin(np.sqrt(x**2 + y**2))

    # Crear la figura
    fig = go.Figure()
    fig.add_trace(go.Surface(z=z, x=x, y=y, colorscale='Viridis'))

    # Actualizar layout
    fig.update_layout(
        title='Visualización 3D de Datos de Maremoto',
        scene=dict(
            xaxis_title='Distancia (km)',
            yaxis_title='Magnitud de la Ola (Mw)',
            zaxis_title='Altura de la Ola (m)',
        )
    )

    # Convertir la figura a HTML
    html_graph = fig.to_html(full_html=False)

    return render(request, 'grafico/index.html', {'html_graph': html_graph})
