import streamlit as st

st.write("""
# Hello All
""")

entity=["Length","Density","Flowrate","Volume","Pressure"]
main = st.sidebar.radio("select a unit for entity", entity)

if main=="Length":
    st.markdown('** Length Conversation**')
    i=st.sidebar.number_input("Add the value to be converted for length",min_value=float(0), max_value=float(1000000000000000000000000000000000),step=0.5)
    i=float(i)
    length=["m","cm","feet","inch"]
    unit = st.sidebar.radio("select a unit for length", length)

    if unit=="m":
        st.write(str(i) + " " + unit +" = " ,str(round((100*i),4)) +" cm." )
        st.write(str(i) + " " + unit +" = " ,str(round((3.28084*i),4)) +" feet." )
        st.write(str(i) + " " + unit +" = " ,str(round((39.3701*i),4)) +" inch." )
    if unit=="cm":
        st.write(str(i) + " " + unit +" = " ,str(round((0.01*i),4)) +" m." )
        st.write(str(i) + " " + unit +" = " ,str(round((0.0328084*i),4)) +" feet." )
        st.write(str(i) + " " + unit +" = " ,str(round((0.393701*i),4)) +" inch." )
    if unit=="feet":
        st.write(str(i) + " " + unit +" = " ,str(round((0.3048*i),4)) +" m." )
        st.write(str(i) + " " + unit +" = " ,str(round((30.48*i),4)) +" cm." )
        st.write(str(i) + " " + unit +" = " ,str(round((12*i),4)) +" inch." )
    elif unit=="inch":
        st.write(str(i) + " " + unit +" = " ,str(round((0.0254*i),4)) +" m." )
        st.write(str(i) + " " + unit +" = " ,str(round((2.54*i),4)) +" cm." )
        st.write(str(i) + " " + unit +" = " ,str(round((12*i),4)) +" feet." )


if main=="Density":
    st.markdown('**Density Conversation**')
    j=st.sidebar.number_input("Add the value to be converted for density ",min_value=float(0), max_value=float(1000000000000000000000000000000),step=0.5)
    j=float(j)
    density=["g/cc","kg/m3","ppg","lb/ft3"]
    unit1 = st.sidebar.radio("select a unit for density", density)

    if unit1=="g/cc":
        st.write(str(j) + " " + unit1 + " = " ,str(round((1000*j),4)) +" kg/m3." )
        st.write(str(j) + " " + unit1 + " = " ,str(round((8.35*j),4)) +" ppg." )
        st.write(str(j) + " " + unit1 + " = " ,str(round((62.428*j),4)) +" lb/ft3." )
    if unit1=="kg/m3":
        st.write(str(j) + " " + unit1 + " = " ,str(round((0.001*j),4)) +" g/cc." )
        st.write(str(j) + " " + unit1 + " = " ,str(round((0.00835*j),4)) +" ppg." )
        st.write(str(j) + " " + unit1 + " = " ,str(round((0.062428*j),4)) +" lb/ft3." )
    if unit1=="ppg":
        st.write(str(j) + " " + unit1 + " = " ,str(round(((1/8.35)*j),4)) +" g/cc." )
        st.write(str(j) + " " + unit1 + " = " ,str(round((119.760479*j),4)) +" kg/m3." )
        st.write(str(j) + " " + unit1 + " = " ,str(round((7.4764*j),4)) +" lb/ft3." )
    elif unit1=="lb/ft3":
        st.write(str(j) + " " + unit1 + " = " ,str(round((0.016018*j),4)) +" g/cc." )
        st.write(str(j) + " " + unit1 + " = " ,str(round((16.0184533*j),4)) +" kg/m3." )
        st.write(str(j) + " " + unit1 + " = " ,str(round((0.133754*j),4)) +" ppg." )




if main=="Flowrate":
    st.markdown('**Flowrate Conversation**')  
    k=st.sidebar.number_input("Add the value to be converted for flowrate",min_value=float(0), max_value=float(100000000000000000000000000000),step=0.5)
    k=float(k)
    flowrate=["bbl/day","ton/day","MMbbl/year","MMton/year"]
    unit2 = st.sidebar.radio("select a unit for flowrate", flowrate)


    if unit2=="bbl/day":
        st.write(str(k) + " " + unit2 + " = " ,str(round((0.136425648*k),4)) +" ton/day." )
        st.write(str(k) + " " + unit2 + " = " ,str(round(((365*(10**(-6)))*k),4)) +" MMbbl/year." )
        st.write(str(k) + " " + unit2 + " = " ,str(round((49.7953615*(10**(-6))*k),4)) +" MMton/year." )
    if unit2=="ton/day":
        st.write(str(k) + " " + unit2 + " = " ,str(round((7.33*k),4)) +" bbl/day." )
        st.write(str(k) + " " + unit2 + " = " ,str(round((2675.45*(10**(-6))*k),4)) +" MMbbl/year." )
        st.write(str(k) + " " + unit2 + " = " ,str(round(((365*(10**(-6)))*k),4)) +" MMton/year." )
    if unit2=="MMbbl/year":
        st.write(str(k) + " " + unit2 +" = " ,str(round(((1/365)*(10**(6))*k),4)) +" bbl/day." )
        st.write(str(k) + " " + unit2 +" = " ,str(round(((1/2675.45)*(10**(6))*k),4)) +" ton/day." )
        st.write(str(k) + " " + unit2 +" = " ,str(round(((365/2675.45)*k),4)) +" MMton/year." )
    elif unit2=="MMton/year":
        st.write(str(k) + " " + unit2 +" = " ,str(round(((7.33/365)*(10**(6))*k),4)) +" bbl/day." )
        st.write(str(k) + " " + unit2 +" = " ,str(round(((1/365)*(10**(6))*k),4)) +" ton/day." )
        st.write(str(k) + " " + unit2 +" = " ,str(round(((2675.45/365)*k),4)) +" MMbbl/year." )

