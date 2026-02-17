Mini Resume Management API
Author: Pathella Sivaparvathi

Submission for: TensorLogic.ai Assignment

1. Project Overview
This project is a high-performance REST API designed to streamline the collection and retrieval of candidate resumes. It is built using the FastAPI framework for speed and automatic validation.

Core Features:
Resume Metadata Collection: Captures 9 distinct fields including contact details and professional experience.

File Handling: Supports multipart/form-data for direct resume file uploads.

In-Memory Storage: Efficient data handling without the need for external database configuration.

Advanced Search: Filter candidates by skill set, experience level, or graduation year.

Health Monitoring: Built-in endpoint for automated status checks.

2. Technical Specifications
Language: Python 3.10.x

Framework: FastAPI (Asynchronous)

Server: Uvicorn (ASGI)


3. Installation & Setup
Follow these steps to set up the environment locally:

Step 1: Clone the Repository
git clone https://github.com/sivaparvathipathella/miniresume-Pathella-Sivaparvathi.git
cd miniresume-Pathella-Sivaparvathi
Step 2: Virtual Environment Setup
It is recommended to use a virtual environment to avoid dependency conflicts.


# Create the environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

Step 3: Install Required Packages
pip install -r requirements.txt

4. How to Run the Application
Start the development server with the following command:

uvicorn main:app --reload
The API will be live at: http://127.0.0.1:8000

Interactive Swagger Documentation: http://127.0.0.1:8000/docs

5. API Endpoints Detail
[GET] /health
Used to verify the system is operational.

Success Response: 200 OK | {"status": "healthy"}

[POST] /upload
Used to submit a new candidate profile.

Body Type: multipart/form-data

Required Fields:

full_name (String)

dob (String/Date)

contact_number (String)

contact_address (String)

education_qualification (String)

graduation_year (Integer)

years_of_experience (Integer)

skill_set (String)

resume_file (File - .pdf/.doc)

[GET] /candidates
Retrieve all candidates or filter based on specific criteria.

Query Parameters: skill, experience, graduation_year
