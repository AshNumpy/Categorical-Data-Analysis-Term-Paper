import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('../Datasets/processed.csv')

cols = []

with open('../Datasets/questions.txt', 'r') as f:
    for line in f:
        cols.append(line.strip('\n'))

df.groupby('Sex').size().reset_index(name='counts')
temp = df.groupby('Sex').size().reset_index(name='counts')

# donut chart
fig = px.pie(temp, values='counts', names='Sex', title='Cinsiyet Dağılımı', hole=.5)
fig.update_traces(textposition='inside', textinfo='value+label', textfont_size=15)
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide', width=500, height=500, title_x=0.5, title_font_size=20)
fig.show()

temp = df.groupby('Department').size().reset_index(name='counts')

# donut chart
fig = px.pie(temp, values='counts', names='Department', title='Bölümlere Göre Dağılım', hole=.5)
fig.update_traces(textposition='outside', textinfo='value+label', textfont_size=15)
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide', width=700, height=500, title_x=0.5, title_font_size=20)
fig.show()

temp = df.groupby('Department').size().reset_index(name='counts').sort_values(by='counts', ascending=False)

# bar chart
fig = px.bar(temp, y='Department', x='counts', title='Bölümlere Göre Dağılım', text='counts', color='Department')
fig.update_traces(textposition='outside', textfont_size=15)
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide', width=700, height=500, title_x=0.5, title_font_size=20)
fig.update_xaxes(title_text='Kişi Sayısı')
fig.update_yaxes(title_text='Bölüm')
fig.show()

temp = df[['likert_1']]

# Histogram grafiği
fig = go.Figure()

fig.add_trace(go.Histogram(
    x=df['likert_1'],
    nbinsx=5
))

# Caption başlığı
caption_text = "Onun hakkındaki fikirlerimi etkiler."

fig.update_layout(
    title_x=0.5,
    title_font_size=20,
    title_font_color="Black",
    title_text="Kız/Erkek arkadaşımın sosyal medya kullanımı",
    xaxis_title_text="Ölçek Puanı",
    yaxis_title_text="Kişi Sayısı",
    width=900,
    height=500,
    annotations=[
        dict(
            x=1,
            y=2,
            xref="x",
            yref="y",
            text="Kesinlikle Katılmıyorum",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=30
        ),
        dict(
            x=5,
            y=2,
            xref="x",
            yref="y",
            text="Kesinlikle Katılıyorum",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=30
        ),
        dict(
            x=0.5,
            y=1.125,
            xref='paper',
            yref='paper',
            text=caption_text,
            showarrow=False,
            font=dict(
                size=20,
                color='Black'
            )
        )
    ]
)

fig.show()

# Histogram grafiği
fig = go.Figure()

fig.add_trace(go.Histogram(
    x=df['likert_2'],
    nbinsx=5
))

# Caption başlığı
caption_text = "istediği gibi kurcalayabilir."

fig.update_layout(
    title_x=0.5,
    title_font_size=20,
    title_font_color="Black",
    title_text="Kız/Erkek arkadaşım telefonumu",
    xaxis_title_text="Ölçek Puanı",
    yaxis_title_text="Kişi Sayısı",
    width=900,
    height=500,
    annotations=[
        dict(
            x=1,
            y=2,
            xref="x",
            yref="y",
            text="Kesinlikle Katılmıyorum",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=30
        ),
        dict(
            x=5,
            y=2,
            xref="x",
            yref="y",
            text="Kesinlikle Katılıyorum",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=30
        ),
        dict(
            x=0.5,
            y=1.125,
            xref='paper',
            yref='paper',
            text=caption_text,
            showarrow=False,
            font=dict(
                size=20,
                color='Black'
            )
        )
    ]
)

fig.show()

# Histogram grafiği
fig = go.Figure()

fig.add_trace(go.Histogram(
    x=df['likert_3'],
    nbinsx=5
))

# Caption başlığı
caption_text = ""

fig.update_layout(
    title_x=0.5,
    title_font_size=20,
    title_font_color="Black",
    title_text="İlk buluşmada hesap ortak olarak ödenmeli.",
    xaxis_title_text="Ölçek Puanı",
    yaxis_title_text="Kişi Sayısı",
    width=900,
    height=500,
    annotations=[
        dict(
            x=1,
            y=2,
            xref="x",
            yref="y",
            text="Kesinlikle Katılmıyorum",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=30
        ),
        dict(
            x=5,
            y=2,
            xref="x",
            yref="y",
            text="Kesinlikle Katılıyorum",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=30
        ),
        dict(
            x=0.5,
            y=1.125,
            xref='paper',
            yref='paper',
            text=caption_text,
            showarrow=False,
            font=dict(
                size=20,
                color='Black'
            )
        )
    ]
)

fig.show()

# Histogram grafiği
fig = go.Figure()

