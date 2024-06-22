import pickle
import streamlit as st
from streamlit_option_menu import option_menu





# loading the saved models
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
cancer_disease_model = pickle.load(open('cancer_diseases_model.sav', 'rb'))
parkinson_disease_model = pickle.load(open('perkinson_disease_model.sav', 'rb'))






# sidebar for navigation

with st.sidebar:

    

    selected = option_menu('MULTIPLE DISEASE PREDICTION SYSTEM',

                          

                          ['HOME',
                          'HEART DISEASE PREDICTION',
                          'CANCER DISEASE PREDICTION',
                          'PARKINSON DISEASE PREDICTION',
                          'CONCLUSION'],

                          

                          default_index=0)
    st.success('version-1.0.0')
    st.error('application is developed only for project purpose. Not for serious medical concern use')

    

    


 




# (1) Heart Disease Prediction Page

if (selected == 'HEART DISEASE PREDICTION'):
    st.image("heart.jpeg",use_column_width=True)

    # page title

    st.title('Heart Disease Prediction using ML')
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain types')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholestoral in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting Electrocardiographic results')
    thalach = st.text_input('Maximum Heart Rate achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of the peak exercise ST segment')
    ca = st.text_input('Major vessels colored by flourosopy')
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
      if any(not x for x in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
        st.error("Please fill all the details.")
      else:
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                          

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person is not having  any heart disease'
        
        st.success(heart_diagnosis)



        

    
    st.image("images (1).jpg", caption="Mapping View Of Heart Disease In India", use_column_width=True)
    st.image("images(2).jpeg", caption="Statistical Chart Of Age-Group vs First Time Heart Disease", use_column_width=True)
    st.image("image (3).jpeg", caption="Statistical Chart Of Gender vs First Time Heart Disease", use_column_width=True)










# (2) Cancer Disease Prediction Page

if (selected == 'CANCER DISEASE PREDICTION'):

    # page title
    st.image("Cancer.jpeg",use_column_width=True)

    st.title('Cancer Disease Prediction using ML')
    radius_mea = st.text_input('radius_mea')
    texture_mea = st.text_input('texture_mea')
    perimeter_mea = st.text_input('perimeter_mea')
    area_mea = st.text_input('area_mea')
    smoothness_mea = st.text_input('smoothness_mea')

    # code for Prediction
    Cancer_diagnosis = ''

    # creating a button for Prediction

    if st.button('Cancer Disease Test Result'):
        if any(not x for x in [radius_mea,texture_mea,perimeter_mea,area_mea,smoothness_mea]):
            st.error("Please fill all the details.")

        else:
            cancer_prediction = cancer_disease_model.predict([[radius_mea,texture_mea,perimeter_mea,area_mea,smoothness_mea]])
            if (cancer_prediction[0] == 1):
                Cancer_diagnosis = 'The person may not have any cancer disease(B)'
            else:
                Cancer_diagnosis = 'The person may have any cancer disease(M)'
            st.success(Cancer_diagnosis)
                


        

    
    st.image("image (4).jpeg", caption="Mapping View Of Cancer Disease In India", use_column_width=True)
    st.image("images(5).jpg", caption="Statistical Chart Of Age-Group vs First Time Cancer Disease", use_column_width=True)
    st.image("image (6).jpeg", caption="Statistical Chart Of Gender vs First Time Cancer Disease", use_column_width=True)

      








# (3) Parkinson Disease Prediction Page

if (selected == 'PARKINSON DISEASE PREDICTION'):

    # page title
    st.image("Parkinson.jpeg",use_column_width=True)

    st.title('Parkinson Disease Prediction using ML')
    MDVPFo = st.text_input('MDVP:Fo(Hz)')
    MDVPFhi = st.text_input('MDVP:Fhi(Hz)')
    MDVPFlo = st.text_input('MDVP:Flo(Hz)')
    MDVPJitter = st.text_input('MDVP:Jitter(%)')
    MDVPJitte = st.text_input('MDVP:Jitter(Abs)')
    MDVPRAP = st.text_input('MDVP:RAP')
    MDVPPPQ = st.text_input('MDVP:PPQ')
    JitterDD = st.text_input('Jitter:DD')
    MDVPShimmer = st.text_input('MDVP:Shimmer')
    MDVPShimme = st.text_input('MDVP:Shimmer(dB)')
    
    
    # code for Prediction
    parkinson_diagnosis = ''

    # creating a button for Prediction

    if st.button('Parkinson Disease Test Result'):
        if any(not x for x in [MDVPFo,MDVPFhi,MDVPFlo,MDVPJitter,MDVPJitte,MDVPRAP,MDVPPPQ,JitterDD,MDVPShimmer,MDVPShimme]):
            st.error("Please fill all the details.")
        else:
            parkinson_prediction = parkinson_disease_model.predict([[MDVPFo,MDVPFhi,MDVPFlo,MDVPJitter,MDVPJitte,MDVPRAP,MDVPPPQ,JitterDD,MDVPShimmer,MDVPShimme]])
            if (parkinson_prediction[0] == 1):
                parkinson_diagnosis = 'The person is not having parkinson disease'
            else:
                parkinson_diagnosis = 'The person have any Parkinson disease'
            st.success(parkinson_diagnosis)
        


                                  

    st.image("images (7).jpeg", caption="Statistical View Of Parkinson's Disease In India", use_column_width=True)
    st.image("images (8).png", caption="Statistical Chart Of Age-Group vs First Time Parkinson's Disease", use_column_width=True)
    st.image("images (9).jpg", caption="Statistical Chart Of Gender vs First Time Parkinson's Disease", use_column_width=True)






#coding for Home page.....
if (selected == 'HOME'):
    st.title(' MULTIPLE DISEASE PREDICTION SYSTEM USING MACHINE LEARNING')
    st.image("disease.jpeg",use_column_width=True)
    st.write('Experience our distinguished health hub, where advanced machine learning technology intersects with proactive wellness. Our platform leverages machine learning algorithms to deliver personalized disease prediction, fitness tracking, and comprehensive wellness resources, facilitating your pursuit of optimal health. Equipped with data-driven insights and decision-making tools, we endeavor to cultivate a community of health-conscious individuals committed to enhancing their well-being. Step into our realm and embark on a journey toward transforming your residence into a sanctuary of vitality and longevity. Welcome to the premier destination for holistic health management powered by machine learning.')
    
    st.title('Heart Disease Problem in India')
    st.image("home_heart.jpeg",use_column_width=True)
    # Heart Disease Overview
    st.write("**Heart Disease Overview:**")
    st.write("Heart disease, also known as cardiovascular disease, refers to a range of conditions that affect the heart and blood vessels, often leading to various complications. It is a leading cause of death worldwide, encompassing conditions such as coronary artery disease, heart failure, arrhythmias, and heart valve problems.")
    # Types of Heart Disease
    st.write("**Types of Heart Disease:**")
    st.write("1. **Coronary Artery Disease (CAD):** Occurs when plaque builds up in the coronary arteries, restricting blood flow to the heart muscle.")
    st.write("2. **Heart Failure:** A condition where the heart cannot pump enough blood to meet the body's needs.")
    st.write("3. **Arrhythmias:** Irregular heartbeats, including tachycardia (fast heartbeat) and bradycardia (slow heartbeat).")
    st.write("4. **Heart Valve Problems:** Conditions affecting the valves that regulate blood flow within the heart, such as stenosis (narrowing) or regurgitation (leakage).")
    #Symptoms of Heart Disease
    st.write("**Symptoms of Heart Disease:**")
    st.write("1. **Chest Pain or Discomfort:** Often described as tightness, pressure, squeezing, or pain in the chest.")
    st.write("2. **Shortness of Breath:** Difficulty breathing, especially during physical activity or when lying down.")
    st.write("3. **Fatigue:** Feeling tired or weak, even with minimal exertion.")
    st.write("4. **Swelling:** Fluid retention, leading to swelling in the legs, ankles, feet, or abdomen.")
    st.write("5. **Dizziness or Lightheadedness:** Feeling faint or dizzy, especially upon standing up quickly.")
    st.write("6. **Irregular Heartbeat:** Sensation of fluttering or palpitations in the chest.")
    st.write("7. **Nausea or Indigestion:** Some people may experience stomach discomfort, nausea, or vomiting.")
    # Treatment of Heart Disease
    st.write("**Treatment of Heart Disease:**")
    st.write("1. **Medications:** Depending on the type of heart disease, medications may be prescribed to manage symptoms, control blood pressure, lower cholesterol levels, regulate heart rhythm, or prevent blood clots.")
    st.write("2. **Lifestyle Changes:** Adopting a heart-healthy lifestyle can significantly improve heart health. This includes maintaining a balanced diet, engaging in regular exercise, quitting smoking, managing stress, and limiting alcohol intake.")
    st.write("3. **Medical Procedures:** In more severe cases, medical procedures may be necessary. These can include angioplasty and stenting to open blocked arteries, coronary artery bypass surgery to reroute blood flow around blockages, valve repair or replacement surgery, or implantation of devices such as pacemakers or defibrillators.")
    st.write("4. **Cardiac Rehabilitation:** A structured program involving exercise training, education, and counseling to help individuals recover from heart-related events and improve their overall cardiovascular health.")
    st.write("Early detection, prompt treatment, and ongoing management are essential in effectively managing heart disease and reducing the risk of complications. Regular check-ups with a healthcare provider are crucial for monitoring heart health and addressing any concerns.")



    st.title(' Cancer Disease Problem in India')
    st.image("home_cancer.jpeg",use_column_width=True)
    # Cancer Disease Overview
    st.write("**Cancer Disease Overview:**")
    st.write("Cancer is a group of diseases characterized by the uncontrolled growth and spread of abnormal cells. It can affect various organs and tissues in the body, leading to a range of symptoms and complications.")

    # Types of Cancer
    st.write("**Types of Cancer:**")
    st.write("1. **Breast Cancer:** Affects the breast tissue and is one of the most common cancers among women.")
    st.write("2. **Lung Cancer:** Develops in the lungs and is often associated with smoking or exposure to carcinogens.")
    st.write("3. **Prostate Cancer:** Occurs in the prostate gland and is one of the most common cancers among men.")
    st.write("4. **Colorectal Cancer:** Affects the colon or rectum and can develop from precancerous polyps.")
    st.write("5. **Skin Cancer:** Develops in the skin cells and is often caused by exposure to ultraviolet (UV) radiation from the sun or tanning beds.")
    st.write("6. **Leukemia:** Affects the blood and bone marrow, leading to the overproduction of abnormal white blood cells.")
    st.write("7. **Lymphoma:** Affects the lymphatic system, which is part of the body's immune system, and includes Hodgkin lymphoma and non-Hodgkin lymphoma.")
    st.write("8. **Brain Cancer:** Develops in the brain or spinal cord and can cause symptoms such as headaches, seizures, and neurological changes.")

    # Symptoms of Cancer
    st.write("**Symptoms of Cancer:**")
    st.write("1. **Unexplained Weight Loss:** Losing weight without trying can be a symptom of various types of cancer.")
    st.write("2. **Fatigue:** Feeling tired or weak, even with adequate rest and sleep.")
    st.write("3. **Persistent Pain:** Chronic pain that does not go away and may worsen over time.")
    st.write("4. **Changes in Bowel or Bladder Habits:** Including diarrhea, constipation, blood in the stool or urine, or changes in urination patterns.")
    st.write("5. **Unexplained Bruising or Bleeding:** Including easy bruising, frequent nosebleeds, or bleeding gums.")
    st.write("6. **Persistent Cough or Hoarseness:** Especially if accompanied by blood in the sputum or difficulty swallowing.")
    st.write("7. **Skin Changes:** Such as new moles or changes in the size, shape, or color of existing moles.")

    # Treatment of Cancer
    st.write("**Treatment of Cancer:**")
    st.write("1. **Surgery:** Removal of cancerous tumors or affected tissues through surgical procedures.")
    st.write("2. **Chemotherapy:** The use of drugs to kill cancer cells or prevent them from growing and spreading.")
    st.write("3. **Radiation Therapy:** Using high-energy beams to target and destroy cancer cells.")
    st.write("4. **Immunotherapy:** Stimulating the body's immune system to recognize and attack cancer cells.")
    st.write("5. **Targeted Therapy:** Drugs or other substances that specifically target cancer cells while minimizing damage to healthy cells.")
    st.write("6. **Hormone Therapy:** Blocking or inhibiting the production or action of hormones that promote cancer growth.")
    st.write("7. **Bone Marrow Transplantation:** Replacing diseased bone marrow with healthy stem cells to treat certain types of cancer.")

    st.write("Early detection, prompt treatment, and ongoing monitoring are crucial for improving cancer outcomes and quality of life. Regular screenings and consultations with healthcare professionals can aid in early diagnosis and appropriate management.")


    
    
    st.title('Parkinson Disease Problem in India')
    st.image("home_parkin.jpeg",use_column_width=True)
    

    #Parkinson's Disease Overview
    st.write("**Parkinson Disease Overview:**")
    st.write("Parkinson disease is a progressive neurological disorder that affects movement. It is characterized by tremors, stiffness, bradykinesia (slowness of movement), and impaired balance and coordination. Parkinson disease results from the loss of dopamine-producing cells in the brain.")

    #Symptoms of Parkinson's Disease
    st.write("**Symptoms of Parkinson's Disease:**")
    st.write("1. **Tremors:** Involuntary shaking of the hands, arms, legs, jaw, or face, typically at rest.")
    st.write("2. **Bradykinesia:** Slowness of movement, making simple tasks like buttoning a shirt or walking difficult.")
    st.write("3. **Stiffness:** Muscle rigidity, which can cause discomfort or pain and limit range of motion.")
    st.write("4. **Impaired Balance and Coordination:** Difficulty maintaining balance and coordinating movements, leading to falls or unsteady gait.")
    st.write("5. **Postural Instability:** Difficulty adjusting posture and maintaining an upright position, increasing the risk of falls.")
    st.write("6. **Speech and Swallowing Problems:** Soft or slurred speech, difficulty swallowing, or excessive drooling.")
    st.write("7. **Micrographia:** Handwriting becomes small and cramped.")
    st.write("8. **Masked Face:** Reduced facial expressions, giving the appearance of a 'masked' or expressionless face.")

    
    #Treatment of Parkinson's Disease
    st.write("**Treatment of Parkinson's Disease:**")
    st.write("1. **Medications:** Dopamine-replacement drugs, such as levodopa, can help alleviate motor symptoms. Other medications may be prescribed to manage non-motor symptoms, such as depression, sleep disturbances, or cognitive impairment.")
    st.write("2. **Deep Brain Stimulation (DBS):** A surgical procedure that involves implanting electrodes in the brain to deliver electrical stimulation, helping to regulate abnormal brain activity and reduce motor symptoms.")
    st.write("3. **Physical Therapy:** Exercises and techniques to improve mobility, flexibility, balance, and coordination.")
    st.write("4. **Speech Therapy:** Exercises to strengthen muscles involved in speech and swallowing, as well as strategies to improve communication.")
    st.write("5. **Occupational Therapy:** Techniques and adaptations to help individuals perform daily activities more independently and safely.")
    st.write("6. **Lifestyle Modifications:** Regular exercise, healthy diet, adequate sleep, stress management, and avoiding falls can help improve overall well-being and quality of life.")

    st.write("While there is currently no cure for Parkinson's disease, early diagnosis and comprehensive management can help control symptoms, slow disease progression, and improve quality of life. Regular follow-up with healthcare professionals, including neurologists and specialists in movement disorders, is essential for optimal care and support.")

    
    st.title('Conclusion')
    st.write("In summary, heart disease, cancer, and Parkinsons disease pose significant health risks worldwide. Early detection and personalized treatment are crucial for managing these conditions. Heart disease requires lifestyle changes and medication, while cancer demands diverse treatments like surgery and chemotherapy. Parkinson's disease necessitates medication, rehabilitation, and sometimes surgical interventions. Collaborative efforts among patients, caregivers, and healthcare providers are essential for improving outcomes and quality of life.")











# coding for CONCLUSION  page.....
if (selected == 'CONCLUSION'):
    st.title("LET'S TRY TO FIND OUT, HOW TO BE HEALTHY IN TODAY'S WORLD")
    st.image("health tips.jpeg",use_column_width=True)


    # Balanced Diet


    st.header("1. Balanced Diet:")
    st.write("Prioritize fresh fruits, vegetables, whole grains, lean proteins, and healthy fats, while minimizing processed foods and sugary beverages.")

    # Regular Exercise
    st.header("2. Regular Exercise:")
    st.write("Incorporate physical activity into your routine, such as walking, cycling, or yoga, aiming for at least 150 minutes of moderate-intensity exercise per week.")

    # Hydration
    st.header("3. Hydration:")
    st.write("Drink plenty of water throughout the day to stay hydrated, especially in hot climates.")

    # Stress Management
    st.header("4. Stress Management:")
    st.write("Practice relaxation techniques like meditation, deep breathing, or mindfulness to cope with daily stressors.")

    # Sleep
    st.header("5. Sleep:")
    st.write("Aim for 7-9 hours of quality sleep each night to support overall health and well-being.")

    # Regular Check-ups
    st.header("6. Regular Check-ups:")
    st.write("Schedule regular health check-ups with healthcare professionals for preventive screenings and early detection of any health issues.")

    # Vaccinations
    st.header("7. Vaccinations:")
    st.write("Stay up-to-date with recommended vaccinations to protect against infectious diseases prevalent in India.")

    # Hygiene
    st.header("8. Hygiene:")
    st.write("Practice good hygiene habits, including regular handwashing with soap and water, to prevent the spread of infections.")

    # Avoid Tobacco and Alcohol
    st.header("9. Avoid Tobacco and Alcohol:")
    st.write("Limit or avoid tobacco products and excessive alcohol consumption to reduce the risk of chronic diseases.")

    # Community Support
    st.header("10. Community Support:")
    st.write("Engage with local communities and support networks for social connections and mental well-being.")

    st.write("By adopting these healthy lifestyle habits and staying proactive about your health, you can navigate the challenges of modern living in India while promoting long-term wellness.")


