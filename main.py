import streamlit as st
st.set_page_config( layout='wide')
import pandas as pd
import altair as alt
import plotly.express as px
import plotly.graph_objects as go


padding = 0
st.markdown(f""" <style>.reportview-container .main .block-container{{padding-top: {padding}rem;padding-bottom: {padding}rem;}}</style> """, unsafe_allow_html=True)
st.markdown(""" <style>#MainMenu {visibility: hidden;}</style>""", unsafe_allow_html=True)

Title_html = """
    <style>
        .title h1{
          font-size: 95px;
          font_family:'Britannic Bold';
          color: white;
          background-image: url("https://i.postimg.cc/J4y2tM2t/customer.jpg");
          height:280px;}        
    </style> 
    <div class="title">
        <h1 align='center'>Customer Analysis</h1>
    </div>
    """
st.markdown(Title_html, unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">',unsafe_allow_html=True,)
query_params = st.experimental_get_query_params()
tabs = ["Home"," "," ","Education"," "," ","Marital_Status"," "," "," ", "Age"]
if "tab" in query_params:
    active_tab = query_params["tab"][0]
else:
    active_tab = "Home"
if active_tab not in tabs:
    st.experimental_set_query_params(tab="Home")
    active_tab = "Home"
li_items = "".join(
    f"""
    <li class="nav-item">
        <a class="nav-link{' active' if t==active_tab else ''}" href="/?tab={t}">{t}</a>
    </li>
    """
    for t in tabs)
tabs_html = f"""
    <ul class="nav nav-tabs">
    {li_items}
    </ul>"""
st.markdown(tabs_html, unsafe_allow_html=True)

#Menu
if active_tab == "Home":
    st.markdown(
        "<h6 class='home'>Customer classification means that the product market can be divided into separate groups of customers. In this way, customer management will be easier and as a result, customer needs can be better met. In this data set, 2240 customers with 29 features are available. The first step is to examine the data and graphical graphs of the data are shown to achieve an acceptable understanding of the data. The required preprocessions are then performed on the data to select useful features for categorizing customers from a set of available features, and in this step, graphical diagrams are provided. In the next step, using the silhouette method, the number of clusters for the model is obtained and finally the model is created. According to the output of the model and the obtained diagrams, the desired results are presented for categorizing customers.</h6>",
        unsafe_allow_html=True)
    st.write("")
    st.write("")
    # df = pd.read_excel('data.xlsx')
    # st.dataframe(df)

elif active_tab == "Education":
    data = pd.read_excel('ndata.xlsx')
    data = pd.DataFrame(data)
    options = st.multiselect('What Features you want to compare?',
                             ['Purchase', 'Marital Status', 'Costs', 'Income', 'users_day'])

    if 'Income' in options:
        fig = px.bar(data, x='Education', y='Income', color='Marital_Status')
        fig.update_layout(title_text='Realation between Education and Marital Status with Income', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
    if 'Costs' in options:
        fig = px.bar(data, x='Education', y='Costs', color='Marital_Status')
        fig.update_layout(title_text='Realation between Education and Marital Status with Costs', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
    if 'Purchase' in options:
        fig = px.bar(data, x='Education', y='Purchase', color='Marital_Status')
        fig.update_layout(title_text='Realation between Education and Marital Status with Purchase', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
    if 'users_day' in options:
        fig = px.bar(data, x='Education', y='users_day', color='Marital_Status')
        fig.update_layout(title_text='Realation between Education and Marital Status with Users Day', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
    if 'Marital Status' in options:
        chart2 = alt.Chart(data).mark_bar().encode(alt.X("Education"), y="count()", color='Marital_Status',
                                                   tooltip='count()'
                                                   ).properties(title='Realation between Education and Marital Status')
        st.altair_chart(chart2, use_container_width=True)
    labels = ['Graduation', 'phD', 'Master', 'Bachelor']
    values = [1127, 486, 370, 257]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    st.write(fig)

elif active_tab == "Marital_Status":
    data = pd.read_excel('ndata.xlsx')
    data = pd.DataFrame(data)
    options = st.multiselect('What Features you want to compare?',
                             ['Purchase', 'Education', 'Costs', 'Income', 'users_day'])

    if 'Income' in options:
        fig = px.bar(data, x='Marital_Status', y='Income', color='Education')
        fig.update_layout(title_text='Realation between Marital_Status and Education with Income', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
    if 'Costs' in options:
        fig = px.bar(data, x='Marital_Status', y='Costs', color='Education')
        fig.update_layout(title_text='Realation between Marital_Status and Education with Costs', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
    if 'Purchase' in options:
        fig = px.bar(data, x='Marital_Status', y='Purchase', color='Education')
        fig.update_layout(title_text='Realation between Marital_Status and Education with Purchase', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
    if 'users_day' in options:
        fig = px.bar(data, x='Marital_Status', y='users_day', color='Education')
        fig.update_layout(title_text='Realation between Marital_Status and Education with Users Day', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
    if 'Education' in options:
        chart2 = alt.Chart(data).mark_bar().encode(alt.X("Marital_Status"), y="count()", color='Education',
                                                   tooltip='count()'
                                                   ).properties(title='Realation between Marital Status and Education')
        st.altair_chart(chart2, use_container_width=True)
    labels = ['Single', 'Relationship']
    values = [796, 1444]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    st.write(fig)

elif active_tab == "Age":
    data = pd.read_excel('ndata.xlsx')
    data = pd.DataFrame(data)
    chart1 = alt.Chart(data).mark_bar().encode(alt.X("Age"), y="count()", color='Education', tooltip='count()'
                                               ).properties(title='Realation between Age and Education')
    st.altair_chart(chart1, use_container_width=True)

    chart2 = alt.Chart(data).mark_bar().encode(alt.X("Age"), y="count()", color='Marital_Status', tooltip='count()'
                                               ).properties(title='Realation between Age and Marital_Status')
    st.altair_chart(chart2, use_container_width=True)

    fig = px.bar(data, x='Age', y='Income', color='Education')
    fig.update_layout(title_text='Realation between Age and Education with Income', title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)

    fig = px.bar(data, x='Age', y='Costs', color='Education')
    fig.update_layout(title_text='Realation between Age and Education with Costs', title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("Something has gone terribly wrong.")