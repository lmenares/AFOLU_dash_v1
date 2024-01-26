import streamlit as st
import pandas as pd
import altair as alt
#from streamlit_dynamic_filters import DynamicFilters
#import numpy_financial as npf


st.title("Uso de Suelos 🌱")

st.markdown('''
            El sector Uso de suelos es reportado en el inventario nacional 
            de gases de efecto invernadero como "Uso de la Tierra, Cambio de Uso de 
            la Tierra y Silvicultura" (UTCUTS). Este sector considera los siguientes subsectores:
            + Tierras Forestales
            + Tierras de cultivo
            + Pastizales
            + Humedales
            + Asentamientos
            + Otras tierras
            + Productos de madera recolectada

            El sector UTCUTS reviste gran importancia para el país, ya que es el único sector
            que presenta emisiones netas negativas (capturas) la mayoría de los años,
            por lo que actúa como sumidero de carbono.  
            Dentro del sector, el subsector más importante lo constituyen las Tierras forestales,
            con un 81,5 de las emisiones absolutas del sector en el año 2020, por lo 
            que las medidas en este análisis se centran en este uso de la tierra 
            '''
            )
st.write('''
            ##### :violet[***Para comenzar a explorar las emisiones del sector, seleccione el nivel de implementación de cada medida en las barras de la izquierda***]''')


#st.markdown('A continuación se muestran los resultados segun los siguientes niveles seleccionados para cada medida:')
bau = pd.read_csv('bau_c.csv')
referencia =pd.read_csv('referencia_b.csv')
foresta=pd.read_csv('forestacion.csv')
manejo=pd.read_csv('manejo.csv')
areas=pd.read_csv('areas.csv')
incendios=pd.read_csv('incendios.csv')
lena=pd.read_csv('lena.csv')
sustitucion= pd.read_csv('sustitucion.csv')
restauracion = pd.read_csv('restauracion.csv')

#bau = pd.read_excel('C:\\Users\\lunam\\Desktop\\Streamlit_afolu\\bd_streamlit.xlsx', sheet_name='bau')
#referencia = pd.read_excel('C:\\Users\\lunam\\Desktop\\Streamlit_afolu\\bd_streamlit.xlsx', sheet_name='referencia')
#foresta=pd.read_excel('C:\\Users\\lunam\\Desktop\\Streamlit_afolu\\bd_streamlit.xlsx', sheet_name='forestacion')
#manejo=pd.read_excel('C:\\Users\\lunam\\Desktop\\Streamlit_afolu\\bd_streamlit.xlsx', sheet_name='manejo')
#areas=pd.read_excel('C:\\Users\\lunam\\Desktop\\Streamlit_afolu\\bd_streamlit.xlsx', sheet_name='areas')
#incendios=pd.read_excel('C:\\Users\\lunam\\Desktop\\Streamlit_afolu\\bd_streamlit.xlsx', sheet_name='incendios')
#lena=pd.read_excel('C:\\Users\\lunam\\Desktop\\Streamlit_afolu\\bd_streamlit.xlsx', sheet_name='lena')
#sustitucion=pd.read_excel('C:\\Users\\lunam\\Desktop\\Streamlit_afolu\\bd_streamlit.xlsx', sheet_name='sustitucion')
#restauracion=pd.read_excel('C:\\Users\\lunam\\Desktop\\Streamlit_afolu\\bd_streamlit.xlsx', sheet_name='restauracion')


futuros= list(bau['id_futuro'].unique())

