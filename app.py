"""
This app uses NavbarSimple to navigate between three different pages.
dcc.Location is used to track the current location. A callback uses the current
location to render the appropriate page content. The active prop of each
NavLink is set automatically according to the current pathname. To use this
feature you must install dash-bootstrap-components >= 0.11.0.
For more details on building multi-page Dash applications, check out the Dash
documentation: https://dash.plot.ly/urls
"""
from tempfile import template
# from turtle import width
from grpc import server
from matplotlib.pyplot import autoscale, grid, title
import pandas as pd
import json
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
from PIL import Image
from dash import Input, Output, dcc, html
from sqlalchemy import false
from numerize import numerize
from dash_bootstrap_templates import load_figure_template
load_figure_template(["cyborg", "minty",'flatly','lux'])
img_1918 = Image.open(r"data/sh/New folder/new/new_1918.png")
img_1947 = Image.open(r"data/sh/New folder/new/new_1947.png")
img_1960 = Image.open(r"data/sh/New folder/new/new_1960.png")
img_2015 = Image.open(r"data/sh/New folder/new/new_2015.png")

df1=pd.read_csv(r"data/clean_data/cum_District.csv")
df2=pd.read_csv(r"data/clean_data/units_homless_all.csv")
df3=pd.read_csv(r'data/clean_data/Type_Of_Sturcture_cum.csv')
df4=pd.read_csv(r'data/clean_data/Demolition_Reason_cum.csv')
df5=pd.read_csv(r'data/clean_data/Demolition_Reason_non_cum.csv')
df6=pd.read_csv(r'data/clean_data/Type_Of_Sturcture_non_cum.csv')
df7=pd.read_csv(r'data/clean_data/cum_killed.csv')
df8=pd.read_csv(r'data/clean_data/un_cum_killed.csv')
df9=pd.read_csv(r'data/clean_data/Palestinians_killed.csv')
df10=pd.read_csv(r'data/clean_data/age_range.csv')

years=list(df2.Year.unique())
with open(r'data/raw_data/geoBoundaries-PSE-ADM2.geo.json') as f:
    geo = json.load(f)

fig1=px.bar(df1,x="Housing Units", y='District',animation_frame="Year",orientation='h',width=650,height=520,color='District',
        template='lux',category_orders={'index': df1.index[::-1]},hover_data=["total_Homeless"],title="<b>Demolition Over Years</b>",)
fig1.update_traces(textfont_size=5, textangle=0, textposition="outside", cliponaxis=False,showlegend=False)
fig1.update(layout_showlegend=False)
fig1.update_layout(margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
        pad=0
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',

        )






fig1_1=px.bar(df7,x="Killed", y='District',animation_frame="Year",orientation='h',width=650,height=520,color='District',
        template='lux',category_orders={'index': df1.index[::-1]},hover_data=["Killed"],title="<b>Killed Over Years</b>",)
fig1.update_traces(textfont_size=5, textangle=0, textposition="outside", cliponaxis=False,showlegend=False)
fig1.update(layout_showlegend=False)
fig1.update_layout(margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
        pad=0
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',

        )





list=[img_1918,img_1947,img_1960,img_2015]
# app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app =dash.Dash(
	assets_folder="/assets",
    external_stylesheets=[dbc.themes.LUX]
)
server=app.server
app.title = "Free Palestine"

card_content1 = [

    dbc.CardBody(
        [
            html.H2(className="card-title",id='card1',style={'textAlign':'center',"font-weight": "bold",}),
            html.P(
                className="card-text",id="card1_1",style={'textAlign':'center',"font-size":14,"font-weight": "bold"}
            ),
        ]
    ),
]

card_content2 = [

    dbc.CardBody(
        [
            html.H2(className="card-title",id='card2',style={'textAlign':'center',"font-weight": "bold",'color':'red'}),
            html.P(
                className="card-text",id="card2_2",style={'textAlign':'center',"font-size":14,"font-weight": "bold",'color':'red'}
            ),
        ]
    ),
]

card_content3 = [

    dbc.CardBody(
        [
            html.H2(className="card-title",id='card3',style={'textAlign':'center',"font-weight": "bold",}),
            html.P(
                className="card-text",id="card3_3",style={'textAlign':'center',"font-size":14,"font-weight": "bold"}
            ),
        ]
    ),
]




