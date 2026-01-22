import os

APP_TITLE = "Resume Bullet Enhancer"
APP_ICON = "⚡"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"
TEMPERATURE = 0.7
MAX_RETRIES = 2

MIN_DESC_LENGTH = 15

EXPERIENCE_LEVELS = ["Beginner", "Intermediate", "Advanced"]

BULLET_STYLES = {
    "ATS Optimized": "Keyword-rich, standard terminology",
    "Concise": "Short, punchy, core achievements",
    "Impact-Focused": "Emphasizes metrics and business value"
}

REWRITE_OPTIONS = {
    "Shorter": "Condense under 15 words",
    "More Technical": "Add specific tools/methodology",
    "More Impact-Focused": "Emphasize outcomes"
}

BULLET_COUNTS = [2, 3, 4, 5]
DEFAULT_COUNT = 3

BULLET_LENGTHS = {
    "Short": "Keep strictly under 15 words.",
    "Medium": "Between 15-25 words (balanced).",
    "Long": "Over 25 words. Detailed elaboration on methodology and impact."
}

EXAMPLE_INPUTS = {
    "Backend Engineer": {
        "role": "Backend Developer",
        "tech": "Python, Flask, PostgreSQL, Redis",
        "exp": "Intermediate",
        "desc": "I built the backend for an e-commerce site. It was slow so I added caching which made it faster. I also fixed bugs in the payment system."
    },
    "Data Analyst": {
        "role": "Data Analyst",
        "tech": "SQL, Tableau, Python (Pandas)",
        "exp": "Beginner",
        "desc": "I looked at customer data to find trends. I made dashboards for the marketing team to see how ads were doing. I cleaned the data using Python."
    },
    "Product Manager": {
        "role": "Product Manager",
        "tech": "JIRA, Agile, Linear",
        "exp": "Advanced",
        "desc": "Led a cross-functional team of 10. We launched the mobile app 2 weeks early. I managed the roadmap and stakeholder communication."
    },
    "Frontend Dev": {
        "role": "Frontend Developer",
        "tech": "React, TypeScript, Tailwind, Redux",
        "exp": "Intermediate",
        "desc": "Converted Figma designs into pixel perfect pages. Optimized the bundle size which improved load time by 30%. Implemented dark mode."
    },
    "DevOps Engineer": {
        "role": "DevOps Engineer",
        "tech": "AWS, Docker, Jenkins, Terraform",
        "exp": "Advanced",
        "desc": "Automated the deployment pipeline. Reduced build times from 20 mins to 5 mins. Managed cloud infrastructure cost, saving 15%."
    },
    "Software Intern": {
        "role": "SDE Intern",
        "tech": "Java, Spring Boot, MySQL",
        "exp": "Beginner",
        "desc": "Fixed bugs in the legacy code. Wrote unit tests for the login API. Participated in daily standups and code reviews."
    },
    "ML Engineer": {
        "role": "Machine Learning Engineer",
        "tech": "Python, TensorFlow, PyTorch, Scikit-learn, AWS SageMaker",
        "exp": "Intermediate",
        "desc": "Built a recommendation engine for product suggestions. Trained models on 1M+ data points. Improved click-through rate by 25%. Deployed model to production using SageMaker."
    },
    "Mobile Developer": {
        "role": "Mobile App Developer",
        "tech": "React Native, TypeScript, Firebase, Redux",
        "exp": "Intermediate",
        "desc": "Developed the iOS and Android app from scratch. Integrated push notifications and analytics. App reached 50k downloads in first month."
    },
    "Security Engineer": {
        "role": "Security Engineer",
        "tech": "Python, Burp Suite, AWS Security Hub, Splunk",
        "exp": "Advanced",
        "desc": "Conducted penetration testing on 15 applications. Identified and remediated 40+ vulnerabilities. Implemented SIEM monitoring reducing incident response time by 60%."
    },
    "QA Engineer": {
        "role": "QA Engineer",
        "tech": "Selenium, Cypress, Jest, Postman",
        "exp": "Beginner",
        "desc": "Wrote automated tests for the web application. Created API test suites. Reduced regression testing time from 3 days to 4 hours."
    },
    "Cloud Architect": {
        "role": "Cloud Solutions Architect",
        "tech": "AWS, Azure, Kubernetes, Terraform, CloudFormation",
        "exp": "Advanced",
        "desc": "Designed multi-region architecture for high availability. Migrated 200+ services to cloud. Reduced infrastructure costs by 40% through optimization."
    },
    "UX Designer": {
        "role": "UX/UI Designer",
        "tech": "Figma, Adobe XD, Sketch, Principle",
        "exp": "Intermediate",
        "desc": "Redesigned the checkout flow which increased conversions by 35%. Conducted user research with 50+ participants. Created a design system with 100+ components."
    }
}