imp_forest = st.sidebar.select_slider(
    'Nivel de implementación de Forestación',
    options=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
st.write('Forestación:',imp_forest*100,'%', 'de implementacion de la medida')

imp_manejo = st.sidebar.select_slider(
    'Nivel de implementación de Planes de manejo',
    options=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
st.write('Planes de Manejo:', imp_manejo*100,'%', 'de implementacion de la medida')

imp_areas = st.sidebar.select_slider(
    'Nivel de implementación de Áreas protegidas',
    options=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
st.write('Áreas protegidas:', imp_areas*100,'%', 'de implementacion de la medida')

imp_incendios = st.sidebar.select_slider(
    'Nivel de implementación de Reducción de incendios',
    options=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
st.write('Reducción de incendios:', imp_incendios*100,'%', 'de implementacion de la medida')

imp_sustitucion = st.sidebar.select_slider(
    'Nivel de implementación de Reducción de sustitución',
    options=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
st.write('Reducción de sustitución:', imp_sustitucion*100,'%', 'de implementacion de la medida')

imp_lena = st.sidebar.select_slider(
    'Nivel de implementación de Reducción de extracción de leña',
    options=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
st.write('Reducción de extracción de leña:', imp_lena*100,'%', 'de implementacion de la medida')

imp_restauracion = st.sidebar.select_slider(
    'Nivel de implementación de Restauración y recuperación de bosque nativo',
    options=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
st.write('Restauración y recuperación de bosque nativo:', imp_restauracion*100,'%', 'de implementacion de la medida')

#st.sidebar.write("Desarrollado por")
st.sidebar.image("SSG logo with wordmark medium blue.png", use_column_width=True)

col1, col2 = st.sidebar.columns(2)

col1.image("bid-logo-300x160.png", width=100)

col2.image("logo-ODEPA-TWITTER.jpg", width=90)

mit_forest=foresta[foresta['i_forestacion']==imp_forest]
mit_manejo=manejo[manejo['i_manejo']==imp_manejo]
mit_areas=areas[areas['i_areas']==imp_areas]
mit_incendios=incendios[incendios['i_incendios']==imp_incendios]
mit_sustitucion=sustitucion[sustitucion['i_sustitucion']==imp_sustitucion]
mit_lena=lena[lena['i_lena']==imp_lena]
mit_restauracion=restauracion[restauracion['i_restauracion']==imp_restauracion]

medidas=pd.merge(mit_forest,mit_manejo,on='tiempo')
medidas=pd.merge(medidas,mit_areas, on='tiempo')
medidas=pd.merge(medidas,mit_incendios, on='tiempo')
medidas=pd.merge(medidas,mit_sustitucion, on='tiempo')
medidas=pd.merge(medidas,mit_lena, on='tiempo')
medidas=pd.merge(medidas,mit_restauracion, on='tiempo')

df_mit=pd.merge(bau,medidas,on='tiempo')
df_mit['emis_mit']=df_mit['Em_Mt']-df_mit['m_forestacion']-df_mit['m_manejo']-df_mit['m_areas']-df_mit['m_incendios']-df_mit['m_sustitucion']-df_mit['m_lena']-df_mit['m_restauracion']

medidas['mit_total']=medidas['m_forestacion']+medidas['m_manejo']+medidas['m_areas']+medidas['m_incendios']+medidas['m_sustitucion']+medidas['m_lena']+medidas['m_restauracion']
referencia_mit = medidas[['tiempo','mit_total']]
referencia_mit=pd.merge(referencia_mit,referencia, on='tiempo')
referencia_mit['Em_Mt']=referencia_mit['Em_Mt']-referencia_mit['mit_total']
referencia_mit['escenario']='Esc. Mitigación'
referencia_mit=referencia_mit.drop(columns=['mit_total'])

df_referencia=pd.concat([referencia,referencia_mit],axis=0)

chart_bau = alt.Chart(bau).mark_line().encode(
    x=alt.X('tiempo:O',title='Año'),
    y=alt.Y('Em_Mt:Q',title='Emisiones (Mt CO2eq)'),
    detail='id_futuro:N',
).properties(
    width=400,
).configure_mark(color='gray')

chart_bau = chart_bau.configure_legend(
    title=None,
    labelFontSize=0,
    symbolSize=0,
)


chart_mit = alt.Chart(df_mit).mark_line().encode(
    x=alt.X('tiempo:O',title='Año'),
    y=alt.Y('emis_mit:Q',title='Emisiones (Mt CO2eq)'),
    detail='id_futuro:N',
).properties(
    width=400,
).configure_mark(color='teal')

chart_mit = chart_mit.configure_legend(
    title=None,
    labelFontSize=0,
    symbolSize=0,
)

chart_referencia = alt.Chart(df_referencia).mark_line().encode(
    x=alt.X('tiempo:O',title='Año'),
    y=alt.Y('Em_Mt:Q',title='Emisiones (Mt CO2eq)'),
    color=alt.Color('escenario:N', title='Escenario', scale=alt.Scale(domain=['Línea Base', 'Esc. Mitigación'], range=['gray', 'teal']))
).properties(
    width=400
)

st.subheader('Emisiones')
tab1, tab2, tab3= st.tabs(["Línea Base","Escenario Mitigación", "Futuro referencia"])

with tab1:
   st.altair_chart(chart_bau, use_container_width=True)

with tab2:
   st.altair_chart(chart_mit, use_container_width=True)

with tab3:
    st.altair_chart(chart_referencia, use_container_width=True)


option = st.selectbox(
    'Seleccione si desea información sobre multiples futuros o sobre el futuro de referencia',
    ('Múltiples futuros', 'Futuro de referencia'))

st.write(option)

emis_bau_2050=bau[bau['tiempo']==2050]
emis_bau_2050['Escenario']='Línea Base'
emis_mit = df_mit[['tiempo','id_futuro','emis_mit']]
emis_mit= emis_mit.rename(columns={'emis_mit':'Em_Mt'})
emis_mit_2050=emis_mit[emis_mit['tiempo']==2050]
emis_mit_2050['Escenario']='Esc. Mitigación'

exito_bau = (emis_bau_2050['Em_Mt'] < -73).sum()
exito_mit = (emis_mit_2050['Em_Mt'] < -73).sum()
fracaso_bau = (emis_bau_2050['Em_Mt'] > -73).sum()
fracaso_mit = (emis_mit_2050['Em_Mt'] > -73).sum()

df_boxplot= pd.concat([emis_bau_2050,emis_mit_2050],axis=0)

boxplot = alt.Chart(df_boxplot).mark_boxplot(size=50).encode(
    x=alt.X('Escenario:N', title='Escenario', axis=alt.Axis(labelAngle=0, labelAlign='center')),
    y=alt.Y('Em_Mt:Q', title='Emisiones (MtCO2eq)'),
    color=alt.Color('Escenario:N', scale=alt.Scale(domain=['Línea Base', 'Esc. Mitigación'], range=['gray', 'teal']), legend=None)
).properties(
    title=alt.TitleParams(text='Comparación emisiones 2050')
).configure(background='rgba(169,169,169,0.3)')

boxplot = boxplot.configure_title(fontSize=15, offset=5, orient='top', anchor='middle')

torta_bau = {'Casos': ['Éxito', 'Fracaso'], 'Cantidad': [exito_bau,fracaso_bau]}
df_torta_bau = pd.DataFrame(torta_bau)

torta_mit = {'Casos': ['Éxito', 'Fracaso'], 'Cantidad': [exito_mit,fracaso_mit]}
df_torta_mit = pd.DataFrame(torta_mit)

chart_torta_bau = alt.Chart(df_torta_bau).mark_arc().encode(
    theta='Cantidad',
    color='Casos'
).properties(title='Línea Base',
    width=200,
    height=163
).configure(background='rgba(169,169,169,0.3)')

chart_torta_mit = alt.Chart(df_torta_mit).mark_arc().encode(
    theta='Cantidad',
    color='Casos'
).properties(title='Esc. Mitigación',
    width=200,
    height=163
).configure(background='rgba(169,169,169,0.3)')


if option == 'Múltiples futuros':
    col1, col2 = st.columns(2)
    with col1:
        st.altair_chart(boxplot, use_container_width=True)

    with col2:
        st.altair_chart(chart_torta_bau, use_container_width=True)
        st.altair_chart(chart_torta_mit, use_container_width=True)
else:
    st.dataframe(
        df_referencia,
        column_config={
            'tiempo':st.column_config.NumberColumn(
                'Año',
                format='%g'
            ),
            'Em_Mt': st.column_config.NumberColumn(
                'Emisiones (MtCO2eq)',
                help='Emisiones totales del sector, números negativos indican capturas',
                format='%.2f'
            ),
            'escenario':'Escenario'
        },
        hide_index=True,
    )


mit_forest_b=mit_forest.rename(columns={'m_forestacion':'mitigacion'}).drop(columns=['i_forestacion','c_forestacion'])
mit_forest_b['medida']='Forestación'

mit_manejo_b=mit_manejo.rename(columns={'m_manejo':'mitigacion'}).drop(columns=['i_manejo','c_manejo'])
mit_manejo_b['medida']='Manejo de BN'

mit_areas_b=mit_areas.rename(columns={'m_areas':'mitigacion'}).drop(columns=['i_areas','c_areas'])
mit_areas_b['medida']='Áreas protegidas'

mit_incendios_b=mit_incendios.rename(columns={'m_incendios':'mitigacion'}).drop(columns=['i_incendios','c_incendios'])
mit_incendios_b['medida']='Red. incendios'

mit_sustitucion_b=mit_sustitucion.rename(columns={'m_sustitucion':'mitigacion'}).drop(columns=['i_sustitucion','c_sustitucion'])
mit_sustitucion_b['medida']='Red. sustitución'

mit_restauracion_b=mit_restauracion.rename(columns={'m_restauracion':'mitigacion'}).drop(columns=['i_restauracion','c_restauracion'])
mit_restauracion_b['medida']='Restauracion de BN'

mit_lena_b=mit_lena.rename(columns={'m_lena':'mitigacion'}).drop(columns=['i_lena','c_lena'])
mit_lena_b['medida']='Red. uso de leña'

df_medidas=pd.concat([mit_forest_b,mit_manejo_b,mit_areas_b,mit_incendios_b,mit_lena_b,mit_sustitucion_b,mit_restauracion_b],axis=0)
df_medidas=df_medidas[df_medidas['tiempo']>2020]

chart_mit_total = (
    (
        alt.Chart(df_medidas).mark_bar().encode(
           alt.X('sum(mitigacion):Q', title='Mitigación acumulada (MtCO2eq)'),
           alt.Y('medida:N', title='Medidas'),
           alt.Color('medida:N', legend=None),
        )
    )
    .properties(title="Mitigación por medida")
)

chart_mit_anual= (
     (
         alt.Chart(df_medidas).mark_bar().encode(
            alt.X('tiempo:O', title='Año'),
            alt.Y('mitigacion:Q', title='Mitigación anual (MtCO2eq)'),
            alt.Color('medida:N', title='Medidas'),
         )
     )
)

st.subheader('Acciones de mitigación')
st.altair_chart(chart_mit_total,use_container_width=True)

st.altair_chart(chart_mit_anual,use_container_width=True)

#costos

costo_forestacion=mit_forest.rename(columns={'c_forestacion':'costo'}).drop(columns=['i_forestacion','m_forestacion'])
costo_forestacion['medida']='Forestación'
costo_forestacion=costo_forestacion[costo_forestacion['tiempo']>2023]

costo_manejo=mit_manejo.rename(columns={'c_manejo':'costo'}).drop(columns=['i_manejo','m_manejo'])
costo_manejo['medida']='Manejo de BN'
costo_manejo=costo_manejo[costo_manejo['tiempo']>2023]

costo_areas=mit_areas.rename(columns={'c_areas':'costo'}).drop(columns=['i_areas','m_areas'])
costo_areas['medida']='Áreas protegidas'
costo_areas=costo_areas[costo_areas['tiempo']>2023]

costo_incendios=mit_incendios.rename(columns={'c_incendios':'costo'}).drop(columns=['i_incendios','m_incendios'])
costo_incendios['medida']='Red. incendios'
costo_incendios=costo_incendios[costo_incendios['tiempo']>2023]

costo_sustitucion=mit_sustitucion.rename(columns={'c_sustitucion':'costo'}).drop(columns=['i_sustitucion','m_sustitucion'])
costo_sustitucion['medida']='Red. sustitución'
costo_sustitucion=costo_sustitucion[costo_sustitucion['tiempo']>2023]

costo_restauracion=mit_restauracion.rename(columns={'c_restauracion':'costo'}).drop(columns=['i_restauracion','m_restauracion'])
costo_restauracion['medida']='Restauración BN'
costo_restauracion=costo_restauracion[costo_restauracion['tiempo']>2023]

costo_lena=mit_lena.rename(columns={'c_lena':'costo'}).drop(columns=['i_lena','m_lena'])
costo_lena['medida']='Red. uso de leña'
costo_lena=costo_lena[costo_lena['tiempo']>2023]

df_costos=pd.concat([costo_areas,costo_forestacion,costo_incendios,costo_lena,costo_manejo,costo_restauracion,costo_sustitucion],axis=0)
#df_costos=df_costos[df_costos['tiempo']>2023]


#vpn_forestacion=npf.npv(0.06,costo_forestacion['costo'])
vpn_forestacion = sum(cf / (1 + 0.06)**i for i, cf in enumerate(costo_forestacion['costo']))
cma_forestacion=vpn_forestacion/((mit_forest_b['mitigacion']).sum())

vpn_manejo=sum(cf / (1 + 0.06)**i for i, cf in enumerate(costo_manejo['costo']))
cma_manejo=vpn_manejo/((mit_manejo_b['mitigacion']).sum())

vpn_areas=sum(cf / (1 + 0.06)**i for i, cf in enumerate(costo_areas['costo']))
cma_areas=vpn_areas/((mit_areas_b['mitigacion']).sum())

vpn_incendios=sum(cf / (1 + 0.06)**i for i, cf in enumerate(costo_incendios['costo']))
cma_incendios=vpn_incendios/((mit_incendios_b['mitigacion']).sum())

vpn_sustitucion=sum(cf / (1 + 0.06)**i for i, cf in enumerate(costo_sustitucion['costo']))
cma_sustitucion=vpn_sustitucion/((mit_sustitucion_b['mitigacion']).sum())

vpn_restauracion=sum(cf / (1 + 0.06)**i for i, cf in enumerate(costo_restauracion['costo']))
cma_restauracion=vpn_restauracion/((mit_restauracion_b['mitigacion']).sum())

vpn_lena=sum(cf / (1 + 0.06)**i for i, cf in enumerate(costo_lena['costo']))
cma_lena=vpn_lena/((mit_lena_b['mitigacion']).sum())


df_vpn=pd.DataFrame(
    {
        'Medida':list(df_costos['medida'].unique()),
        'VPN (MMUSD)': [vpn_areas,vpn_forestacion,vpn_incendios,vpn_lena, vpn_manejo,vpn_restauracion,vpn_sustitucion],
        'CM (USD/tCO2eq)': [cma_areas,cma_forestacion,cma_incendios,cma_lena,cma_manejo,cma_restauracion,cma_sustitucion]
    }
)

chart_vpn= (
    (
        alt.Chart(df_vpn).mark_bar().encode(
           alt.X('VPN (MMUSD):Q'),
           alt.Y('Medida:N'),
           alt.Color('Medida:N', legend=None),
        )
    )
    .properties(title="Costo total por medida")
)

chart_costo_anual= (
     (
         alt.Chart(df_costos).mark_bar().encode(
            alt.X('tiempo:O', title='Año'),
            alt.Y('costo:Q', title='Costo anual (MMUSD)'),
            alt.Color('medida:N', title='Medidas'),
         )
     )
)

st.subheader('Costo de las medidas')
col1, col2 = st.columns(2)
with col1:
    st.altair_chart(chart_vpn, use_container_width=True)

with col2:
    st.dataframe(
        df_vpn,
        column_config={
            'VPN (MMUSD)':st.column_config.NumberColumn(
                help='Valor presente neto acumulado',
                format='💰 $ %.2f'
            ),
            'CM (USD/tCO2eq)':st.column_config.NumberColumn(
                help='Costo de mitigación de cada medida',
                format='%.2f $/tCO2eq'
            )
        },
        hide_index=True,
    )

st.altair_chart(chart_costo_anual,use_container_width=True)


#npf.npv()
