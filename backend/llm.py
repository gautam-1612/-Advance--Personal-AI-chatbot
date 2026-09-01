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


class Project(BaseModel):
    name: str
    description: str
    technologies: list[str]
    link: str | None = None


class ResumeContent(BaseModel):
    name: str
    education: str
    skills: list[str]
    projects: list[Project]
    experience: str
    achievements: list[str]
    certifications: list[str]
    useful_links: dict[str, str]


sysMessage = f"""
you are a great resume content/skill extractor and you have to extract the skills from the resume/content provided by the user. 
You have to provide the data in JSON format. The data must be following {ResumeContent}
"""
role = "system"

systemMsg = {"role": role, "content": sysMessage}

userMessage = f"""
Extract the Skills from the provide content. Don't add any information by yourself. The content is as follows:


"""
