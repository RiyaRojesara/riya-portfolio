import json
import random
from django.shortcuts import render
from django.http import FileResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.conf import settings
import os


def home(request):
    """Main portfolio page — single page scrollable."""

    # ─────────────────────────────────────────
    # ✏️  CUSTOMIZE: Update all data below with your own info
    # ─────────────────────────────────────────

    context = {
        # Personal Info
        'name': 'Riya Rojesara',
        'title': 'AI-ML Engineer',
        'tagline': 'Developing production-ready AI: LangChain/LangGraph, RAG, and intelligent agents.',
        'about_text': (
        "I'm an AI/ML Engineer focused on building production-ready intelligent systems using LLMs, "
        "agent workflows, and advanced retrieval pipelines. I specialize in turning complex data and "
        "real-world problems into scalable AI solutions with practical impact. From healthcare data "
        "summarization to multi-agent assistants, I enjoy designing systems that are both powerful and reliable."
    ),

    'about_text_2': (
        "My stack includes Python, LangChain, LangGraph, Transformers, FastAPI, and modern ML frameworks "
        "like PyTorch and TensorFlow. I work across the full AI lifecycle—from data processing and model "
        "development to deployment and evaluation. I believe great AI systems are not just accurate, but "
        "efficient, interpretable, and built for real-world use."
    ),
        'location': 'Ahmedabad, Gujarat',
        'email': 'riyarojesara008@gmail.com',

        # ✏️  CUSTOMIZE: Social Links
        'github_url': 'https://github.com/RiyaRojesara',
        'linkedin_url': 'https://www.linkedin.com/in/riya-rojesara-83383a304/',

        # ✏️  CUSTOMIZE: Experience
        'experiences': [
            {
        'role': 'Associate AI-ML Engineer',
        'company': 'Artem HealthTech Pvt. Ltd.',
        'period': 'Feb 2026 – Present',
        'description': 'Building production-ready LLM-powered healthcare systems, including medical data extraction, summarization, and intelligent workflows. Developing RAG pipelines and agent-based solutions to process patient records and generate actionable clinical insights.',
        'tags': ['Python', 'LLMs', 'LangChain', 'LangGraph', 'RAG', 'NLP', 'FastAPI', 'Healthcare AI'],
        'icon': '🚀',
    },
    {
        'role': 'Data Science Intern',
        'company': 'Petpooja',
        'period': 'May 2025 – Feb 2026',
        'description': 'Worked on Deep Learning and NLP-based systems, including text processing, computer vision tasks, and LLM integrations. Built intelligent pipelines using LangChain and LangGraph for automation, data understanding, and real-world AI applications.',
        'tags': ['Python', 'Deep Learning', 'NLP', 'Computer Vision', 'Transformers', 'LangChain', 'LangGraph', 'PyTorch'],
        'icon': '🎨',
    },
    {
        'role': 'AI-ML Intern',
        'company': 'Technocolabs Softwares Inc.',
        'period': 'Jan 2025 - Apr 2025',
        'description': 'Worked on core Machine Learning and predictive modeling tasks, including data preprocessing, feature engineering, and model building. Developed predictive systems using algorithms like SVM, Random Forest, and regression techniques for real-world datasets.',
        'tags': ['Python', 'Machine Learning', 'Predictive Modeling', 'Scikit-learn', 'Pandas', 'NumPy', 'Data Analysis'],
        'icon': '📊',
    },
    {
    "role": "AI-ML Intern",
    "company": "Zidio Development",
    "period": "Sep 2024 - Dec 2024",
    "description": "Gained hands-on experience in core Machine Learning concepts, including data preprocessing, exploratory data analysis, and building predictive models. Learned and applied algorithms like SVM, Random Forest, and regression techniques on real-world datasets, while strengthening foundational ML skills such as model evaluation and feature selection.",
    "tags": ["Python", "Machine Learning", "Predictive Modeling", "Scikit-learn", "Pandas", "NumPy", "Data Analysis", "Matplotlib", "Seaborn"],
    "icon": "🤖"
}
        ],

        # ✏️  CUSTOMIZE: Projects
        'projects': [
            {
        'title': 'Healthcare Data Extraction & Summarization System',
        'description': 'Built an LLM-powered system to fetch and process patient history from live healthcare portals, extracting critical clinical data and generating concise summaries for faster doctor decision-making.',
        'tags': ['Python', 'LLMs', 'NLP', 'LangChain', 'RAG', 'Data Extraction', 'Healthcare AI'],
        'github': 'https://github.com/yourusername/healthcare-llm-system',
        'demo': None,
        'featured': True,
        'emoji': '🏥',
    },
    {
        'title': 'LangGraph ChatFlow (Adaptive AI Chatbot)',
        'description': 'Developed a multi-threaded AI chatbot using LangGraph with memory retention, RAG-based document querying, and fallback web search integration for handling unknown queries intelligently.',
        'tags': ['Python', 'LangGraph', 'LangChain', 'LLMs', 'RAG', 'Agents', 'Conversational AI'],
        'github': 'https://github.com/yourusername/langgraph-chatflow',
        'demo': None,
        'featured': True,
        'emoji': '🤖',
    },
    {
        'title': 'AI LinkedIn Post Generator',
        'description': 'Built an LLM-based content generation system that creates high-engagement LinkedIn posts with multiple variants using A/B testing across tone, style, and length.',
        'tags': ['Python', 'LLMs', 'Prompt Engineering', 'NLP', 'Content Generation'],
        'github': 'https://github.com/yourusername/linkedin-post-generator',
        'demo': None,
        'featured': True,
        'emoji': '✍️',
    },
    {
        'title': 'Malaria Detection using Deep Learning',
        'description': 'Developed a medical image classification system using CNN and VGG19, combined with traditional ML models like SVM and Random Forest for accurate malaria cell detection.',
        'tags': ['Python', 'Deep Learning', 'CNN', 'VGG19', 'Computer Vision', 'Scikit-learn'],
        'github': 'https://github.com/yourusername/malaria-detection',
        'demo': None,
        'featured': False,
        'emoji': '🧬',
    },
    {
        'title': 'AI-Powered Financial Assistant (Multi-Agent System)',
        'description': 'Designed a multi-agent AI assistant using LLMs to provide real-time stock insights by integrating financial APIs and web search, reducing manual research effort significantly.',
        'tags': ['Python', 'LLMs', 'Agents', 'Phidata', 'Groq', 'YFinance', 'Automation'],
        'github': 'https://github.com/yourusername/ai-financial-assistant',
        'demo': None,
        'featured': True,
        'emoji': '📈',
    },
        ],

        # ✏️  CUSTOMIZE: Certificates
        'certificates': [
                {
        'title': 'Introduction to Generative AI',
        'issuer': 'Google Cloud',
        'badge': '🤖',
        'color': 'blue',
    },
    {
        'title': 'Prompt Engineering: Shaping Better AI Responses',
        'issuer': 'IBM SkillsBuild',
        'badge': '✍️',
        'color': 'purple',
    },
    {
        'title': 'Introduction to Large Language Models',
        'issuer': 'Google Cloud',
        'badge': '🧠',
        'color': 'indigo',
    },
    {
        'title': 'Neural Networks and Deep Learning',
        'issuer': 'DeepLearning.AI',
        'badge': '📊',
        'color': 'green',
    },
    {
        'title': 'Introduction to Natural Language Processing',
        'issuer': 'Great Learning',
        'badge': '💬',
        'color': 'teal',
    },
        ],

        # ✏️  CUSTOMIZE: Tech Stack
        'tech_stack': {
        'Programming & Databases': [
            {'name': 'Python', 'icon': '🐍', 'level': 95},
            {'name': 'PostgreSQL', 'icon': '🐘', 'level': 85},
            {'name': 'MongoDB', 'icon': '🍃', 'level': 80},
            {'name': 'SQLite', 'icon': '🗄️', 'level': 75},
        ],
        'ML & Data Science': [
            {'name': 'NumPy', 'icon': '🔢', 'level': 90},
            {'name': 'Pandas', 'icon': '🐼', 'level': 92},
            {'name': 'Scikit-learn', 'icon': '📊', 'level': 88},
            {'name': 'Feature Engineering', 'icon': '🧩', 'level': 87},
            {'name': 'Data Processing', 'icon': '⚙️', 'level': 90},
            {'name': 'Data Extraction & Automation', 'icon': '🔄', 'level': 85},
        ],
        'Deep Learning & NLP': [
            {'name': 'Transformers', 'icon': '🤖', 'level': 90},
            {'name': 'BERT', 'icon': '🧠', 'level': 85},
            {'name': 'GPT', 'icon': '✨', 'level': 88},
            {'name': 'Natural Language Processing', 'icon': '💬', 'level': 90},
            {'name': 'Computer Vision', 'icon': '👁️', 'level': 80},
        ],
        'Frameworks & Tools': [
            {'name': 'PyTorch', 'icon': '🔥', 'level': 90},
            {'name': 'TensorFlow', 'icon': '📐', 'level': 85},
            {'name': 'LangChain', 'icon': '🔗', 'level': 92},
            {'name': 'LangGraph', 'icon': '🕸️', 'level': 90},
            {'name': 'FastAPI', 'icon': '⚡', 'level': 88},
            {'name': 'Django', 'icon': '🎯', 'level': 82},
            {'name': 'Flask', 'icon': '🍶', 'level': 80},
            {'name': 'Selenium', 'icon': '🌐', 'level': 78},
        ],
        'LLMs & AI Systems': [
            {'name': 'Prompt Engineering', 'icon': '✍️', 'level': 92},
            {'name': 'RAG Pipelines', 'icon': '📚', 'level': 90},
            {'name': 'Agent Systems', 'icon': '🧩', 'level': 88},
            {'name': 'Model Fine-tuning', 'icon': '🎯', 'level': 85},
            {'name': 'Model Integration', 'icon': '🔌', 'level': 90},
        ],
        'DevOps & Tools': [
            {'name': 'Git', 'icon': '🔧', 'level': 90},
            {'name': 'GitHub', 'icon': '🐙', 'level': 92},
            {'name': 'GitLab', 'icon': '🦊', 'level': 80},
            {'name': 'Docker', 'icon': '🐳', 'level': 85},
            {'name': 'Jira', 'icon': '📌', 'level': 78},
        ],
    },
    }

    return render(request, 'portfolio/index.html', context)


