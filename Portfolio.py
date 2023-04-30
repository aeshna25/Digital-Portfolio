from pathlib import Path
import streamlit as st
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "mains.css"
resume_file = current_dir / "assests" / "Aeshna Gupta Data analyst Resume.pdf"
profile_pic = current_dir / "assests" / "profile-pic.png"


# general settings
PAGE_TITLE= 'Digital CV | Aeshna Gupta'
PAGE_ICON = ':wave:'
NAME = 'Aeshna Gupta'
DESCRIPTION = 'Senior Data Analyst| Dell Technologies, assisting sales and marketing by supporting data-dirver decision-making'

EMAIL= 'aeshnaagg@gmail.com'
SOCIAL_MEDIA ={
                'LinkedIn': 'https://linkedin.com/in/aeshna-gupta',
                'Github':'https://github.com/aeshna25'  ,
                'Medium':'https://medium.com/@aeshnagupta',
                'Business Project': 'https://aeshna25.github.io/Aeshna_Portfolio/'

}

PROJECTS= {
            "💻 Customer acquistion and profiling using Segmentation and PCA": "https://github.com/aeshna25/Customer-acquisition",
            "💻 Buyer Prediction using Deep learning techniques":"https://github.com/aeshna25/Buyer-Prediction-using-Deep-learning",
            "💻 Web scraping using Selenium and BeautifulSoup on Naukri job site":'https://github.com/aeshna25/Web-scrapping',
            # "💻 Credit Card Fraud Prediction using AutoML , S3 bucket and Airflow",
            "💻 Linkedin connections analysis": 'https://github.com/aeshna25/LinkedIn-Connnections-Analysis',
            "💻 Data analysis and modeling": 'https://eda-and-modeling-ap.streamlit.app/'
}

st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)


#load css, pdf and pic
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file,'rb') as pdf_file:
    PDFbyte= pdf_file.read()
profile_pic=Image.open(profile_pic)


#Hero section
col1,col2= st.columns(2,gap='small')
with col1:
    st.image(profile_pic,width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
    label="Download Resume",
    data = PDFbyte,
    file_name = 'Aeshna Gupta Resume',
    mime= 'application/octet-stream'
    )
    st.write("📭",EMAIL)

#social links
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


#experience 
st.write('#')
st.subheader('Experience and Qualifications')
st.write("---")
st.write(""" 
- ✔️ 2.5 Years experience extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python , SQL and Excel
- ✔️ Good understanding of statistical principals and their respective applications
- ✔️ Experience in presenting analysis to non-technical audience
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks

""")

#skills
st.write('#')
st.subheader("Hard Skills")
st.write("---")
st.write(
"""
- 💻 Programming: Python(Scikit-learn, Pandas), SQL
- 🖌️ Data Visualization: Plotly, Streamlit, Ms Excel
- 📚 Modeling: AutoML, Random forest, Kmean clustering, PCA, linear regression, decision tress
- 💾 Database: Teradata, SSMS, SSIS
- 📠 Other skills: Research, Reports and Forecast, Quantitative Market analysis, Communication, Decision analysis, Critical thinking, predictive analysis
"""
)

#work history
st.write('#')
st.subheader("Work History")
st.write("---")

#job1
st.write("👩‍💻","Senior Data analyst| Dell Technologies")
st.write("05/2022- Present")

st.write("""
 - 💭 Gathered and sorted quantitative data for the development of customer relationship management (CRM) systems and databases
 - 💭 Developed NLP model to assist the sales team in understanding order cancellation reasons 
 - 💭 Developed and implemented statistical data analysis to increase customer acquisition in the past quarter 
 - 💭 Created SSIS packages & to extract data from multiple databases 
 - 💭 Presented data models to top executives to demonstrate financial performance and predict growth

""")

# job2
st.write("👩‍💻","Software Engineer | Dell Technologies")
st.write("07/2020- 05/2022")

st.write("""
 - 💭 Building a customer loyalty- LTV and segmentation using B2B customer online browsing behaviour, purchase pattern & customer feedback (qualitative & quantitative)
 - 💭 Analyzed and produced KPI reports allowing to monitor feedback and revenue of customers(channel, affiliated, alliance) closely
 - 💭 Design and build Text analysis dashboard using unsupervised models LDA, NMF to help stakeholders understand customers through their verbatims
 - 💭 Developed NLP models using Python to uncover topics, sentiments, emotions, trend in unstructured customer remarks.
 - 💭 Increased the customer footfall on the tool by 45 percent in 6 months
""")
# internship
st.write("👩‍💻","Research Intern | National University of Singapore")
st.write("06/2019- 07/2019")

st.write("""
 - 💭 Global Academic Internship Program (GAIP) in association with Hewlett Packard Enterprise (HPE) organized an internship for Big data analysis, during the course I was trained in  Hadoop, Neural Network and Machine learning. 

""")

#achievements
st.write('#')
st.subheader("Achievements")
st.write("---")
st.write(
"""
- 📁 Awarded the "Leadership Award" for my work on Topic modelling dashboard (07/2021)
- 📁 Stood 3rd as a team In Dell CMR competition (10/2021)
- 📁 Mentored candidates in the field of AI and created a recommendation system as part of ACM chapters in college

"""
)

# --- Schooling ---
st.write('#')
st.subheader("Education")
st.write("---")

st.write("👩‍💻","B.tech in Information Technology | Indira Gandhi Delhi Technical University for Women, Delhi")
st.write("08/2016- 05/2020")
st.write("CGPA: 7.6")

st.write("👩‍💻","12th | Holy Angels' Convent School")
st.write("04/2014- 04/2015")
st.write("CGPA: 9.3")


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

# --- PURSUITS & INTERESTS---
st.write('\n')
st.subheader("Pursuits & Interests")
st.write("---")

columns = st.columns(4)
columns[0].button('Volunteering')
columns[1].button('Photography')
columns[2].button('Blogging')
columns[3].button('Digital Illustration')


# for deployment:
#1. Requirement.txt: pip install pipreqs 
# 2. python -m pipreqs.pipreqs --encoding=utf8 "<location of project folder>"
# 3. upload all folders and files to github
# 4. Go to streamlit profile and follow steps for streamlit deployment
