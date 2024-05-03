import streamlit as st
if 'Was_Pressed' not in st.session_state:
    st.session_state.Was_Pressed = False





st.title("Python Quiz")
st.write("Best of Luck!")


c=0
Q1= st.radio("Question 1. '%' is the symbol for commenting" , ["True", "False"], index=None)
if st.session_state.Was_Pressed: 
    if Q1== "False":
        st.write('Correct')
        c+=1
    else:
        st.write("Incorrect")
Q2= st.write("Question 2. Which of the following stores characters")
Q21=st.checkbox("Str")
Q22=st.checkbox("Dictonary")
Q23= st.checkbox("Int")
Q24= st.checkbox("bool")
if st.session_state.Was_Pressed:
    if Q21 and Q22:
        st.write('Correct')
        c+=1
    else:
        st.write('Incorrect')
Q3= st.multiselect(" Question 3. What are the steps of running a streamlit program (must have steps in order)", ['Deploy','in terminal type: streamlit run code_name.py', 'Write code', 'import streamlit as st', 'put code in Github repository'])
A= ['import streamlit as st','Write code', 'in terminal type: streamlit run code_name.py','put code in Github repository','Deploy']
if st.session_state.Was_Pressed:   
    if Q3==A:
        st.write('Correct')
        c+=1
    else:
        st.write('Incorrect')
Q4= st.radio("Question 4. What is the benefit of a while loop? " , ["It is more efficient", "You don't need a counter", "It cannot cause an infinate loop", "You don't need to know how many times the loop needs to run"], index=None)
if st.session_state.Was_Pressed:   
    if Q4== "You don't need to know how many times the loop needs to run":
        st.write('Correct')
        c+=1
    else:
        st.write("Incorrect")
Q5= st.radio("Question 5. What does the 'Continue' command do?" , ["Skips to the beginning of the code", "stops the loop", "Stops the code", "Makes the code crash"], index=None)
if st.session_state.Was_Pressed:
    if Q5=="Skips to the beginning of the code":
        st.write('Correct')
        c+=1
    else:
        st.write("Incorrect")




if st.button("Submit"):
    st.session_state.Was_Pressed = True
    st.rerun()
  
if st.session_state.Was_Pressed== True:
    st.write(f"Score: {c} out of 5")
    if c==5: 
        st.balloons()

