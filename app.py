import streamlit as st
import pandas as pd

# Wczytanie danych mentorów
mentors = pd.DataFrame({
    'mentor_id': [1, 2, 3, 4],
    'name': ['Anna Kowalska', 'Jan Nowak', 'Ewa Wiśniewska', 'Tomasz Zieliński'],
    'skills': ['Python;Data Science;Machine Learning', 'JavaScript;React;Web Development', 
               'Project Management;Agile', 'DevOps;AWS;CI/CD'],
    'location': ['Warszawa', 'Kraków', 'Szczecin', 'Gdańsk'],
    'experience': [5, 3, 10, 7],
    'availability': ['poniedziałek;wtorek', 'środa;czwartek', 'wtorek;piątek', 'poniedziałek;środa']
})

# Formularz dla Mentee
st.title("Znajdź swojego mentora")

skills_input = st.text_input("Jakie umiejętności chcesz rozwijać? (np. Python, JavaScript)")
location_input = st.selectbox("Wybierz lokalizację", ["Warszawa", "Kraków", "Szczecin", "Gdańsk", "Zdalnie"])
availability_input = st.multiselect("Wybierz preferowane dni spotkań", ["poniedziałek", "wtorek", "środa", "czwartek", "piątek"])
experience_input = st.slider("Minimalne doświadczenie mentora (w latach)", 0, 10, 2)

# Dopasowanie mentorów
def match_mentors(mentors, skills_input, location_input, availability_input, experience_input):
    filtered_mentors = mentors[mentors['skills'].str.contains(skills_input, case=False, na=False)]
    
    if location_input != "Zdalnie":
        filtered_mentors = filtered_mentors[filtered_mentors['location'] == location_input]

    for day in availability_input:
        filtered_mentors = filtered_mentors[filtered_mentors['availability'].str.contains(day, case=False, na=False)]
    
    filtered_mentors = filtered_mentors[filtered_mentors['experience'] >= experience_input]
    
    return filtered_mentors

# Wywołanie funkcji dopasowania po kliknięciu przycisku
if st.button("Szukaj mentora"):
    matched_mentors = match_mentors(mentors, skills_input, location_input, availability_input, experience_input)
    
    if not matched_mentors.empty:
        st.write("Znalezieni mentorzy:")
        st.dataframe(matched_mentors)
    else:
        st.write("Nie znaleziono mentorów spełniających kryteria.")
