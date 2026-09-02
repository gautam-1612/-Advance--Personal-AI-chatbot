from groq import Groq
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai ?")

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"


class Education(BaseModel):
    institution: str
    degree: str
    cgpa: str
    start_year: str
    end_year: str


class Experience(BaseModel):
    company: str
    location: str
    title: str
    start_date: str
    end_date: str
    responsibilities: list[str]


class Project(BaseModel):
    name: str
    description: str
    technologies: list[str]
    link: str | None = None
    priority: int


class ResumeContent(BaseModel):
    name: str
    email: str
    phone: str
    profile_summary: str
    education: list[Education]
    skills: list[str]
    certifications: list[str]
    experience: list[Experience]
    projects: list[Project]
    achievements: list[str]
    useful_links: dict[str, str]


sysMessage = """
You are an expert resume and professional-profile information extractor.

Extract the candidate's information from the resume and supplemental
information provided by the user.

Return ONLY valid JSON matching the ResumeContent structure.

SOURCE PRIORITY:

1. Use the resume as the primary source for:
   - name
   - profile summary
   - education
   - professional experience
   - certifications
   - skills

2. Use the supplemental information as the authoritative source for:
   - current LeetCode progress
   - GitHub
   - LinkedIn
   - current/additional skills
   - projects
   - project links
   - project priority

3. If the two sources contain conflicting information, prefer the
   supplemental information.

GENERAL RULES:

1. NEVER invent, assume, estimate, or hallucinate information.

2. Only extract information explicitly present in the provided sources.

3. Do not modify, shorten, or create URLs.

4. If information is unavailable:
   - string → ""
   - list → []
   - dictionary → {}
   - optional project link → null

SKILLS:

5. Extract individual technical skills into the skills list.

6. Include technologies the candidate explicitly says they know, use,
   or are familiar with.

7. Do not turn a technology into professional experience unless the
   source explicitly says the candidate used it professionally.

EDUCATION:

8. Extract each education entry with:
   - institution
   - degree
   - CGPA
   - start year
   - end year

EXPERIENCE:

9. Extract each professional experience entry with:
   - company
   - location
   - title
   - start date
   - end date
   - responsibilities

10. Statements describing work performed at a company belong under
    experience.responsibilities.

11. Do NOT place normal job responsibilities inside achievements.

ACHIEVEMENTS:

12. Achievements should contain actual accomplishments, awards,
    milestones, or measurable achievements.

13. Examples include:
    - LeetCode problems solved
    - LeetCode badges
    - awards
    - rankings
    - measurable accomplishments

14. Do NOT copy normal job responsibilities into achievements.

CERTIFICATIONS:

15. Extract certifications as individual items.

PROJECTS:

16. The supplemental project list is the authoritative project list.

17. Do NOT create duplicate projects from the resume.

18. If a project appears in both the resume and supplemental information,
    merge the information into ONE project.

19. Preserve the exact order of projects from the supplemental information.

20. Assign priority sequentially:
    first project = 1,
    second project = 2,
    third project = 3,
    and so on.

21. Do NOT reorder projects based on your own judgment.

22. Extract project:
    - name
    - description
    - technologies
    - link
    - priority

23. Only include technologies explicitly provided for that project.
    Do not infer technologies from the project name.

24. If a project has more detailed information in the resume, you may
    combine that information with the supplemental project information,
    but do not duplicate the project.

25. Do not add projects that are not present in the supplemental project list.

IMPORTANT:

26. Keep profile information, experience responsibilities,
    achievements, skills, certifications, and projects in their
    appropriate fields.

27. Do not move information between categories merely because it
    sounds related.

28. Return ONLY the JSON object.

29. Do not return markdown, explanations, comments, or code fences.

Accuracy and honesty are more important than completeness.
"""

systemMsg = {"role": "system", "content": sysMessage}

resume_text = """
PROFILE 
Gautam Bhushan 
+91-8725835407 |  gautambhushan5@gmail.com |  GitHub 
Software Engineer with 2+ years of professional experience developing enterprise software solutions. Strong foundation in 
full-stack web development with React, Next.js, Node.js, and MongoDB through hands-on projects. 
EDUCATION 
Punjab Technical University. 7.2 CGPA
Bachelor of Technology in Computer Science & Engineering. 2018 – 2022 
 
SKILLS 
• Programming Languages: JavaScript, C++ (for DSA, Solved 150+ Questions on Leetcode.) 
• Frontend: React.js, Next.js, HTML, CSS, Tailwind CSS 
• Backend: Node.js, Express.js, REST APIs 
• Databases: MongoDB, Supabase 
• Cloud & Tools: Google Cloud Platform (GCP) 
• Developer Tools: Git, GitHub, VScode 
 
CERTIFICATIONS 
• The Complete JavaScript Course 2025 : From Zero to Expert by Jonas Schmedtmann.  (link - "https://www.udemy.com/certificate/UC-df4e925c-a376-4ef6-8074-80533c919596/") 
• The Ultimate React Course 2025: React, Next.js, Redux & More by Jonas Schmedtmann.  (link - "https://www.udemy.com/certificate/UC-3011e7f0-9ec7-47d2-9d97-074d7fee6240/" ) 
 
EXPERIENCE 
Wipro Limited Noida, India 
Project Engineer Dec 2022 – Apr 2025 
• Collaborated with cross-functional teams delivering enterprise software solutions for a global telecom client Ericsson. 
• Managed and resolved Jira tickets within agile sprints, ensuring timely fixes and stable application releases. 
• Debugged and fixed application issues, improving performance, reliability, and overall system stability. 
• Created clear technical and process documentation to improve collaboration and long-term maintainability. 
 
"""

