import streamlit as st
from Train import predict

@st.cache_data(persist=True)
def load_data():
    pass


@st.cache_data(persist=True)
def predict_stroke(X, y, features):
    pass

def app(df, X, y):
    data = load_data()
    st.title("Cerebrovascular Forecasting using Machine Learning")
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Tree Classifier</b> for Brain Stroke Detection.
            </p>
        """, unsafe_allow_html=True)
    
    

    st.markdown("""General Convention:
    \n 0 -> Absent or False
    \n 1 -> Present or True\n 
    
    \nWork types:\n
    0 -> Children 
    1 -> Government Job 
    2 -> Private Job 
    3 -> Self-employed
    4 -> Unemployed

    \nResidence Type:\n 
    1 -> Urban
    0 -> Rural
    """)
    
    
    # Take input of features from the user.
    A = st.slider("Gender", int(df["gender"].min()), int(df["gender"].max()))
    B = st.slider("Age", int(df["age"].min()), int(df["age"].max()))
    C= st.slider("Hypertension", int(df["hypertension"].min()), int(df["hypertension"].max()))
    D = st.slider("Heart Diseases", int(df["heart_disease"].min()), int(df["heart_disease"].max()))
    E = st.slider("Married", int(df["ever_married"].min()), int(df["ever_married"].max()))
    F = st.slider("Work Type", int(df["work_type"].min()), int(df["work_type"].max()))
    G = st.slider("Residence type", int(df["Residence_type"].min()), int(df["Residence_type"].max()))
    H = st.slider("Average Glucose Level", int(df["avg_glucose_level"].min()), int(df["avg_glucose_level"].max()))
    I = st.slider("Basal Metabolic Index (BMI)", int(df["bmi"].min()), int(df["bmi"].max()))
    
    features = [A,B,C,D,E,F,G,H,I]
    if st.button("Predict"):
        prediction, score = predict(X, y, features)
        score = score
        st.info("Predicted Sucessfully...")
        if (prediction == 1):
            st.warning("The person is prone to experience a Brain Stroke!!")
        else:
            st.success("The person has relatively less probability of Brain Stroke")
        #st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")