def download_cv(request):
    """Serve the CV PDF for download."""
    cv_path = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'files', 'cv.pdf')
    if os.path.exists(cv_path):
        return FileResponse(open(cv_path, 'rb'), as_attachment=True, filename='Riya_Rojesara_CV.pdf')
    else:
        # Return a friendly 404 if CV not yet uploaded
        raise Http404("CV file not found. Please add your cv.pdf to portfolio/static/files/")


@csrf_exempt
@require_POST
def chat(request):
    """Simple AI assistant — mock responses (no API key needed)."""
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip().lower()
    except (json.JSONDecodeError, AttributeError):
        return JsonResponse({'reply': "Sorry, I couldn't understand that."}, status=400)

    reply = get_bot_reply(user_message)
    return JsonResponse({'reply': reply})


def get_bot_reply(message: str) -> str:
    """Rule-based chatbot responses — customized for Riya Rojesara."""

    rules = [
    (['introduce yourself', 'tell me about yourself', 'about riya'], [
        "Hi! I'm Riya Rojesara, an AI/ML Engineer specializing in LLMs, LangChain, and intelligent agent systems. I have experience building real-world AI solutions like healthcare data extraction systems, multi-agent chatbots, and financial assistants. I'm passionate about solving practical problems using scalable AI technologies."
    ]),

    (['current role', 'current job', 'what do you do'], [
        "I am currently working as an Associate AI/ML Engineer at Artem HealthTech, where I build LLM-powered healthcare systems for extracting clinical data and generating summaries to assist doctors in decision-making."
    ]),

    (['previous experience', 'internship', 'past work'], [
        "I have worked as a Data Science Intern at Petpooja and an AI-ML Intern at Technocolabs Softwares, where I gained hands-on experience in data science, machine learning, and real-world AI applications."
    ]),

    (['education', 'degree', 'study background'], [
        "I hold an M.Sc. in Artificial Intelligence and Machine Learning from Gujarat University and a B.Sc. in Microbiology, which gives me a strong interdisciplinary foundation."
    ]),

    (['technical skills', 'skills', 'tech stack'], [
        "My technical stack includes Python, LangChain, LangGraph, PyTorch, TensorFlow, FastAPI, and databases like MongoDB and PostgreSQL. I also work extensively with LLMs, RAG pipelines, and multi-agent systems."
    ]),

    (['llm experience', 'large language models', 'llm'], [
        "I have hands-on experience with Large Language Models including prompt engineering, fine-tuning, and building applications using LangChain and LangGraph. I specialize in creating intelligent agent-based systems and retrieval pipelines."
    ]),

    (['healthcare project', 'medical project'], [
        "I built a Healthcare Data Extraction and Summarization System that fetches patient data from healthcare portals, extracts key clinical information, and generates concise summaries to help doctors make faster decisions."
    ]),

    (['chatbot project', 'langgraph project', 'chatflow'], [
        "I developed a LangGraph-based ChatFlow system with adaptive intelligence, featuring memory retention, RAG-based document querying, and fallback mechanisms using DuckDuckGo for unknown queries."
    ]),

    (['linkedin project', 'content generation'], [
        "I created an AI-powered LinkedIn Post Generator that uses LLMs to generate high-engagement posts with multiple variations based on tone, length, and topic, enabling A/B testing."
    ]),

    (['financial assistant', 'finance project'], [
        "I designed a multi-agent AI-powered financial assistant using Phidata and Groq LLMs that provides real-time stock insights using YFinance and reduces manual research effort significantly."
    ]),

    (['malaria project', 'cv project', 'computer vision'], [
        "I developed a malaria detection system using machine learning and deep learning models like SVM, Random Forest, CNN, and VGG19 for accurate classification of cell images."
    ]),

    (['rag', 'retrieval augmented generation'], [
        "I have experience building RAG pipelines that combine retrieval mechanisms with LLMs to generate accurate, context-aware responses, especially useful in chatbot and document-based systems."
    ]),

    (['frameworks', 'tools'], [
        "I work with frameworks like TensorFlow, PyTorch, LangChain, LangGraph, and FastAPI. I also use tools like Docker, Git, Selenium, and Jira for development and deployment."
    ]),

    (['databases', 'db knowledge'], [
        "I have experience working with databases such as MongoDB, PostgreSQL, and SQLite for storing and managing structured and unstructured data."
    ]),

    (['certifications', 'courses'], [
        "I have completed certifications from Google Cloud, IBM SkillsBuild, DeepLearning.AI, and Great Learning in areas like Generative AI, Prompt Engineering, Neural Networks, and NLP."
    ]),

    (['strengths', 'why hire you'], [
        "My strengths include strong problem-solving skills, hands-on experience with real-world AI systems, and the ability to build end-to-end scalable solutions using modern AI technologies like LLMs and agent frameworks."
    ]),

    (['weakness', 'areas of improvement'], [
        "I continuously work on improving model optimization and deployment efficiency, especially for large-scale LLM systems, to make them more cost-effective and performant."
    ]),

    (['tools for deployment', 'production'], [
        "For deployment, I use FastAPI, Docker, and cloud-based solutions. I focus on building scalable and production-ready AI systems."
    ]),

    (['version control', 'collaboration tools'], [
        "I use Git, GitHub, and GitLab for version control and Jira for project management and team collaboration."
    ]),

    (['location', 'where are you based'], [
        "I am based in Ahmedabad, Gujarat, India."
    ]),

    (['contact', 'email', 'connect'], [
        "You can reach me at riyarojesara008@gmail.com or connect with me via LinkedIn and GitHub."
    ])

    ]

    for keywords, responses in rules:
        if any(kw in message for kw in keywords):
            return random.choice(responses)
 
    # Default fallback
    fallbacks = [
        "Great question! I'd suggest checking the relevant section on this page, or reaching out to Riya at riyarojesara008@gmail.com 📧",
        "I'm not sure about that one! Try browsing the sections above, or drop Riya an email — she's super responsive. 😊",
        "Hmm, I don't have a specific answer for that. Feel free to connect with Riya on LinkedIn for detailed discussions!",
    ]
    return random.choice(fallbacks)
