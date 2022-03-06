from re import template
import dash
from dash import dcc
from dash import html, Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from os import name


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']



app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

##############        !!!!!!!        Veuillez changer ce chemin       !!!!!!!     #############
##############       !!!!!!!!        Veuillez changer ce chemin      !!!!!!!!     #############
##############        !!!!!!!        Veuillez changer ce chemin       !!!!!!!     #############
##############        !!             Veuillez changer ce chemin       !!          #############
##############        !!             Veuillez changer ce chemin       !!          #############


df = pd.read_csv(r"C:\Users\hp\Desktop\data viz\ExportData.csv", sep=";", decimal=',', low_memory=False)
df = df[df["Continent"] !="AUTRE"]
df_export = df[df["Libellé du flux"] == "Exportations FAB"]
df_import = df[df["Libellé du flux"] == "Importations CAF"]

colors = {
 'background': '#111111',
 'text': '#3376FF'
}





# Exportations


ann = 2018

df_inter = df_export.groupby("Libellé du pays").sum()
df_export_annee=df_inter.loc[:, df_inter.columns.str.startswith('Valeur') & df_inter.columns.str.endswith(str(ann))]
df_1 = pd.DataFrame(df_export_annee.sum(axis=1))
df_1.rename(columns={0:"values_export"}, inplace=True)

df_1 = df_1.sort_values(by="values_export", ascending=False).head(20)
df_1

fig_9 = go.Figure(data=[
    go.Bar(name='ab', x=df_1.index, y=df_1["values_export"])
])
# Change the bar mode
fig_9.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0, 0, 0, 0)', template="plotly_dark")



# fig

annee=2018
test=df_import.groupby("Continent").sum()
df_impo2018=test.loc[:, test.columns.str.startswith('Valeur') & test.columns.str.endswith(str(annee))]
df_impo2018.sum(axis=1)
fig_1 = px.pie(values=df_impo2018.sum(axis=1), names=df_impo2018.sum(axis=1).index, template="plotly_dark")



# Importations



ann = 2018

df_inter = df_import.groupby("Libellé du pays").sum()
df_import_annee=df_inter.loc[:, df_inter.columns.str.startswith('Valeur') & df_inter.columns.str.endswith(str(ann))]
df_1 = pd.DataFrame(df_import_annee.sum(axis=1))
df_1.rename(columns={0:"values_import"}, inplace=True)

df_1 = df_1.sort_values(by="values_import", ascending=False).head(20)
df_1

fig = go.Figure(data=[
    go.Bar(name='ab', x=df_1.index, y=df_1["values_import"])
    
])
fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)',paper_bgcolor='rgba(0, 0, 0, 0)', template="plotly_dark")
fig_2 = fig



app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.Br(),
        html.H1(children="Tableau de bord des Importations et des Exportations du Maroc", style={'text-align': 'center', 'color': '#05F2F2'}),
        html.Br(),
    ], className='row'),
    html.Div(children=[
        
        html.Div([
            
        
        
        html.Label('Veuillez choisir une année', style={'text-align': 'center', 'color': colors['text']}),
        dcc.Dropdown(id="annee_gauche",
        options=[
        {'label': '2018', 'value': 2018},
        {'label': '2019', 'value': 2019},
        {'label': '2020', 'value': 2020},
        {'label': '2021', 'value': 2021}
        ],style={'text-align': 'center', 'color': colors['text']},
        value=2018
        ),

        html.H4(children='Importations et Exportations par principaux produits', style={'text-align': 'center', 'color': colors['text']}),
        dcc.Graph(
            id='graph3',
        ),
        

        ], className='five columns'),
          
        html.Div([
        
        
        

        html.Label('Veuillez choisir une année', style={'text-align': 'center', 'color': colors['text']}),
        dcc.Dropdown(id="annee_droite",
        options=[
        {'label': '2018', 'value': 2018},
        {'label': '2019', 'value': 2019},
        {'label': '2020', 'value': 2020},
        {'label': '2021', 'value': 2021}
        ], style={'text-align': 'center', 'color': colors['text']},
        
        value=2021
        ),

        html.H4(children='Distribution des échanges commerciaux du Maroc', style={'text-align': 'center', 'color': colors['text']}),

        dcc.Graph(
            id='graph5'
        ),

        ], className='seven columns'),

    ], className='row'),

    
    html.Div(style={'text-align': 'center', 'backgroundColor': colors['background']}, children=[
        html.Div([
            html.H4(children='Exportations', style={'text-align': 'center', 'color': colors['text']}),
            html.Div(children='''
            Les 20 premiers pays ayant un grand flux d'Exportations avec le Maroc.
        ''', style={'text-align': 'center', 'color': '#8CFE9D'}),
            dcc.Graph(
                id='graph1',
                figure=fig_9
            ),  
            
        ], className='four columns'),
        html.Div([
           html.H4(children='Importations', style={'text-align': 'center', 'color': colors['text']}),
            html.Div(children='''
            Les 20 premiers pays ayant un grand flux d'Importations avec le Maroc.
        ''', style={'text-align': 'center', 'color': '#8CFE9D'}),
            dcc.Graph(
                id='graph2',
                figure=fig_2
            ),  
            
        ], className='four columns'),
        
        html.Div([

           
            html.Label('Veuillez choisir une Continent', style={'text-align': 'center', 'color': colors['text']}),
            dcc.Dropdown(id="Continent_slctd",
            options=[
            {'label': 'AFRIQUE', 'value': 'AFRIQUE'},
            {'label': 'AMERIQUE', 'value': 'AMERIQUE'},
            {'label': 'ASIE', 'value': 'ASIE'},
            {'label': 'AUSTRALIE', 'value': 'AUSTRALIE'},
            {'label': 'EUROPE', 'value': 'EUROPE'}
            ],style={'text-align': 'center', 'color': colors['text']},
            value='EUROPE'
            ),
            
            dcc.Graph(
                id='graph4'
            ),
            html.H4(children='Evolution des échanges commerciaux Maroc', style={'text-align': 'center', 'color': colors['text']}),
            html.Br()
            
        ], className='four columns'),

    ], className='row'),
    
    
    
])
######################################################################################################################
@app.callback(
    [Output("graph3", "figure"),
    Output("graph5", "figure")], 
    [Input("annee_gauche", "value"),
    Input("annee_droite", "value")]
    )
