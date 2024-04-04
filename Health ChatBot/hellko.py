import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

  #here we increse message probability
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    #at end we break loop and stored bool fuction in required_words   

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    #make percentage in 1 to 100 so that we can easily compare it    
    else:
        return 0


def check_all_messages(message):
    highpblst = {}

    
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highpblst
        highpblst[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    
    response('How may I help you?\n1.Health checkup\n2.Facilities\n3.Consultants\n4.Career\n5.About HOspital\n6.Emergency', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    
    response('a.Basic checkup\nb.Whole body checkup\nc.heart checkup', ['1','Health','checkup','health','Checkup'], single_response=True)
    
    response('Facilities under basic Health Checkup\n 1.Blood Group\n2.Diabetes\n3.Cholestrol\nTotal cost will be rs.1000+GST\nWant to book an appointment[yes/no] ', ['a', 'Basic ','basic','checkup' ,'Checkup'], single_response=True)
    response('Please tell us your deatils in format given below \nAims(space)yourname(space)email?', ['yes', ' YES','Yes'], single_response=True)
    response('Your appointment has been booked and further details will be mailed to you shortly',['Aims','AIMS','aims'], single_response=True)

    response('Facilities under basic Health Checkup\n 1.Blood Group\n2.Diabetes\n3.Cholestrol\n4.DIgital chest x-ray\n5.ESR\nTotal cost will be rs.2000+GST\nWant to book an appointment[yes/no]', ['b', ' Whole','whole','checkup' ,'Checkup','body','Body'], single_response=True)
    response('Please tell us your deatils in format given below \nAims(space)yourname(space)email?', ['yes', ' YES','Yes'], single_response=True)
    response('Your appointment has been booked and further details will be mailed to you shortly',['Aims','AIMS','aims'], single_response=True)

    response('Facilities under basic Health Checkup\n 1.ECG\n2.MRI\n3.Blood Pressure\n4.EEG\nTotal cost will be rs.5000+GST\nWant to book an appointment[yes/no]', ['c', 'heart','Heart','checkup' ,'Checkup'], single_response=True)
    response('Please tell us your deatils in format given below \nAims(space)yourname(space)email?', ['yes', ' YES','Yes'], single_response=True)
    response('Thank YOU,Bye', ['NO', ' No','no'], single_response=True)
    response('Your appointment has been booked and further details will be mailed to you shortly',['Aims','AIMS','aims'], single_response=True)

    response('1.MRI\n2.Cathlab\n3.Investigation\n4.Other Facilities', ['2','facilities','Failities','facility','Facility'], single_response=True)
    response('M.R.I.\nMulti Channel, Open MRI has been started', ['MRI','mri'], single_response=True)
    response('Ultra modern Cath lab, having facilities for all type of Cardiac, Neuro & peripherals interventure procedures', ['cathlab','Cathlab\nCardiac catheterization is a procedure performed to diagnose and treat certain types of cardiovascular diseases'], single_response=True)
    response('#RADIOLOGY\n#M.R.I.\n#CT Scan\n#Color Doppler\n# (2D)3D \n#Radiography\n#Digital X-Ray\n#Barium Meal Follow Through\n#H.S.G.', ['investigation','investigation'], single_response=True)
    response('#Emergency Services\n#Laboratory and Radiology\n#Blood Bank with Components\n#Critical Care Ambulance\n#Pharmacy\n#Heamo-Dialysis\n#PhysiotherapyAudiometry\n#Health Check-up Plans', ['Other ','Facilities','other' ,'facilities'], single_response=True)

    response('\n#Cardiology\n\nDr. S.R. Mittal -\n M.D., D.MPre. Exp. - Retd. Prof. & H.O.D., J.L.N. Hospital,\n.Dr. Rahul Gupta - \nM.D.,D.M., FACC, FESCPre. Exp. - G.B. Pant Hospital, New Delhi.\nDr. Vivek Mathur -\n M.D., DNB, FESC, FSCAIPre. Exp. - Fortis Escort Heart Institute, New Delhi.\n\n#Heart Surgery\n\nDr. Vivek Rawat -\n M.Ch.Pre. Exp. - SMS Hospital, Jaipur.Neuro Physician\n Dr. Vinod K Sharma \n- D.M.Pre. Exp. - SMS Hospital, Jaipurand B.J.M.C. AhmedabadNeuro Surgery\nDr. Siddharth Verma \n- M.S., DNBPre. Exp. - Safdarjung Hospital and \nSir Gangaram Hospital New DelhiNephrologyDr.\n Ranveer Singh Choudhary\n – D.M.. Exp. - Bombay Hospital, Mumbai.\n\n#Gastroenterology\n\nDr. Rishabh Kothari\n – MD, DNB (Gastroenterology)Prev. Exp.:- Max Super Speciality Hospital (Vaishali) Delhi\nDr. S. P. Jindal\n – MS, DNB (GI Surgery & Liver Transplant))Prev. Exp.: Apollo Hospital, New DelhiSurgical Oncology\nDr. Arpit Jain\n – MS, DNBPrev Exp:- Bhagwan Mahaveer Cancer Hospital & Research Centre, JaipurUrology', ['3','consultants','consultant','Consultant','Consultants'], single_response=True)
    
    response('#Sr. Consultants/Consultants :\n General Medicine, Radiology, Neurology, Nephrology, Paediatric Surgery,Officers & Staff for Marketing, Finance, Accounts, Purchase, EDP, HR, Front Office etc.\n\n#Visiting Consultants :\n in Super Specialities.\n\n#NursingOfficers & Staff for Marketing, Finance, Accounts, Purchase, EDP, HR, Front Office etc. :\n\n Nursing Superintendent, ICU Staff, Cath Lab Scrub Nurse, Supervisors & Staff Nurses\n\n#Paramedical:\n\nTechnicians in EEG, OT, Dialysis, CSSD, Ophthalmology & Dentistry, CATH LAB\n\n#Support Services : \n\nSpeech Therapist, Audiologist, Pharmacist & Medical Records Officer.\n\n#Education:\n\nTeachers and instructors have the challenging task of helping students learn. To keep their attention, many teachers must find new ways to create interest and motivate those students. The nursing profession requires similar skills.\n', ['4','career','Career'], single_response=True)

    response('Ajmer is well known spiritual city of the country, having international identity specially due to Dargah of Khwaja Sahib and Great Hindu pilgrim Pushkar Raj.\n\nPopulation of Ajmer district is near about 30 lakhs, but unfortunately not much attention is paid regarding development of medical facilities. There is only one big government hospital to look after a large number of patients residing at Ajmer and surrounding areas. It is obviously very difficult to meet out all medical requirements of the large number of patients by a single hospital. So many people are compelled to go Jaipur, Delhi, Mumbai, Ahmadabad etc for medical aids.\n\need for a modern well equipped & multi specialty hospital was felt since long. Mittal Hospital & Research Centre is established to contribute medical care facilities to every class of the society at large\n\nFoundation stone of the building was laid by Gurudev Shri Harprasad Mishra "Uvesee" on 26 October, 2003 at Pushkar Road, Ajmer, which is located at prime point and only 2 to 7 km. away from the various parts of the city. This five storey building spreading over-1.20 Lakhs sq. feet constructed area was completed in 2 years. Hospital was inaugurated on 4th of November, 2005 by Gurudev Shri Harprasad Mishra "Uvesee".\n\n', ['5','about','About','hospital','Hospital'], single_response=True)

    response('We have detected your location and amulalance will arrive as soon as possible/n', ['6','Emergency','emergency','EMERGENCY'], single_response=True)
    


   
    best_match = max(highpblst, key=highpblst.get)
 

    return long.unknown() if highpblst[best_match] <1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
# print("Bot: Good Morning,How may i help you?")
# while True:
#     print('Bot: ' + get_response(input('You: ')))