if main=="Volume":
    st.markdown('**Volume Conversation**')
    i1=st.sidebar.number_input("Add the value to be converted for volume",min_value=float(0), max_value=float(1000000000000000000000000000000000),step=0.5)
    i1=float(i1)
    volume=["cm3","m3","bbl","gallon","ft3","liter"]
    unit3 = st.sidebar.radio("select a unit for volume", volume)

    if unit3=="cm3":
        st.write(str(i1) + " " + unit3 +" = " ,str(round(((1/1000000)*i1),6)) +" m3." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round(((6.28981/1000000)*i1),6)) +" bbl." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round(((0.000264172)*i1),6)) +" gallon." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round(((3.5315/100000)*i1),6)) +" ft3." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round(((1/1000)*i1),6)) +" liter." )
    if unit3=="m3":
        st.write(str(i1) + " " + unit3 +" = " ,str(round((1000000*i1),4)) +" cm3." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((6.29*i1),4)) +" bbl." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((264.172*i1),4)) +" gallon." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((35.3147*i1),4)) +" ft3." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((1000*i1),4)) +" liter." )
    if unit3=="bbl":
        st.write(str(i1) + " " + unit3 +" = " ,str(round((158987*i1),4)) +" cm3." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((0.16*i1),6)) +" m3." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((42*i1),4)) +" gallon." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((5.61458*i1),4)) +" ft3." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((158.987*i1),4)) +" liter." )
    if unit3=="gallon":
        st.write(str(i1) + " " + unit3 +" = " ,str(round((3785.41*i1),4)) +" cm3." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((0.00378541*i1),6)) +" m3." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((0.0238095*i1),6)) +" bbl." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((0.133681*i1),6)) +" ft3." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((3.78541*i1),4)) +" liter." )
    if unit3=="ft3":
        st.write(str(i1) + " " + unit3 +" = " ,str(round((28316.8*i1),4)) +" cm3." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((0.0283168*i1),6)) +" m3." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((0.178108*i1),6)) +" bbl." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((7.48052*i1),4)) +" gallon." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((28.3168*i1),4)) +" liter." )
    if unit3=="liter":
        st.write(str(i1) + " " + unit3 +" = " ,str(round((1000*i1),4)) +" cm3." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round(((1/1000)*i1),6)) +" m3." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((0.006289*i1),6)) +" bbl." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((0.264172*i1),4)) +" gallon." )
        st.write(str(i1) + " " + unit3 +" = " ,str(round((0.0353147*i1),6)) +" ft3." )

elif main=="Pressure":
    st.markdown('**Pressure Conversation**')
    i2=st.sidebar.number_input("Add the value to be converted for pressure",min_value=float(0), max_value=float(1000000000000000000000000000000000),step=0.5)
    i2=float(i2)
    pressure=["Pa","bar","Atm","psi","torr"]
    unit4 = st.sidebar.radio("select a unit for pressure", pressure)

    if unit4=="Pa":
        st.write(str(i2) + " " + unit4 +" = " ,str(round(((1/100000)*i2),6)) +" bar." )
        st.write(str(i2) + " " + unit4 +" = " ,str(round(((9.869/1000000)*i2),6)) +" Atm." )
        st.write(str(i2) + " " + unit4 +" = " ,str(round((0.000145038*i2),6)) +" psi." )
        st.write(str(i2) + " " + unit4 +" = " ,str(round((0.00750062*i2),6)) +" psi." )
    if unit4=="bar":
        st.write(str(i2) + " " + unit4 +" = " ,str(round((100000*i2),6)) +" Pa." )
        st.write(str(i2) + " " + unit4 +" = " ,str(round((0.986923*i2),6)) +" Atm." )
        st.write(str(i2) + " " + unit4 +" = " ,str(round((14.5038*i2),6)) +" psi." )
        st.write(str(i2) + " " + unit4 +" = " ,str(round((750.062*i2),6)) +" torr." )
    if unit4=="Atm":
        st.write(str(i2) + " " + unit4 +" = " ,str(round((101325*i2),6)) +" Pa." )
        st.write(str(i2) + " " + unit4 +" = " ,str(round((1.01325*i2),6)) +" bar." )
        st.write(str(i2) + " " + unit4 +" = " ,str(round((14.6959*i2),6)) +" psi." )
        st.write(str(i2) + " " + unit4 +" = " ,str(round((760*i2),6)) +" torr." )
    if unit4=="psi":
        st.write(str(i2) + " " + unit4 +" = " ,str(round((6894.76*i2),6)) +" Pa." )
        st.write(str(i2) + " " + unit4 +" = " ,str(round((0.0689476*i2),6)) +" bar." )
        st.write(str(i2) + " " + unit4 +" = " ,str(round((0.068046*i2),6)) +" Atm." )
        st.write(str(i2) + " " + unit4 +" = " ,str(round((51.7149*i2),6)) +" torr." )
    elif unit4=="tor":
        st.write(str(i2) + " " + unit4 +" = " ,str(round((133.322*i2),6)) +" Pa." )
        st.write(str(i2) + " " + unit4 +" = " ,str(round((0.00133322*i2),6)) +" bar." )
        st.write(str(i2) + " " + unit4 +" = " ,str(round((0.00131579*i2),6)) +" Atm." )