card_content4 = [

    dbc.CardBody(
        [
            html.H2(className="card-title",id='card4',style={'textAlign':'center',"font-weight": "bold",}),
            html.P(
                className="card-text",id="card4_4",style={'textAlign':'center',"font-size":14,"font-weight": "bold"}
            ),
        ]
    ),
]

card_content5 = [

    dbc.CardBody(
        [
            html.H2(className="card-title",id='card5',style={'textAlign':'center',"font-weight": "bold",'color':'red'}),
            html.P(
                className="card-text",id="card5_5",style={'textAlign':'center',"font-size":14,"font-weight": "bold",'color':'red'}
            ),
        ]
    ),
]

card_content6 = [

    dbc.CardBody(
        [
            html.H2(className="card-title",id='card6',style={'textAlign':'center',"font-weight": "bold",}),
            html.P(
                className="card-text",id="card6_6",style={'textAlign':'center',"font-size":14,"font-weight": "bold"}
            ),
        ]
    ),
]



app.layout = html.Div(
    [
        dcc.Location(id="url"),
        dbc.NavbarSimple(

            children=[dbc.Row(html.Img(src="https://images-ext-2.discordapp.net/external/kPU4DOpEojKELow0BL0jIAjjtCrSyXR1KbfDrefwNJw/https/i.ibb.co/y4Chtgh/palestine.png",
            style={'hieght': '30%', 'width': '30%', 'margin-left':'auto', 'margin-right':'auto'})),
                dbc.NavLink("House Demolition", href="/", active="exact",style={'textAlign':'center',"font-size":20,"font-weight": "bold"}),
                dbc.NavLink('Palestinians murdered', href="/page-1", active="exact",style={'textAlign':'center',"font-size":20,"font-weight": "bold"}),
                # dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],

            brand="Free Palestine",
            brand_href="####",
            color="primary",
            dark=True,
            brand_style={"font-size":35,
                        "font-weight": "bold"}

       ),
        dbc.Container(id="page-content", className="pt-4"),
    ]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div([        dbc.Row([
                                        dbc.Col(dbc.Card(card_content1, color="primary", inverse=True),
                                                style = {'padding-left' : '0%'}),
                                        dbc.Col(dbc.Card(card_content2, color="white", inverse=True)),
                                        dbc.Col(dbc.Card(card_content3, color="green", inverse=True),
                                                style = {'padding-right' : '0%'}),

                                         ],
                                    className="mb-4",
                                         ),html.Hr(className='mb-3'),
                                         html.Br(),


                                dbc.Row([



                                    dbc.Col([

                                        # html.H1('Call back Example 2', style={'textAlign':'left'}),
                                         dcc.Dropdown(years, id='dropdown',value=None,
                                         placeholder='Choose a year ',
                                         style={
                                            'border': 'black',
                                           'color': 'black',
                                              'width': '80%',
                                                  }),
                                         dcc.Graph(id='myGraph2',figure={}),


                                            ],width={"size":5, "order": 3},),





                                dbc.Col([

                                        # html.H1('Call back Example 2', style={'textAlign':'left'}),
                                         dcc.Graph(id='myGraph1',figure=fig1,style = {'padding-left' : '0%'}),


                                                ],width={ "size":6,"order": 1,'offset' :0},align="start"),


                                dbc.Col([


                                ],width={"size":1, "order": 2},)

                                            ],
                                            className="mb-4",

                                            ),html.Hr(className='mb-3'),
                                                html.Br(),





                                dbc.Row([

                                    dbc.Col([

                                        # html.H1('Call back Example 2', style={'textAlign':'left'}),
                        dcc.Slider( min=0,
                                    max=3,
                                    value=4,
                                    id='my-slider',
                                    step=None,


                                    marks={
                                            0: '1918',
                                            1: '1947',
                                            2: '1960',
                                            3: {'label': '2015', 'style': {'color': 'black'}}},
                                            vertical =True

                                )

                                            ],width={"size": 1, "order": 1}),

                                dbc.Col([dcc.Graph(id='myGraph',figure={},),],width={ "order": 2,}),

                                dbc.Col([dcc.Graph(id='myGraph3',figure={},),],width={ "order": 3,}),

                                dbc.Col([dcc.RadioItems(id='radio',
                                                        options=[
                                                            {'label': 'Type', 'value': 1},
                                                            {'label': 'Reason', 'value': 2},
                                                        ],
                                                        value=1
                                                        ),
                                         dcc.Dropdown(years, id='dropdown2',value=None,
                                        placeholder='Choose a year ',),

                                ],width={"size":1 ,"order": 4}),





                                ],),







],className='mb-5')

    elif pathname == "/page-1":
        return html.Div([
            dbc.Row([
                                        dbc.Col(dbc.Card(card_content4, color="primary", inverse=True),
                                                style = {'padding-left' : '0%'}),
                                        dbc.Col(dbc.Card(card_content5, color="white", inverse=True)),
                                        dbc.Col(dbc.Card(card_content6, color="green", inverse=True),
                                                style = {'padding-right' : '0%'}),

                                         ],
                                    className="mb-4",
                                         ),html.Hr(className='mb-3'),
                                         html.Br(),






            dbc.Row([



                                    dbc.Col([

                                         dcc.Dropdown(years, id='dropdown2',value=None,
                                         placeholder='Choose a year ',
                                         style={
                                            'border': 'black',
                                           'color': 'black',
                                              'width': '80%',
                                                  }),
                                         dcc.Graph(id='myGraph2_2',figure={}),


                                            ],width={"size":5, "order": 3},),





                                dbc.Col([

                                         dcc.Graph(id='myGraph1_1',figure=fig1_1,style = {'padding-left' : '0%'}),


                                                ],width={ "size":6,"order": 1,'offset' :0},align="start"),


                                dbc.Col([


                                ],width={"size":1, "order": 2},)

                                            ],
                                            className="mb-4",

                                            ),html.Hr(className='mb-3'),
                                                html.Br(),




                    dbc.Row([


                                dbc.Col([



                                    dcc.Graph(id='myGraph3_3',figure={},),
                                    html.Hr(className='mb-3'),

                                    dcc.Graph(id='myGraph5_5',figure={},),






                                ],width={ 'size':2,"order": 1,}),

                                dbc.Col([




                                    ],width={'size':4, "order": 2,}),

                                dbc.Col([

                                dcc.Graph(id='myGraph4_4',figure={},),
                                     dcc.Dropdown(years, id='dropdown3',value=None,
                                        placeholder='Choose a year ',
                                         style={
                                            'border': 'black',
                                           'color': 'black',
                                              'width': '70%',
                                                  }
                                        )



                                ],width={ 'size':4,"order": 3}),





                                ],),

















        ],className='mb-5')
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

@app.callback(
Output('myGraph2','figure'),
Output('card1','children'),
Output('card1_1','children'),
Output('card2','children'),
Output('card2_2','children'),
Output('card3','children'),
Output('card3_3','children'),


Input('dropdown','value'))
def update_graph2(drowpvalue):
    if drowpvalue==None:

        fig2 = px.choropleth_mapbox(df1[df1['Year']==2022], geojson=geo, color="Housing Units",
                                locations="District", featureidkey="properties.shapeName",
                                color_continuous_scale=px.colors.sequential.Blugrn,
                                range_color=(0, 1000),
                                hover_data=['total_Homeless','Housing Units',"Year"],
                                center={"lat": 31.89, "lon": 34.6},template='lux',
                                # animation_frame="Year",
                                mapbox_style="carto-positron", zoom=7.35,width=600, height=400,
                                )
        fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0},title="Cumulative till 2022",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',

        )
        fig2.update_geos(fitbounds="locations", visible=False)
        # fig.update_traces( hovertemplate='Year:cumulative till 2022')

        ban1=numerize.numerize(int(df1[df1['Year']==2022]['total_Homeless'].sum()))
        ban1_1='Homeless people from 2004 till 2022'

        ban2=numerize.numerize(int(df1[df1['Year']==2022]['Housing Units'].sum()))
        ban2_2='House was Demolished from 2004 till 2022'

        ban3=df1[df1['Year']==2022].sort_values('Housing Units',ascending=False)['District'].iloc[0]
        ban3_3='Highest District in demolishing from 2004 till 2022 '

    else:

        fig2 = px.choropleth_mapbox(df2[df2['Year']==drowpvalue], geojson=geo, color="Housing Units",
                                locations="District", featureidkey="properties.shapeName",
                                color_continuous_scale=px.colors.sequential.Mint,
                                range_color=(0, 100),
                                hover_data=['total_Homeless','Housing Units',"Year"],
                                center={"lat": 31.89, "lon": 34.6},template='plotly_white',
                                # animation_frame="Year",
                                mapbox_style="carto-positron", zoom=7.35,width=600, height=400)
        fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
        )
        fig2.update_geos(fitbounds="locations", visible=False)


        ban1=numerize.numerize(int(df2[df2['Year']==drowpvalue]['total_Homeless'].sum()))
        ban1_1=f'Homeless people at {drowpvalue}'

        ban2=numerize.numerize(int(df2[df2['Year']==drowpvalue]['Housing Units'].sum()))
        ban2_2=f'House was Demolished at {drowpvalue}'

        ban3=df2[df2['Year']==drowpvalue].sort_values('Housing Units',ascending=False)['District'].iloc[0]
        ban3_3=f'Highest District in demolishing at {drowpvalue}'

    return fig2,ban1,ban1_1,ban2,ban2_2,ban3,ban3_3