fig.add_trace(go.Histogram(
    x=df['likert_4'],
    nbinsx=5
))

# Caption başlığı
caption_text = "gece eğlenmeye çıkabilir."

fig.update_layout(
    title_x=0.5,
    title_font_size=20,
    title_font_color="Black",
    title_text="Kız/Erkek arkadaşım ben olmadan",
    xaxis_title_text="Ölçek Puanı",
    yaxis_title_text="Kişi Sayısı",
    width=900,
    height=500,
    annotations=[
        dict(
            x=1,
            y=2,
            xref="x",
            yref="y",
            text="Kesinlikle Katılmıyorum",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=30
        ),
        dict(
            x=5,
            y=2,
            xref="x",
            yref="y",
            text="Kesinlikle Katılıyorum",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=30
        ),
        dict(
            x=0.5,
            y=1.125,
            xref='paper',
            yref='paper',
            text=caption_text,
            showarrow=False,
            font=dict(
                size=20,
                color='Black'
            )
        )
    ]
)

fig.show()

# Histogram grafiği
fig = go.Figure()

fig.add_trace(go.Histogram(
    x=df['likert_5'],
    nbinsx=5
))

# Caption başlığı
caption_text = ""

fig.update_layout(
    title_x=0.5,
    title_font_size=20,
    title_font_color="Black",
    title_text="Kız/Erkek arkadaşım giyimime karışabilir.",
    xaxis_title_text="Ölçek Puanı",
    yaxis_title_text="Kişi Sayısı",
    width=900,
    height=500,
    annotations=[
        dict(
            x=1,
            y=2,
            xref="x",
            yref="y",
            text="Kesinlikle Katılmıyorum",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=30
        ),
        dict(
            x=5,
            y=2,
            xref="x",
            yref="y",
            text="Kesinlikle Katılıyorum",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=30
        ),
        dict(
            x=0.5,
            y=1.125,
            xref='paper',
            yref='paper',
            text=caption_text,
            showarrow=False,
            font=dict(
                size=20,
                color='Black'
            )
        )
    ]
)

fig.show()

# Histogram grafiği
fig = go.Figure()

fig.add_trace(go.Histogram(
    x=df['likert_6'],
    nbinsx=5
))

# Caption başlığı
caption_text = "cinsten yakın arkadaşı olabilir."

fig.update_layout(
    title_x=0.5,
    title_font_size=20,
    title_font_color="Black",
    title_text="Kız/Erkek arkadaşımın karşı",
    xaxis_title_text="Ölçek Puanı",
    yaxis_title_text="Kişi Sayısı",
    width=900,
    height=500,
    annotations=[
        dict(
            x=1,
            y=2,
            xref="x",
            yref="y",
            text="Kesinlikle Katılmıyorum",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=30
        ),
        dict(
            x=5,
            y=2,
            xref="x",
            yref="y",
            text="Kesinlikle Katılıyorum",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=30
        ),
        dict(
            x=0.5,
            y=1.125,
            xref='paper',
            yref='paper',
            text=caption_text,
            showarrow=False,
            font=dict(
                size=20,
                color='Black'
            )
        )
    ]
)

fig.show()

# Histogram grafiği
fig = go.Figure()

fig.add_trace(go.Histogram(
    x=df['likert_7'],
    nbinsx=5
))

# Caption başlığı
caption_text = "ilişkileri benim için önemsizdir."

fig.update_layout(
    title_x=0.5,
    title_font_size=20,
    title_font_color="Black",
    title_text="Kız/Erkek arkadaşımın önceki",
    xaxis_title_text="Ölçek Puanı",
    yaxis_title_text="Kişi Sayısı",
    width=900,
    height=500,
    annotations=[
        dict(
            x=1,
            y=2,
            xref="x",
            yref="y",
            text="Kesinlikle Katılmıyorum",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=30
        ),
        dict(
            x=5,
            y=2,
            xref="x",
            yref="y",
            text="Kesinlikle Katılıyorum",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=30
        ),
        dict(
            x=0.5,
            y=1.125,
            xref='paper',
            yref='paper',
            text=caption_text,
            showarrow=False,
            font=dict(
                size=20,
                color='Black'
            )
        )
    ]
)

fig.show()

df.iloc[:,10].value_counts()
temp = df.groupby('soru8').size().reset_index(name='counts').sort_values(by='counts', ascending=False)

