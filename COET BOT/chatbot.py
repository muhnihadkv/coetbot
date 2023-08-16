from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import spacy
spacy.load('en_core_web_sm')
# from spacy.lang.en import English
from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot('<b>COET BOT</b>')

# nlp = spacy.load("en_core_web_sm")

chatbot = ChatBot(
    'ChatBot for College Enquiry',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "Hi there, Welcome to COET! 👋 If you need any assistance, I'm always here.Go ahead and write the number of any query. 😃✨<b><br><br>  Which of the following user groups do you belong to? <br><br>1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br><br>",
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'   
) 
trainer = ListTrainer(chatbot)
#langFile = os.listdir('C:/Users/LENOVO/OneDrive/Desktop/coet/college-enquiry-chatbot/COET BOT/custom.yml')

# python app.py
# Training with Personal Ques & Ans 
conversation = [
"Hi",
"Helloo!",
"Hey",

"How are you?",
"I'm good.</br> <br>Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Great",
"Go ahead and write the number of any query. 😃✨ <br> 1.&emsp;Student's Section Enquiry.</br>2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"good",
"Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"fine",
"Go ahead and write the number of any query. 😃✨ <br> 2.&emsp;Faculty Section Enquiry. </br>3.&emsp;Parent's Section Enquiry.</br>4.&emsp;Visitor's Section Enquiry.</br>",

"Thank You",
"Your Welcome 😄",

"Thanks",
"Your Welcome 😄",

"Bye",
"Thank You for visiting!..",

"who made you ?",
"I created by Nihad , Akshay, Roshit ,Shibu",

"what is your name ?" ,
"I'm COET Bot",

"What do you do?",
"I am made to give Information about COET college.",

"What courses available?",
"The following engineering courses are available: <br> 1.Computer science and engineering <br> 2.Civil engineering <br> 3.Mechanical engineering <br> 4.Electronics and communication engineering <br> 5.Electrical and electronics engineering <br> 6.Information technology",

"How many courses are available",
"6",

"What about the fee details?",
"The tuition fee is Rs.5000 and college fee is Rs.35000 per year",

"Where is the college located?",
"To get location of coet 👉 <a href=" 'https://maps.app.goo.gl/2bQ6B1Pt5zei2YVQ9' ">Click Here</a>",

"location of college",
"To get location of coet 👉 <a href=" 'https://maps.app.goo.gl/2bQ6B1Pt5zei2YVQ9' ">Click Here</a>",

"Does the college conduct any fun programs?",
"Yes,of course. Our college not only provides excellent education but also encourage students to take part in different curriculam activities",

"duration of btech course?",
"Duration of btech course is from 4 years upto maximum of 6 years",

"How many semesters are there in a year?",
"2",

"What are the eligibility for admission?",
"+2 with keam rank is the eligibility for admission.There are NRI seats and management seats for which keam rank is not mandatory.",

"Certificates required for admission ?",
"1.Keam allotment card <br> 2.Aadhar card of student <br> 3.Sslc certificate <br> 4.+2 certificate <br> 5.Transfer certificate",

"Is college bus facility available?",
"Yes,the college bus facility is available to kannur,thalassery and mattannur routes",

"How long will the classes be?",
"Class starts at 9.30 am to 4.30 pm",

"class timing",
"Class starts at 9.30 am to 4.30 pm",

"What about hostel facilites?",
"The college has ladies hostel,for boys pgs are available",

"Does the college have canteen?",
"Yes the college have canteen and they are providing tasty and hygienic food",

"scholarship details",
"Yes the college grants scholarship for academically excellent students and also for economically weaker students.Their fees are reduced and scholarships like egrants are provided.",

"What about placements?",
"Yes the college also provides good placement offers to students",

"ragging present",
"Anti ragging camps are present in the campus to prevent ragging",

"How many classes are there in a day?",
"It depends on the academic calender.According to aicte 6 hours for regular classes also there are special classes on saturdays.",

"Does the college encourage sports?",
"Yes of course, the college provides training on different sports activities and there are many clubs for sports in the college",

"strength of departments",
"Strength of each departments <br> 1.Computer science and engineering - 60 <br> 2.Civil engineering - 60 <br> 3.Mechanical engineering - 60 <br> 4.Electronics and communication engineering - 120 <br> 5.Electrical and electronics engineering - 60 <br> 6.Information technology - 60",

"strength of ec department",
"120",

"strength of eee engineering department",
"60",

"strength of cs engineering department",
"60",

"strength of it department",
"60",

"strength of ce engineering department",
"60",

"strength of me engineering department",
"60",

"strength of ec",
"120",

"strength of eee",
"60",

"strength of cs",
"60",

"strength of it",
"60",

"strength of ce",
"60",

"strength of me",
"60",

"strength of electronics and communications",
"120",

"strength of electrical and electronics",
"60",

"strength of computer science",
"60",

"strength of information technology",
"60",

"strength of civil engineering",
"60",

"strength of mechanical engineering",
"60",

"What else can you do?",
"I can help you know more about COET",
    
    "1",
    "<b>STUDENT <br>The following are frequently searched terms related to student . Please select one from the options below : <br> <br> 1.1 Curriculars <br>1.2  Extra-Curriculars<br>1.3  Administrative<br>1.4 Examination <br>1.5 Placements </b>",
    
    "1.1",
    "<b>  CURRICULAR <br>  These are the top results: <br> <br> 1.1.1 Programmes <br> 1.1.2 Academic Calendar <br> 1.1.3 Syllabus </b>",
    "1.1.1",
    "<b> 1.1.1 Programmes <br>The link to Programmes 👉 <a href=" 'https://www.cethalassery.ac.in/ug-programs.php' ">Click Here</a> </b>",
    "1.1.2",
    "<b > 1.1.2 Academic Calender<br>The link to Academic Calender👉<a href=" 'https://www.cethalassery.ac.in/academic-calendar.php' ">Click Here</a> </b>",
    "1.1.3",
    "<b> 1.1.3 Syllabus<br>The link to Syllabus 👉 <a href=" 'https://www.cethalassery.ac.in/btech-syllabus.php#' ">Click Here</a> </b>",

    "1.2",
    "<b>EXTRA-CURRICULAR<br>These are the top results: <br> <br> 1.2.1 Events<br> 1.2.2 Students Corner <br> 1.2.3 College Union</b>",
    "1.2.1",
    "<b > 1.2.1 Events<br>The link to Events👉 <a href=" 'https://www.cethalassery.ac.in/events-cs.php' ">Click Here</a></b>",
    "1.2.2",
    "<b > 1.2.2 Students Corner<br>The link to Student Corner👉<a href=" 'https://www.cethalassery.ac.in/students-corner.php' ">Click Here</a> </b>",
    "1.2.3",
    "<b > 1.2.3 College Union <br>The link to College Union👉 <a href=" 'https://www.cethalassery.ac.in/college-union.php' ">Click Here</a> </b>",

    "1.3",
    "<b>1.3 ADMINISTRATIVE<br>These are the top results: <br> <br> 1.3.1 Students Portal<br> 1.3.2 Notices </b>",
    "1.3.1",
    "<b> 1.3.1 Students Portal<br>The link to Students Portal👉 <a href=" 'https://www.cethalassery.ac.in/administration-staff.php' ">Click Here</a> </b>",
    "1.3.2",
    "<b> 1.3.2 Notices<br>The link to Notices👉 <a href=" 'https://www.cethalassery.ac.in/' ">Click Here</a> </b>",

    "1.4",
    "<b > EXAMINATION <br>These are the top results:<br> 1.4.1 Notices<br> 1.4.2 Notes <br> 1.4.3 Question Paper Archive </b>",
    "1.4.1",
    "<b > 1.4.1 Notices<br>The link to Notices👉 <a href=" 'https://www.ktunotes.in/category/notifications/' ">Click Here</a> </b>",
    "1.4.2",
    "<b > 1.4.2 Notes<br>The link to Notes👉<a href=" 'https://www.ktunotes.in/category/NOTES/' ">Click Here</a> </b>",
    "1.4.3",
    "<b > 1.4.3 Question Paper Archive<br>The link to Archives👉 <a href=" 'https://www.ktunotes.in/tag/ktu-question-papers/' ">Click Here</a> </b>",

    "1.5",
    "<b > PLACEMENTS These are the top results:<br> 1.5.1 Placements<br> 1.5.2 Our Recruiters <br> 1.5.3 Placement Statistics </b>",
    "1.5.1",
    "<b> 1.5.1 Placements<br>The link to Placements👉 <a href=" 'http://placement.cethalassery.ac.in/' ">Click Here</a> </b>",
    "1.5.2",
    "<b> 1.5.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'https://sites.google.com/view/placements-tly/placements/our-recruiters' ">Click Here</a> </b>",
    "1.5.3",
    "<b > 1.5.3 Placement Statistics<br>The link to Placement Statistics👉 <a href=" 'https://sites.google.com/view/placements-tly/placements/placement-statistics' ">Click Here</a> </b>",

    "2",
    "<b >FACULTY<br>The following are frequently searched terms related to faculty. Please select one from the options below :</br></br>2.1 Portals & Administration<br>2.2  Change Personal Details<br>2.3  Examination </b>",
    
    "2.1",
    "<b > PORTALS & ADMINISTRATION These are the top results:<br> 2.1.1 Biometric Attendance System <br>2.1.2 Programmes </b>",
    "2.1.1",
    "<b> 2.1.1 Biometric Attendance<br>The link to Biometric Attendance👉<a href=" 'https://coet.etlab.in/' ">Click Here</a> </b>",
    "2.1.2",
    "<b> 2.1.2 Programmes<br>The link to Programmes👉<a href=" 'https://www.cethalassery.ac.in/ug-programs.php' ">Click Here</a> </b>",

    "2.2",
    "<b > CHANGE PERSONAL DETAILS These are the top results:<br> <br> 2.2.1 Site Login <br> </b>",
    "2.2.1",
    "<b> 2.2.1 Site Login<br>The link to Site Login👉<a href=" 'https://coet.etlab.in/' ">Click Here</a> </b>",
   
    "2.3",
    "<b > EXAMINATION <br>These are the top results:<br> <br> 2.3.1 Notices<br> 2.3.2 Question Paper Archive </b>",
    "2.3.1",
    "<b> 2.3.1 Notices <br>The link to Notices 👉 <a href=" 'https://www.ktunotes.in/category/notifications/' ">Click Here</a> </b>",
    "2.3.2",
    "<b> 2.3.2 Question Paper Archive <br>The link to Archive👉<a href=" 'https://www.ktunotes.in/tag/ktu-question-papers/' ">Click Here</a> </b>",
  
    "3",
    "<b> PARENTS <br>The following are frequently searched terms related to Parents. Please select one from the options below : <br> <br> 3.1 About Us <br>3.2 Notices <br>3.3 Fee Payment <br>3.4 Placements </b> " ,

    "3.1",
    "<b > ABOUT US<br>These are the top results:<br> <br> 3.1.1 About COET<br> 3.1.2 Contact Us <br> 3.1.3 Principal's Address </b>",
    "3.1.1",
    "<b > 3.1.1 About COET<br>The link to About COET👉 <a href=" 'https://www.cethalassery.ac.in/about-us.php' ">Click Here</a> </b>",
    "3.1.2",
    "<b > 3.1.2 Contact Us <br>The link to Contact Us👉<a href=" 'https://www.cethalassery.ac.in/contact-us.php' ">Click Here</a> </b>",
    "3.1.3",
    "<b > 3.1.3 Principal's Address <br>The link to Principal's Address👉 <a href=" 'https://www.cethalassery.ac.in/principal.php' ">Click Here</a> </b>",

    "3.2",
    "<b > NOTICES<br>These are the top results:<br> <br> 3.2.1 All Notices  </b>",
    "3.2.1",
    "<b > 3.2.1 All Notices <br>The link to All Notices👉 <a href=" 'https://www.cethalassery.ac.in/' ">Click Here</a> </b>",

    "3.3",
    "<b > FEE PAYMENT<br>These are the top results:<br> <br>3.3.1 Payment Details <br> 3.3.2 Online Payment Portal </b>",
    "3.3.1",
    "<b > 3.3.1 Payment Details<br>The link to Payment Details 👉 <a href=" 'https://www.cethalassery.ac.in/fee-structure.php' ">Click Here</a> </b>",
    "3.3.2",
    "<b > 3.3.2 Payment Portal <br>The link to Payment Portal👉<a href=" 'https://www.onlinesbi.sbi/sbicollect/icollecthome.htm' ">Click Here</a> </b>",

    "3.4",
    "<b > PLACEMENTS These are the top results:<br> <br>3.4.1 Placements<br> 3.4.2 Our Recruiters <br> 3.4.3 Placement Statistics </b>",
    "3.4.1",
    "<b> 3.4.1 Placements<br>The link to Placements👉 <a href=" 'http://placement.cethalassery.ac.in/' ">Click Here</a> </b>",
    "3.4.2",
    "<b> 3.4.2 Our Recruiters<br>The link to Recruiters👉<a href=" 'https://sites.google.com/view/placements-tly/placements/our-recruiters' ">Click Here</a> </b>",
    "3.4.3",
    "<b > 3.4.3 Placement Statistics<br>The link to Placement Statistics👉 <a href=" 'https://sites.google.com/view/placements-tly/placements/placement-statistics' ">Click Here</a> </b>",

    "4",
    "<b VISITORS <br>The following are frequently searched terms related to visitors. Please select one from the options below : <br> <br> 4.1 About Us<br>4.2 Programs We Offer <br>4.3 Student Bodies <br>4.4 Extra-Curricular </b>",
    
    "4.1",
    "<b > ABOUT US<br>These are the top results:<br> <br>4.1.1 About COET<br> 4.1.2 Contact Us <br> 4.1.3 Principal's Address </b>",
    "4.1.1",
    "<b > 4.1.1 About COET<br>The link to About COET👉 <a href=" 'https://www.cethalassery.ac.in/about-us.php' ">Click Here</a> </b>",
    "4.1.2",
    "<b > 4.1.2 Contact Us <br>The link to Contact Us👉<a href=" 'https://www.cethalassery.ac.in/contact-us.php' ">Click Here</a> </b>",
    "4.1.3",
    "<b > 4.1.3 Principal's Address <br>The link to Principal's Address👉 <a href=" 'https://www.cethalassery.ac.in/principal.php' ">Click Here</a> </b>",

    "4.2",
    "<b > PROGRAMS WE OFFER <br>These are the top results:<br> <br>4.2.1 Under-Graduate <br> 4.2.2 Post-Graduate </b>",
    "4.2.1",
    "<b > 4.2.1 Under-Graduate<br>The link to Under-Graduate👉 <a href=" 'https://www.cethalassery.ac.in/ug-programs.php' ">Click Here</a> </b>",
    "4.2.2",
    "<b > 4.2.2 Post-Graduate <br>The link to Post-Graduate👉<a href=" 'https://www.cethalassery.ac.in/pg-programs.php' ">Click Here</a> </b>",

    "4.3",
    "<b > STUDENT BODIES <br>These are the top results:<br> <br>4.3.1 Students Corner  <br> 4.3.2 College Union <br> 4.3.3 Students Project Groups </b>",
    "4.3.1",
    "<b > 4.3.1 Students Corner  <br>The link to Students Corner  👉 <a href=" 'https://www.cethalassery.ac.in/students-corner.php' ">Click Here</a> </b>",
    "4.3.2",
    "<b > 4.3.2 College Union <br>The link to College Union 👉<a href=" 'https://www.cethalassery.ac.in/college-union.php' ">Click Here</a> </b>",
    "4.3.3",
    "<b > 4.3.3 Students Project Groups <br>The link to Students Project Groups👉 <a href=" 'https://www.cethalassery.ac.in/' ">Click Here</a> </b>",

    "4.4",
    "<b > EXTRA-CURRICULAR <br>These are the top results:<br> <br>4.4.1 Events  <br> 4.4.2 Library </b>",
    "4.4.1",
    "<b > 4.4.1 Events    <br>The link to Events   👉 <a href=" 'https://www.cethalassery.ac.in/events-cs.php' ">Click Here</a> </b>",
    "4.4.2",
    "<b > 4.4.2 Library <br>The link to Library 👉<a href=" 'http://library.cethalassery.in/' ">Click Here</a> </b>",

]
#trainer.train("chatterbot.corpus.english.custom")
trainer.train(conversation)
