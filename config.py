EXPERIENCE_LEVELS = ["Beginner", "Intermediate", "Advanced"]

BULLET_STYLES = {
    "ATS Optimized": "Keyword-rich bullets for Applicant Tracking Systems",
    "Concise": "Short, punchy bullets that get straight to the point",
    "Impact-Focused": "Emphasizes outcomes and contributions"
}

REWRITE_OPTIONS = {
    "Shorter": "Make it more concise",
    "More Technical": "Add more technical depth",
    "More Impact-Focused": "Emphasize outcomes"
}

BULLET_COUNT_OPTIONS = [2, 3, 4, 5]

DEFAULT_BULLET_COUNT = 3

BULLET_LENGTH_OPTIONS = {
    "Short (10-15 words)": (10, 15),
    "Medium (15-25 words)": (15, 25),
    "Long (25-35 words)": (25, 35)
}
DEFAULT_BULLET_LENGTH = "Medium (15-25 words)"
MIN_DESCRIPTION_LENGTH = 30 
MIN_DESCRIPTION_WORDS = 5 

MAX_RETRIES = 1 
TEMPERATURE = 0.7  
EXAMPLE_INPUTS = [
    {
        "name": "Backend Developer",
        "description": "I worked on the backend of our e-commerce platform. I built REST APIs for the checkout and payment processing. We used Python with Flask and PostgreSQL database. I also wrote unit tests and fixed several bugs in the order management system.",
        "tech_stack": "Python, Flask, PostgreSQL, Redis, Docker",
        "target_role": "Backend Engineer",
        "experience_level": "Intermediate"
    },
    {
        "name": "Data Analyst",
        "description": "I analyzed customer behavior data to find patterns and trends. Created dashboards for the marketing team to track campaign performance. Used SQL to query large datasets and Python for data visualization. Presented findings to stakeholders weekly.",
        "tech_stack": "Python, SQL, Tableau, Pandas, Excel",
        "target_role": "Data Analyst",
        "experience_level": "Beginner"
    },
    {
        "name": "Full Stack Developer",
        "description": "Led development of a real-time collaboration tool for remote teams. Architected the microservices backend and designed the React frontend. Implemented WebSocket connections for live updates. Mentored two junior developers and conducted code reviews.",
        "tech_stack": "React, Node.js, TypeScript, MongoDB, AWS, WebSocket",
        "target_role": "Senior Full Stack Developer",
        "experience_level": "Advanced"
    },
    {
        "name": "ML Engineer",
        "description": "Built machine learning models to predict customer churn. Processed and cleaned large datasets for training. Deployed models using Docker containers on cloud infrastructure. Improved prediction accuracy through feature engineering and hyperparameter tuning.",
        "tech_stack": "Python, TensorFlow, Scikit-learn, Docker, AWS SageMaker",
        "target_role": "Machine Learning Engineer",
        "experience_level": "Intermediate"
    }
]
