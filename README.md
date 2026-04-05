** Student Grade Predictor (Linear Regression)**
A desktop-based Machine Learning application that predicts a student's marks based on their study hours. 
The system uses Simple Linear Regression and integrates with MongoDB Atlas for real-time data retrieval and logging.

**Features**
Machine Learning Engine: Implements scikit-learn Linear Regression to find the correlation between study time and academic performance.
Cloud Database: Connects to MongoDB Atlas to fetch training data and store prediction logs.
Dynamic Data Cleaning: Uses pandas to handle missing values and ensure data types are correct before training.
Modern UI: A clean, user-friendly interface built with Tkinter.
Secure Configuration: Uses .env files to protect sensitive database credentials.

**Tech Stack**
Language: Python 3.14
Machine Learning: Scikit-Learn
Data Analysis: Pandas
Database: MongoDB Atlas (NoSQL)
GUI: Tkinter
Environment Management: Python-Dotenv

**Installation & Setup**

1.Clone the Repository:
  git clone https://github.com/yourusername/LinearRegression_project.git
  cd LinearRegression_project

2. Install Dependencies:
   pip install pandas scikit-learn pymongo dnspython python-dotenv

3. Configure Environment Variables:
   Create a .env file in the root directory and add your MongoDB Atlas connection string:
   MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/universitydb

4. Database Requirement:
   Ensure your MongoDB collection is named students inside the universitydb database and contains documents with the following structure:
   { "hours": 5, "marks": 75 }

5. Run the App:
    python LinearRegression.py

Author
Muzammil Ansari Computer Science Student at DUET

   