@app.callback(
Output('myGraph','figure'),
# Output('myGraph2','figure'),
Input('my-slider','value'))
def update_graph(slidervalue):

    if slidervalue not in [0,1,2,3]:
        fig = px.imshow(list[0],template='lux',title='<b>Israeli Invasion</b>')

        fig.update_layout(coloraxis_showscale=False,width=400,height=400,
        # title={
        # 'text': "Israeli Invasion",

        # 'y':0.92,
        # 'x':0.3,
        # 'xanchor': 'center',
        # 'yanchor': 'top'},

        # font_family="Courier New",
        # font_color="Black",
        # title_font_family="Times New Roman",

        # title_font_color="Black",
         margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
        pad=0
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    # paper_bgcolor="white",
        )
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)


    else:
        fig = px.imshow(list[slidervalue],template='lux',title='<b>Israeli Invasion</b>')
        fig1.update_traces(textfont_size=5, textangle=0, textposition="outside", cliponaxis=False,showlegend=False)
        fig.update_layout(coloraxis_showscale=False,width=400,height=400,
        # title={
        # 'text': "Israeli Invasion",
        # 'y':.92,
        # 'x':0.3,
        # 'xanchor': 'center',
        # 'yanchor': 'top'},

        # font_family="Courier New",
        # font_color="Black",
        # title_font_family="Times New Roman",
        # title_font_color="Black",
         margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
        pad=0
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    # paper_bgcolor="white",
        )
        fig.update_xaxes(showticklabels=False)
        fig.update_yaxes(showticklabels=False)

    return fig