fig = px.bar(temp, x='soru8', y='counts', text='counts', color='soru8')
fig.update_traces(texttemplate='%{text:.2s}', textposition='inside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

# Caption başlığı
caption_text = "hangi faktör sizin için en önemlisidir?"

fig.update_layout(
    title_x=0.5,
    title_font_size=20,
    title_font_color="Black",
    title_text="Kız/Erkek arkadaşı seçiminde",
    xaxis_title_text="Seçilenler",
    yaxis_title_text="Kişi Sayısı",
    width=1000,
    height=700,
    annotations=[
        dict(
            x=0.5,
            y=1.1,
            xref='paper',
            yref='paper',
            text=caption_text,
            showarrow=False,
            font=dict(
                size=20,
                color='Black'
            )
        )
    ],
    xaxis=dict(
        tickmode='linear',
        tick0=1,
        dtick=1
    ),
    margin=dict(t=120),
    showlegend=False
)

fig.show()

temp = df.groupby('soru9').size().reset_index(name='counts').sort_values(by='counts', ascending=False)

fig = px.bar(temp, x='soru9', y='counts', text='counts', color='soru9')
fig.update_traces(texttemplate='%{text:.2s}', textposition='inside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

# Caption başlığı
caption_text = "hangi özellikleri önemsiyorsunuz?"

fig.update_layout(
    title_x=0.5,
    title_font_size=20,
    title_font_color="Black",
    title_text="Kız/Erkek arkadaşı seçiminde",
    xaxis_title_text="Seçilenler",
    yaxis_title_text="Kişi Sayısı",
    width=1000,
    height=700,
    annotations=[
        dict(
            x=0.5,
            y=1.1,
            xref='paper',
            yref='paper',
            text=caption_text,
            showarrow=False,
            font=dict(
                size=20,
                color='Black'
            )
        )
    ],
    margin=dict(t=120),
    showlegend=False
)

fig.show()

temp = df.groupby('soru10').size().reset_index(name='counts').sort_values(by='counts', ascending=False)

fig = px.bar(temp, x='soru10', y='counts', text='counts', color='soru10')
fig.update_traces(texttemplate='%{text:.2s}', textposition='inside')
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

# Caption başlığı
caption_text = "başarının anahtarı sizce nedir?"

fig.update_layout(
    title_x=0.5,
    title_font_size=20,
    title_font_color="Black",
    title_text="Kız/Erkek ilişkilerinde",
    xaxis_title_text="Seçilenler",
    yaxis_title_text="Kişi Sayısı",
    width=1000,
    height=700,
    annotations=[
        dict(
            x=0.5,
            y=1.1,
            xref='paper',
            yref='paper',
            text=caption_text,
            showarrow=False,
            font=dict(
                size=20,
                color='Black'
            )
        )
    ],
    margin=dict(t=120),
    showlegend=False
)

fig.show()

# Histogram grafiği
fig = go.Figure()

fig.add_trace(go.Histogram(
    x=df['soru11']
))

# Caption başlığı
caption_text = ""

fig.update_layout(
    title_x=0.5,
    title_font_size=20,
    title_font_color="Black",
    title_text="Kaç tane romantik ilişkiniz oldu?",
    xaxis_title_text="İlişki Sayısı",
    yaxis_title_text="Kişi Sayısı",
    width=900,
    height=500,
    annotations=[
        dict(
            x=0.5,
            y=1.125,
            xref='paper',
            yref='paper',
            text=caption_text,
            showarrow=False,
            font=dict(
                size=20,
                color='Black'
            )
        )
    ]
)

fig.show()

# Histogram grafiği
fig = go.Figure()

fig.add_trace(go.Histogram(
    x=df['soru12'],
    xbins=dict(
        start=0,
        end=100,
        size=5
    )
))

# Caption başlığı
caption_text = ""

fig.update_layout(
    title_x=0.5,
    title_font_size=20,
    title_font_color="Black",
    title_text="En uzun ilişkiniz ne kadar sürdü?",
    xaxis_title_text="İlişkinin Uzunluğu (Ay)",
    yaxis_title_text="Kişi Sayısı",
    width=900,
    height=500,
    annotations=[
        dict(
            x=0.5,
            y=1.125,
            xref='paper',
            yref='paper',
            text=caption_text,
            showarrow=False,
            font=dict(
                size=20,
                color='Black'
            )
        )
    ],

    xaxis=dict(
        tickmode='linear',
        tick0=0,
        dtick=10
    )
)

fig.show()
# Histogram grafiği
fig = go.Figure()

fig.add_trace(go.Histogram(
    x=df['soru13'],
    xbins=dict(
        start=0,
        end=30,
        size=3
    )
))

# Caption başlığı
caption_text = "yaklaşık kaç gün görüşüyorsunuz?"

fig.update_layout(
    title_x=0.5,
    title_font_size=20,
    title_font_color="Black",
    title_text="Kız/Erkek arkadaşınızla bir ayda",
    xaxis_title_text="Görüşülen Gün Sayısı",
    yaxis_title_text="Kişi Sayısı",
    width=900,
    height=500,
    annotations=[
        dict(
            x=0.5,
            y=1.125,
            xref='paper',
            yref='paper',
            text=caption_text,
            showarrow=False,
            font=dict(
                size=20,
                color='Black'
            )
        )
    ],

    xaxis=dict(
        tickmode='linear',
        tick0=0,
        dtick=5
    )
)

fig.show()