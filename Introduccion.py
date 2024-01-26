import streamlit as st
import pandas as pd
import altair as alt
from streamlit_dynamic_filters import DynamicFilters

st.set_page_config(
    page_title="Evaluación de vías de reducción de emisiones",
)

st.write("## Evaluación de vías de reducción de emisiones: Sectores UTCUTS y Agricultura")

#st.sidebar.success("Seleccione un sector")
#st.sidebar.write("Desarrollado por")
st.sidebar.image("SSG logo with wordmark medium blue.png", use_column_width=True)

col1, col2 = st.sidebar.columns(2)

# Cargar y mostrar la primera imagen en la primera columna
col1.image("bid-logo-300x160.png",width=100)

# Cargar y mostrar la segunda imagen en la segunda columna
col2.image("logo-ODEPA-TWITTER.jpg",width=90)

st.subheader('Contexto')

st.markdown(
    """
    Chile se ha comprometido a enfrentar el cambio climático con una mirada de largo plazo a través de la Ley Marco de Cambio Climático, definiendo como objetivo alcanzar la carbono-neutralidad a más tardar al año 2050. Para esto, además existen metas y objetivos que ayudan a orientar los esfuerzos de mitigación. Por ejemplo, la Estrategia Climática de Largo Plazo (ECLP) establece emisiones máximas de gases de efecto invernadero (GEI), o presupuestos de carbono, para el período 2020-2030 para los sectores emisores y objetivos de captura de carbono para el sector de uso de la tierra, cambio de uso de la tierra y silvicultura (UTCUTS).
El cumplimiento de metas de largo plazo involucra desafíos respecto de la incertidumbre que conlleva un horizonte tan amplio, sujeto a condiciones que son cambiantes y que afectan los resultados esperados. Además, los sectores que emiten o capturan emisiones tienen características específicas que son relevantes de considerar al momento de evaluar medidas de mitigación y su impacto.
Este estudio se enfoca en los sectores agricultura y UTCUTS. Tiene como objetivo realizar una evaluación, considerando incertidumbre y la participación de actores relevantes, de las opciones de reducción de emisiones en ambos sectores en Chile. Incluye además los costos y beneficios asociados a la implementación de estrategias de mitigación. El análisis busca ayudar a robustecer la estrategia de mitigación del sector de agricultura y UTCUTS.


"""
)

st.markdown('##### Para los escenarios de emisiones se consideraron las siguientes medidas para cada sector:')

col1,col2=st.columns(2)
with col1:
    st.markdown(
        """
        ###### Sector Uso de Suelos:
        + Forestación
        + Aumento de superficie de bosque nativo bajo planes de manejo
        + Creación de nuevas áreas silvestres protegidas
        + Reducción de la superficie de incendios forestales
        + Reducción de la sustitución de bosque nativo por plantaciones forestales
        + Reducción de la extracción de leña
        + Restauración y recuperación de bosque nativo
        """
        )
with col2:
    st.image('parque-huerquehue-la-araucania.jpg',width=230)

col1,col2=st.columns(2)
with col1:
    st.image('agricultura-chile-1.jpg',width=330)
with col2:
    st.markdown(
        """
        ###### Sector Agricultura:
        + Biodigestores para tratamiento de purines porcinos y bovinos
        + Aditivo reductor de metano para bovinos
        + Uso eficiente de fertilizantes nitrogenados
        + Arroz reducido en metano
        + Reducción de quemas agrícolas
        """
        )


st.markdown(
    """
#### Para explorar los resultados por sector, ingrese al menú de la izquierda 👈

"""
)

# st.title("AFOLU")
# bau = pd.read_excel('C:\\Users\\lunam\\Desktop\\Streamlit_afolu\\tableau_p3.xlsx', sheet_name='bau')
# foresta=pd.read_excel('C:\\Users\\lunam\\Desktop\\Streamlit_afolu\\tableau_p3.xlsx', sheet_name='forestacion')
# manejo=pd.read_excel('C:\\Users\\lunam\\Desktop\\Streamlit_afolu\\tableau_p3.xlsx', sheet_name='manejo')

# chart = alt.Chart(bau).mark_line().encode(
#     x='tiempo:O',
#     y='bau:Q',
#     detail='id_futuro:N',
#     #color='grey'  
# ).properties(
#     width=400,  
# )

# chart = chart.configure_legend(
#     title=None,       
#     labelFontSize=0,  
#     symbolSize=0,     
# )


# st.altair_chart(chart, use_container_width=True)



# dynamic_filters = DynamicFilters(bau, filters=['tiempo', 'id_futuro'])

# with st.sidebar:
#     dynamic_filters.display_filters()

# datab= dynamic_filters.display_df()

# # Verificar si los filtros están activos
# if datab is not None:
#     # Crear el gráfico de líneas con Altair usando el DataFrame filtrado
#     chart = alt.Chart(datab.filter_df).mark_line().encode(
#         x='tiempo:O',
#         y='valor:Q',
#         color='id_futuro:N',
#     )

#     # Mostrar el gráfico en Streamlit
#     st.altair_chart(chart, use_container_width=True)
# else:
#     st.warning("No hay datos filtrados. Ajusta los filtros para ver datos.")