def update_bar_chart(annee_gauche, annee_droite):
    #               #####################################       graph_haut_guache

    df_inter = df_import.groupby("Code du groupement d'utilisation").sum()
    df_import_annee=df_inter.loc[:, df_inter.columns.str.startswith('Valeur') & df_inter.columns.str.endswith(str(annee_gauche))]
    df_1 = pd.DataFrame(df_import_annee.sum(axis=1))
    df_1.rename(columns={0:"values_import"}, inplace=True)


    df_inter = df_export.groupby("Code du groupement d'utilisation").sum()
    df_export_annee=df_inter.loc[:, df_inter.columns.str.startswith('Valeur') & df_inter.columns.str.endswith(str(annee_gauche))]
    df_2 = pd.DataFrame(df_export_annee.sum(axis=1))
    df_2.rename(columns={0:"values_export"}, inplace=True)

    df_1['values_export'] = df_2['values_export']
    df_12 = df_1
    Continent = df_12.index

    fig_h_g = go.Figure(data=[
        go.Bar(name='Importations', x=Continent, y=df_12["values_import"]),
        go.Bar(name='Exportations', x=Continent, y=df_12["values_export"])
    ])
    fig_h_g.update_layout(template='plotly_dark')
    fig_h_g.update_xaxes(type='category')

    #         #####################################         graph_haut_droit

    df_inter = df_import.groupby("Continent").sum()
    df_import_annee=df_inter.loc[:, df_inter.columns.str.startswith('Valeur') & df_inter.columns.str.endswith(str(annee_droite))]
    df_1 = pd.DataFrame(df_import_annee.sum(axis=1))
    df_1.rename(columns={0:"values_import"}, inplace=True)


    df_inter = df_export.groupby("Continent").sum()
    df_export_annee=df_inter.loc[:, df_inter.columns.str.startswith('Valeur') & df_inter.columns.str.endswith(str(annee_droite))]
    df_2 = pd.DataFrame(df_export_annee.sum(axis=1))
    df_2.rename(columns={0:"values_export"}, inplace=True)

    df_1['values_export'] = df_2['values_export']
    df_12 = df_1

    labels = df_12.index

    # Create subplots:
    fig_h_d = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig_h_d.add_trace(go.Pie(labels=labels, values=df_12["values_import"], name="import"),
                1, 1)
    fig_h_d.add_trace(go.Pie(labels=labels, values=df_12["values_export"], name="export"),
                1, 2)

    
    fig_h_d.update_traces(hole=.4, hoverinfo="label+percent+name")

    fig_h_d.update_layout(
        title_text="Importations et Exportations par Continents",
        
        annotations=[dict(text='import  ', x=0.18, y=0.5, font_size=20, showarrow=False),
                    dict(text='  export', x=0.82, y=0.5, font_size=20, showarrow=False)], template='plotly_dark')


    return fig_h_g, fig_h_d
    #          #####################################         graph_bas_droit
@app.callback(
        Output("graph4", "figure"), 
        Input("Continent_slctd", "value"))

def generate_chart(Continent_slctd):

    continent = Continent_slctd
    dff = df[df["Continent"] == continent]
    df_import = dff[dff["Libellé du flux"] == "Importations CAF"]

    for i in range(2018,2022):

        anne=str(i)
        df_inter = df_import.groupby("Libellé du groupement d'utilisation").sum()
        df_import_annee=df_inter.loc[:, df_inter.columns.str.startswith('Valeur') & df_inter.columns.str.endswith(str(anne))]
        df_1 = pd.DataFrame(df_import_annee.sum(axis=1))
        df_1.rename(columns={0:"values_import"}, inplace=True)


        df_inter = df_export.groupby("Libellé du groupement d'utilisation").sum()
        df_export_annee=df_inter.loc[:, df_inter.columns.str.startswith('Valeur') & df_inter.columns.str.endswith(str(anne))]
        df_2 = pd.DataFrame(df_export_annee.sum(axis=1))
        df_2.rename(columns={0:"values_export"}, inplace=True)

        df_1['values_export'] = df_2['values_export']
        df_12 = df_1

        df_12 = pd.DataFrame(df_12.sum())
        df_12.rename(columns={0:annee}, inplace=True)
        df_12 = df_12.T
        if i == 2018:
            df_test = df_12
            
        if i != 2018:
            df_test.loc[str(i)] = df_12.iloc[0]
            


    fig_b_d = go.Figure()
    fig_b_d.add_trace(go.Scatter(x=df_test.index, y=df_test["values_import"], mode='lines+markers', name='Importations', line_color='#33FFEE'))
    fig_b_d.add_trace(go.Scatter(x=df_test.index, y=df_test["values_export"], name='Exportations', line_color='#FFDD33'))
    fig_b_d.update_xaxes(type='category')
    fig_b_d.update_layout(template='plotly_dark')

    return fig_b_d




#####################################################################################################################

if __name__ == '__main__':
    app.run_server(debug=True)