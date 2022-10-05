import pickle
load_model=pickle.load(open('https://github.com/Biju1993/CHENNAI-HOUSE-PRICE-PRDICTION/blob/main/xgd.sav', 'rb'))
q1,q2=st.columns(2)
q1.video("https://www.youtube.com/watch?v=5IvQ3fYKnfM")
q2.image("data:image/png;base64,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")
f1=st.selectbox("SELECT AREA",['KARAPAKKAM','ANNA NAGAR', 'ADYAR', 'CHROMPET', 'KK NAGAR', 'T NAGAR','VELACHERY'])
f11q={'KARAPAKKAM': 0, 'ANNA NAGAR': 5, 'ADYAR': 1, 'CHROMPET': 2, 'KK NAGAR': 4, 'T NAGAR': 6, 'VELACHERY': 3}
q = pd.DataFrame(
    [[12.9191,80.2300],
     [13.0012,80.2565],
     [12.9516,80.1462],
     [13.0410,80.1994],
     [13.0418,80.2341],
     [13.0850,80.2101],
     [12.9815, 80.2180]],
    columns=['lat', 'lon'])
st.map(q.loc[[f11q.get(f1)]])
f2=st.number_input("ENTER AREA IN SQFT")
c1,c2=st.columns(2)
f3=c1.radio("NO OF BEDROOM",[1,2,3,4])
f4=c2.radio("NO OF BATHROOM",[1,2])
f5=st.slider("NO OF ROOM",min_value=1,max_value=6,step=1)
f6=st.radio("PARKING FACILTY AVAILABILITY",["YES","NO"])
f7=st.date_input("SELECT DATE OF BUILD")
f8=st.selectbox("UTILITY AVAILABILITY",['AllPub', 'ELO', 'NoSeWa'])
f9=st.selectbox("MZZONE",['A', 'C', 'I', 'RH', 'RL', 'RM'])
f10=st.selectbox("STREET",['Gravel', 'No Access', 'Paved'])
f11=st.selectbox("BUILDING TYPE",['Commercial', 'HOUSE', 'OTHERS'])
f81={'AllPub': 2, 'ELO': 0, 'NoSeWa': 1}
f91={'A': 0, 'C': 1, 'I': 2, 'RH': 3, 'RL': 4, 'RM': 5}
f101={'Gravel':2, 'No Access':0, 'Paved':1}
f111={'Commercial':2, 'House':0, 'Others':1}
st.checkbox("I ACCEPT TERMS AND CONDITIONS ")
if st.button("CLICK HERE TO PREDICT THE REAL PRICE VALUE"):
    st.header(*load_model([[f11q.get(f1),
                           f2,
                           f3,
                           f4,
                           f5,
                           0 if f6=="NO" else 1,
                           (pd.Timestamp.today().date()-f7).days,
                           f81.get(f8),
                           f91.get(f9),
                           1 if f101.get(f10)==2 else 0,
                           1 if f101.get(f10)== 0 else 0,
                           1 if f101.get(f10)==1 else 0,
                           1 if f111.get(f11)==2 else 0,
                           1 if f111.get(f11)==0 else 0,
                           1 if f111.get(f11)==1 else 0]]))
    st.write("THE PREDICTED PRICE OF THE XGBOOST MODEL.... ")
    st.markdown(':moon:')
    st.balloons()
