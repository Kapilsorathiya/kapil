# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:38:02 2021

@author: kapil
"""
import streamlit as st
import numpy as np
st.title("Oil well performance")

Pr=st.sidebar.number_input("Average Reservoir Pressure",min_value=float(0), max_value=float(10000000000000000000),step=0.5,value=float(2500))
qo=st.sidebar.number_input("Oil Flowrate",min_value=float(0), max_value=float(1000000000000000000),step=0.5,value=float(350))
Pwf=st.sidebar.number_input("Flowing Bottomhole Pressure",min_value=float(0), max_value=float(100000000000000000),step=0.5,value=float(2000))
Pb=st.sidebar.number_input("Bubble Point Pressure",min_value=float(0), max_value=float(100000000000000000000),step=0.5,value=float(2500))

IPR=["Vogel's","Wiggin's"]

def saturated_reservoir():
    Qmax=qo/(1-0.2*(Pwf/Pr)-0.8*((Pwf/Pr)**2))
    st.write("Maximum oil flowrate = ",Qmax," bbl/day")
    Flowing_pressure=np.arange(Pr,0-(Pr/20),-Pr/20)
    f_p=Flowing_pressure
    flow=[]
    for i in f_p:
        Q=Qmax*(1-0.2*(i/Pr)-0.8*((i/Pr)**2))
        flow.append(Q)
    import plotly.express as px
    fig = px.scatter(x=flow,y=f_p)
    fig.update_layout(xaxis_title="Flowrate (bbl/day)", yaxis_title="Flowing  bottomhole  pressure (psi)")
    st.write(fig)

def undersaturated_reservoir():
    if Pwf>=Pb:
        j=qo/(Pr-Pwf)
        qob=j*(Pr-Pb)
        Qmax1=qob+((j*Pb)/1.8)
        st.write("Maximum oil flowrate = ",Qmax1," bbl/day")
        st.write("J = ",j," (bbl per day)/psi")
        Flowing_pressure=np.arange(Pr,Pb-((Pr-Pb)/10),-((Pr-Pb)/10))
        f_p=[]
        for f in Flowing_pressure:
            f_p.append(f) 
        Flowing_pressure1=np.arange(Pb,0-(Pb/20),-Pb/20)
        for f1 in Flowing_pressure1:
            f_p.append(f1)
        flow=[]
        for i in Flowing_pressure:
            Q=j*(Pr-i)
            flow.append(Q)
        for k in Flowing_pressure1:
            Q1=qob+((j*Pb)/1.8)*(1-0.2*(k/Pb)-0.8*((k/Pb)**2))
            flow.append(Q1)
        import plotly.express as px
        fig = px.scatter(x=flow,y=f_p)
        fig.update_layout(xaxis_title="Flowrate (bbl/day)", yaxis_title="Flowing  bottomhole  pressure (psi)")
        st.write(fig)
    else:
        j=qo/((Pr-Pb)+(Pb/1.8)*(1-0.2*(Pwf/Pb)-0.8*((Pwf/Pb)**2)))
        st.write("J = ",j," (bbl per day)/psi")
        qob=j*(Pr-Pb)
        Flowing_pressure=np.arange(Pr,Pb-((Pr-Pb)/10),-((Pr-Pb)/10))
        f_p=[]
        for f in Flowing_pressure:
            f_p.append(f) 
        Flowing_pressure1=np.arange(Pb,0-(Pb/20),-Pb/20)
        for f1 in Flowing_pressure1:
            f_p.append(f1)
        flow=[]
        for i in Flowing_pressure:
            Q=j*(Pr-i)
            flow.append(Q)
        for k in Flowing_pressure1:
            Q1=qob+((j*Pb)/1.8)*(1-0.2*(k/Pb)-0.8*((k/Pb)**2))
            flow.append(Q1)
        import plotly.express as px
        fig = px.scatter(x=flow,y=f_p)
        fig.update_layout(xaxis_title="Flowrate (bbl/day)", yaxis_title="Flowing  bottomhole  pressure (psi)")
        st.write(fig)

def wiggins_saturated():
    Pb=st.sidebar.number_input("Bubble Point Pressure",value=Pr)
    qomax=qo/(1-0.52*(Pwf/Pr)-0.48*((Pwf/Pr)**2))
    st.write("Maximum oil flowrate = ",qomax," bbl/day")
    Flowing_pressure=np.arange(Pr,0-(Pr/20),-Pr/20)
    f_p=Flowing_pressure
    flow=[]
    for i in f_p:
        Q=qomax*(1-0.52*(i/Pr)-0.48*((i/Pr)**2))
        flow.append(Q)
    import plotly.express as px
    fig = px.scatter(x=flow,y=f_p)
    fig.update_layout(xaxis_title="Flowrate (bbl/day)", yaxis_title="Flowing  bottomhole  pressure (psi)")
    st.write(fig)
        
        
def call():
    if curve=="Vogel's":
        if Pwf>Pb or Pwf>Pr:
            st.write("Reservoir fluid is not comming in wellbore because flowing hole pressure is greater")
        st.write("** Using Vogel's method**")
        elif Pr<=Pb:
            st.write("Saturated Reservoir with Bubble point pressure ",Pb ,"psi.")
            saturated_reservoir()
        elif Pr>Pb:
            st.write("Undersaturated Reservoir with Bubble point pressure ",Pb ,"psi.")
            undersaturated_reservoir()

    if curve=="Wiggin's":
        st.write("** Using Wiggin's method**")
        wiggins_saturated()

curve=st.sidebar.radio("Select IPR curve",IPR)
butten = st.sidebar.button('Submit')

if butten:
    call()

def First_Approximation_Method():
    Qmaxp=qo/(1-0.2*(Pwf/Pr)-0.8*((Pwf/Pr)**2))
    Qmaxf=Qmaxp*(Prf/Pr)*(0.2+0.8*(Prf/Pr))
    st.write("Future maximum oil flowrate = ",Qmaxf," bbl/day")
    Flowing_pressure=np.arange(Prf,0-(Prf/20),-Prf/20)
    f_p=Flowing_pressure
    flow=[]
    for i in f_p:
        Q=Qmaxf*(1-0.2*(i/Prf)-0.8*((i/Prf)**2))
        flow.append(Q)
    import plotly.express as px
    fig = px.scatter(x=flow,y=f_p)
    fig.update_layout(xaxis_title="Flowrate (bbl/day)", yaxis_title="Flowing  bottomhole  pressure (psi)")
    st.write(fig)
        
def Second_Approximation_Method():
    Qmaxp=qo/(1-0.2*(Pwf/Pr)-0.8*((Pwf/Pr)**2))
    Qmaxf=Qmaxp*((Prf/Pr)**3)
    st.write("Future maximum oil flowrate = ",Qmaxf," bbl/day")
    Flowing_pressure=np.arange(Prf,0-(Prf/20),-Prf/20)
    f_p=Flowing_pressure
    flow=[]
    for i in f_p:
        Q=Qmaxf*(1-0.2*(i/Prf)-0.8*((i/Prf)**2))
        flow.append(Q)
    import plotly.express as px
    fig = px.scatter(x=flow,y=f_p)
    fig.update_layout(xaxis_title="Flowrate (bbl/day)", yaxis_title="Flowing  bottomhole  pressure (psi)")
    st.write(fig)

def fut_Wiggin():
    qomaxp=qo/(1-0.52*(Pwf/Pr)-0.48*((Pwf/Pr)**2))
    qomaxf=qomaxp*((0.15)*(Prf/Pr)+0.84*((Prf/Pr)**2))
    st.write("Future maximum oil flowrate = ",qomaxf," bbl/day")
    Flowing_pressure=np.arange(Prf,0-(Prf/20),-Prf/20)
    f_p=Flowing_pressure
    flow=[]
    for i in f_p:
        Q=qomaxf*(1-0.52*(i/Prf)-0.48*((i/Prf)**2))
        flow.append(Q)    
    import plotly.express as px
    fig = px.scatter(x=flow,y=f_p)
    fig.update_layout(xaxis_title="Flowrate (bbl/day)", yaxis_title="Flowing  bottomhole  pressure (psi)")
    st.write(fig)

st.sidebar.write("** For future oil well performance**")
Prf=st.sidebar.number_input("Future Reservoir Pressure",min_value=float(0), max_value=float(10000000000000000000),step=0.5,value=float(2200))
future=["Vogel's first","Vogel's second (Fetkovich)","Wiggin's"]
fut=st.sidebar.radio("Select the method",future)

butten1 = st.sidebar.button('Apply')
if butten1:
    call()
    if fut=="Vogel's first":
        st.write("**Prediction of future IPRs**")
        st.write("** Using Vogel's first method**")
        if Pr==Pb:
            First_Approximation_Method()
        else:
            st.write("Vogel's first only works if initial reservoir pressure is equal to the bubble point pressure")
    if fut=="Vogel's second (Fetkovich)":
        st.write("**Prediction of future IPRs**")
        st.write("** Using Vogel's second (Fetkovich) method**")
        if Pr==Pb:
            Second_Approximation_Method()
        else:
            st.write("Vogel's first only works if initial reservoir pressure is equal to the bubble point pressure")     
    if fut=="Wiggin's":
        st.write("** Using Wiggin's method**")
        st.write("**Prediction of future IPRs**")
        fut_Wiggin()
