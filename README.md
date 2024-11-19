# Attendance Management System 
The Attendance Management System is a digital solution designed to streamline the process of tracking and 
managing student attendance. Traditionally, attendance is maintained manually, which is time-consuming and 
prone to errors. This system aims to automate attendance tracking, making it more efficient and reliable for 
both teachers and students. 
Built using Django, a powerful web development framework, the system allows teachers to mark attendance 
for students in various subjects, monitor overall attendance percentages, and export attendance records. 
Students can view their attendance data in real-time, ensuring transparency and enabling them to keep track 
of their performance.  Automating attendance calculations, this system reduces administrative burdens and 
enhances the accuracy of attendance records.

# Inputs: 
1. Teacher Login/Password Verification: Teachers enter a password to access the attendance dashboard. 
2. Student Registration Data: Input student details, including name, enrollment number, batch, 
semester, and other information during registration. 
3. Attendance Marking: Teachers select students, subjects, and attendance status (e.g., present/absent) 
for each session. 
4. Filtering Criteria: Teachers select filters (batch, semester, subject) to view specific student groups for 
attendance. 
5. Export Request: Teachers select a semester to export attendance records in Excel format.
   
# Outputs: 
1. Teacher Dashboard: Displays filtered lists of students, attendance percentages, and options to mark 
attendance. 
2. Student Dashboard: Shows each student’s personal attendance percentage and records by subject. 
3. Attendance Records: Updated attendance percentages for each student, both overall and by subject. 
4. Error Messages: Displays messages for invalid inputs, such as incorrect passwords or missing data. 
5. Excel Report: An exportable Excel file with attendance data, showing attendance percentages for each 
student per subject.