@app.callback(
Output('myGraph3','figure'),
# Output('myGraph2','figure'),
Input('radio','value'),
Input('dropdown2','value')

)
def update_graph3(radio,drop):
    if radio ==1 and drop not in years :
        fig3=px.pie(df3[df3['Year']==2022],template='lux',title='<b>Demolition Type and Reason</b>'

        ,values='Housing Units',names='Type Of Sturcture',hole=.6,hover_data=['Housing Units',],)
        fig3.update_traces(textposition='outside', textinfo='percent',pull=[0, 0.2, 0,0,0,0,0])
        fig3.update_layout(coloraxis_showscale=False,width=500,height=400,

            margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
        pad=0
            ),
            # Add annotations in the center of the donut pies.
            annotations=[dict(text='2004-2020', x=0.5, y=0.5, font_size=20, showarrow=False),
                        ],
                                paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)',

                        )

    elif radio == 2 and drop not in years :
        fig3=px.pie(df4[df4['Year']==2022],template='lux',title='<b>Demolition Type and Reason</b>'

        ,values='Housing Units',names='Demolition Reason',hole=.6,hover_data=['Housing Units',])
        fig3.update_traces(textposition='outside', textinfo='percent',pull=[0, 0.2, 0,0,0,0,0])
        fig3.update_layout(coloraxis_showscale=False,width=500,height=400,

            margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
        pad=0
            ),
            # Add annotations in the center of the donut pies.
            annotations=[dict(text='2004-2020', x=0.50, y=0.5, font_size=20, showarrow=False),
                        ],
                                 paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)',
                        )


    if drop in years:

         if radio ==1 :
                fig3=px.pie(df6[df6['Year']==drop],template='lux',title='<b>Demolition Type and Reason</b>'

                ,values='Housing Units',names='Type Of Sturcture',hole=.6,hover_data=['Housing Units',])
                fig3.update_traces(textposition='outside', textinfo='percent',pull=[0, 0.2, 0,0,0,0,0])
                fig3.update_layout(coloraxis_showscale=False,width=500,height=400,

                    margin=dict(
                l=0,
                r=0,
                b=0,
                t=30,
                pad=0
                    ),
                    # Add annotations in the center of the donut pies.
                    annotations=[dict(text=drop, x=0.5, y=0.5, font_size=20, showarrow=False),
                                ],
                                 paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)',

                                )

         elif radio ==2:

                fig3=px.pie(df5[df5['Year']==drop],template='lux',title='<b>Demolition Type and Reason</b>'

                ,values='Housing Units',names='Demolition Reason',hole=.6,hover_data=['Housing Units',])
                fig3.update_traces(textposition='outside', textinfo='percent',pull=[0, 0.2, 0,0,0,0,0])
                fig3.update_layout(coloraxis_showscale=False,width=500,height=400,


                    margin=dict(
                l=0,
                r=0,
                b=0,
                t=30,
                pad=0
                    ),
                    # Add annotations in the center of the donut pies.
                    annotations=[dict(text=drop, x=0.50, y=0.5, font_size=20, showarrow=False),
                                ],

                                paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)',
                                )

    return fig3