userMessage = f"""
Extract the candidate's complete professional profile from the information
provided below.

There are two sources:

1. Resume content
2. Supplemental professional information

Use BOTH sources.

If the supplemental information conflicts with the resume, prefer the
supplemental information because it may contain more recent information.

Do not add any information that is not explicitly present.

========================
RESUME CONTENT
========================

{resume_text}

========================
SUPPLEMENTAL INFORMATION
========================

CURRENT LEETCODE INFORMATION/ACHIEVEMENTS

- 180+ LeetCode problems solved.
- LeetCode profile:
  https://leetcode.com/u/gautambhushan/
- Earned a 50-day LeetCode badge in 2024.
- Earned a 50-day LeetCode badge in 2026.


OTHER USEFUL LINKS AND CONTACT INFORMATION

- GitHub:
  https://github.com/gautam-1612

- LinkedIn:
  https://www.linkedin.com/in/gautam-bhushan-/

- Email:
  gautambhushan5@gmail.com

- Phone:
  +91-8725835407


ADDITIONAL TECHNICAL KNOWLEDGE

- Currently learning and working with LLM concepts and applications.
- Familiar with Docker.
- Learning prompt engineering.
- Learning structured outputs, JSON and Pydantic.
- Learning prompt chaining.
- Learning streaming LLM responses.
- Building React-based AI applications.


PROJECTS

The following projects are intentionally listed in the candidate's preferred
presentation order.

PROJECT 1
Name:
Advance Personal AI Chatbot

Repository:
https://github.com/gautam-1612/-Advance--Personal-AI-chatbot

Tech Stack: JavaScript, Python, prompt engineering, LLMs, React.js, CSS

Description:
Personal AI chatbot project.


PROJECT 3
Name:
Resume Matching Agent

Repository:
https://github.com/gautam-1612/-Medium--Resume-Matching-Agent

Tech Stack: Python, prompt engineering, LLMs

Description:
AI-powered resume screening and job matching system that extracts
structured JD/resume data, evaluates skill, education, and experience
matches, and ranks candidates using weighted scoring.


PROJECT 4
Name:
Valren Online Store

Repository:
https://github.com/gautam-1612/-Advance--Valren-Online-Store

Tech Stack: Node.js, Express, MongoDB, Mongoose, Express-validator, EJS, bcrypt, CSRF, PDFkit, Stripe, Nodemailer 

Description:
• Built an e-commerce application using Node.js, Express, MongoDB, implementing modular MVC architecture. 
• Implemented authentication, authorization, password reset emails, and secure session management. 
• Integrated payment gateways and order workflows, automated invoice generation and email notifications.


PROJECT 5
Name:
The Wild Oasis Website

Repository:
https://github.com/gautam-1612/-Advance--The-Wild-Oasis-Website

Tech Stack: Next.js (App Router), RSC, Google Cloud Authentication, Supabase, caching, context API, Tailwind

Description:
• Built a full-stack hotel booking application using Next.js App Router with server and client components. 
• Implemented authentication, protected routes, and data management using Supabase and modern React patterns. 
• Developed dynamic cabin listings and booking workflows with optimized performance via Server Actions and caching. 


PROJECT 6
Name:
The Wild Oasis Dashboard

Repository:
https://github.com/gautam-1612/-Advance--The-Wild-Oasis-Dashboard

Tech Stack: React.js, React Router, Supabase auth, Context API, TanStack React Query, Styled Components, Recharts 

Description:
• Built an internal hotel management dashboard using React, Vite, and Supabase for operational workflows. 
• Enabled admins to manage bookings, confirm reservations through role-based access controls. 
• Built authenticated dashboards with live booking statistics and theme switching. 




FINAL INSTRUCTIONS

Extract all relevant information into the ResumeContent structure.

Remember:

- Use both the resume and supplemental information.
- Prefer newer supplemental information when there is a conflict.
- Do not invent information.
- Do not guess missing information.
- Do not modify URLs.
- Preserve the project order.
- Assign priorities from 1 to 11 according to that order.
- Return ONLY valid JSON.
"""

userMessage = {"role": "user", "content": userMessage}

messages = [systemMsg, userMessage]

response = client.chat.completions.create(
    model=model, messages=messages, temperature=0.0
)

answer = response.choices[0].message.content
print(answer)
# Adding llm_response as JSON to the profile.json
import json

answer = response.choices[0].message.content

profile = json.loads(answer)

with open("newprofile.json", "w", encoding="utf-8") as file:
    json.dump(profile, file, indent=2, ensure_ascii=False)

print("newprofile.json updated successfully.")