@app.callback(
Output('myGraph2_2','figure'),
Output('card4','children'),
Output('card4_4','children'),
Output('card5','children'),
Output('card5_5','children'),
Output('card6','children'),
Output('card6_6','children'),


Input('dropdown2','value'))

def update2_2(drowpvalue2):
    if drowpvalue2==None:

        fig2_2 = px.choropleth_mapbox(df7[df7['Year']==2022], geojson=geo, color="Killed",
                                locations="District", featureidkey="properties.shapeName",
                                color_continuous_scale=px.colors.sequential.Blugrn,
                                range_color=(0, 1000),
                                hover_data=['Killed',"Year"],
                                center={"lat": 31.89, "lon": 34.6},template='plotly_white',
                                mapbox_style="carto-positron", zoom=7.35,width=600, height=400,
                                )
        fig2_2.update_layout(margin={"r":0,"t":0,"l":0,"b":0},title="Cumulative Killed till 2022",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',

        )
        fig2_2.update_geos(fitbounds="locations", visible=False)
        # fig.update_traces( hovertemplate='Year:cumulative till 2022')

        ban4=numerize.numerize(int(df7[df7['Year']==2022]['Killed'].sum()))
        ban4_4='Number of Killed people from 2000 till 2022'

        ban6=df7[df7['Year']==2022].sort_values('Killed',ascending=False)['District'].iloc[0]
        ban6_6='Highest District in killing from 2000 till 2022 '

        yy=df9.groupby(["Year","Event location - District",'Type of injury'],as_index=False).sum().drop(columns=['Day','Age'])
        d=yy[yy['Event location - District']=='Gaza'].groupby('Type of injury',as_index=False).count().sort_values(by='Count',ascending=False).iloc[0][0]

        ban5=d
        ban5_5='Most Type of injury'

    else:

        fig2_2 = px.choropleth_mapbox(df8[df8['Year']==drowpvalue2], geojson=geo, color="Killed",
                                locations="District", featureidkey="properties.shapeName",
                                color_continuous_scale=px.colors.sequential.Mint,
                                range_color=(0, 100),
                                hover_data=['Killed',"Year"],
                                center={"lat": 31.89, "lon": 34.6},template='plotly_white',
                                # animation_frame="Year",
                                mapbox_style="carto-positron", zoom=7.35,width=600, height=400)
        fig2_2.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
        )
        fig2_2.update_geos(fitbounds="locations", visible=False)


        ban4=int(df8[df8['Year']==drowpvalue2]['Killed'].sum())
        ban4_4=f'Number of killed people at {drowpvalue2}'

        ban6=df8[df8['Year']==drowpvalue2].sort_values('Killed',ascending=False)['District'].iloc[0]
        ban6_6=f'Highest District in killing at {drowpvalue2}'


        yy=df9.groupby(["Year","Event location - District",'Type of injury'],as_index=False).sum().drop(columns=['Day','Age'])
        d=yy[yy['Event location - District']=='Gaza'].groupby('Type of injury',as_index=False).count().sort_values(by='Count',ascending=False).iloc[0][0]

        ban5=d
        ban5_5='Most Type of injury'

    return fig2_2,ban4,ban4_4,ban5,ban5_5,ban6,ban6_6







@app.callback(
Output('myGraph3_3','figure'),
# Output('myGraph2','figure'),
Input('dropdown3','value'))

def update2_3(dropvalue3):
    mf=df9.groupby(['Gender','Year'],as_index=False).sum().drop(columns=['Age','Day'])
    if dropvalue3 ==None :
        fig5=px.pie(mf[mf['Year']==2022],template='lux',title='<b>Males VS Females</b>'

        ,values='Count',names='Gender',hole=.6,hover_data=['Count',],)
        fig5.update_traces(textposition='outside', textinfo='percent',pull=[0, 0.2, 0,0,0,0,0])
        fig5.update_layout(coloraxis_showscale=False,width=500,height=400,

            margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
        pad=0
            ),
            # Add annotations in the center of the donut pies.
            annotations=[dict(text='2022', x=0.5, y=0.5, font_size=20, showarrow=False),
                        ],
                                paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)',

                        )

    else:

        fig5=px.pie(mf[mf['Year']==dropvalue3],template='lux',title='<b>Males VS Females</b>'

        ,values='Count',names='Gender',hole=.6,hover_data=['Count',],)
        fig5.update_traces(textposition='outside', textinfo='percent',pull=[0, 0.2, 0,0,0,0,0])
        fig5.update_layout(coloraxis_showscale=False,width=500,height=400,

            margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
        pad=0
            ),
            # Add annotations in the center of the donut pies.
            annotations=[dict(text=dropvalue3, x=0.5, y=0.5, font_size=20, showarrow=False),
                        ],
                                paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)',

                        )

    return fig5




@app.callback(
Output('myGraph4_4','figure'),
# Output('myGraph2','figure'),
Input('dropdown3','value'))


def update2_4(dropvalue3):
    if  dropvalue3 ==None :

        fig6=px.bar(df10[df10['Year']==2020],x="Age Range", y='Count',width=650,height=520,color='Age Range',text_auto='.2s',
        template='lux',category_orders={'index': df10.index[::-1]},hover_data=["Count","Year"],title="<b>Killed By Age</b>",)
        fig6.update_traces(textfont_size=15, textangle=0, textposition="outside", cliponaxis=False,showlegend=False)
        fig6.update(layout_showlegend=False)
        fig6.update_layout(margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
        pad=0
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',

        )

    else:
        fig6=px.bar(df10[df10['Year']==dropvalue3],x="Age Range", y='Count',width=650,height=520,color='Age Range',text_auto='.2s',
        template='lux',category_orders={'index': df10.index[::-1]},hover_data=["Count","Year"],title="<b>Killed By Age</b>",)
        fig6.update_traces(textfont_size=15, textangle=0, textposition="outside", cliponaxis=False,showlegend=False)
        fig6.update(layout_showlegend=False)
        fig6.update_layout(margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
        pad=0
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',

        )




    return fig6







@app.callback(
Output('myGraph5_5','figure'),
# Output('myGraph2','figure'),
Input('dropdown3','value'))
def update2_5(dropvalue3):
    killby=df9.groupby(['Killed By','Year'],as_index=False).sum().drop(columns=['Day','Age']).sort_values(by="Year")
    if dropvalue3 ==None :
        fig7=px.pie(killby[killby['Year']==2022],template='lux',title='<b>Killed By</b>'

        ,values='Count',names='Killed By',hole=.6,hover_data=['Count'],)
        fig7.update_traces(textposition='outside', textinfo='percent',pull=[0, 0.2, 0,0,0,0,0])
        fig7.update_layout(coloraxis_showscale=False,width=500,height=400,

            margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
        pad=0
            ),
            # Add annotations in the center of the donut pies.
            annotations=[dict(text='2022', x=0.5, y=0.5, font_size=20, showarrow=False),
                        ],
                                paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)',

                        )

    else:

        fig7=px.pie(killby[killby['Year']==dropvalue3],template='lux',title='<b>Killed By</b>'

        ,values='Count',names='Killed By',hole=.6,hover_data=['Count'],)
        fig7.update_traces(textposition='outside', textinfo='percent',pull=[0, 0.2, 0,0,0,0,0])
        fig7.update_layout(coloraxis_showscale=False,width=500,height=400,

            margin=dict(
        l=0,
        r=0,
        b=0,
        t=30,
        pad=0
            ),
            # Add annotations in the center of the donut pies.
            annotations=[dict(text=dropvalue3, x=0.5, y=0.5, font_size=20, showarrow=False),
                        ],
                                paper_bgcolor='rgba(0,0,0,0)',
                                 plot_bgcolor='rgba(0,0,0,0)',

                        )

    return fig7









if __name__ == "__main__":
    app.run_server()
