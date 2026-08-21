# FLOKI

Floki is a Python-based personal assistant that evolved through three different
versions, progressing from text-based commands to voice interaction
and finally to a wake-word-based system.

It can automate everyday tasks such as opening websites, providing information, checking the time, and searching Wikipedia through simple user commands.



---

# FEATURES :

# Version 1 — Text-Based

- Text-based interaction through keyboard commands
- Opens YouTube, Google, Gmail, WhatsApp and ChatGPT
- Provides the current day and time
- Searches Wikipedia for information
- Supports `exit`, `quit` and `stop` commands

Interaction : Keyboard / text

---

# VERSION 2 — Voice Assistant

- Greets the user when started
- Takes commands through the microphone
- Converts speech to text using SpeechRecognition
- Responds using text-to-speech with `pyttsx3`
- Opens websites and provides day/time information
- Searches Wikipedia and speaks the results

Interaction: 🎙️ Voice commands

---

# VERSION 3 — VALHALLA Mode

- Starts in a locked state
- Waits for the wake word **`VALHALLA`**
- Responds with **"Yes, my lord."** when activated
- Greets the user and starts accepting voice commands
- Supports the same core tasks as Version 2

Interaction: "VALHALLA" → Voice commands

---

# TECHNOLOGIES USED : 

- Python
- SpeechRecognition
- pyttsx3
- PyAudio
- Wikipedia
- pytest
- Docker
- Git & GitHub
- GitHub Actions


---

---

# PROJECT STRUCTURE :

    FLOKI/
    │
    ├── floki.py
    ├── test_floki.py
    ├── requirements.txt
    ├── Dockerfile
    ├── .dockerignore
    ├── .gitignore
    ├── README.md
    │
    ├── .github/
    │   └── workflows/
    │       └── ci.yml
    │
    └── old_versions/
        └── ...

---

#  DOCKER:

Floki includes Docker support for running the project in a
containerized environment.

### Build the Docker image

`docker build -t floki .`

### Run the container

`docker run --rm floki`

The Docker version is designed for non-interactive execution and
does not use microphone-based voice interaction.

---

# CONTINUOUS INTEGRATION  :

Floki uses GitHub Actions to automatically test the project whenever
changes are pushed to the repository.

The CI workflow:

1. Checks out the repository
2. Sets up Python
3. Installs required system dependencies
4. Installs Python dependencies
5. Runs the automated pytest tests

A successful workflow confirms that the tested core functionality
passes the automated checks.

---

# PROJECT GOAL  : 

Floki was created as a way to explore Python development, voice interaction, automated testing, Docker, Git, GitHub, and CI/CD in one project.

The project shows how a simple Python program can gradually grow into a more organized application with different ways of interacting with the user.

It also helped me understand how software can be tested, containerized, and automatically checked using a continuous integration pipeline.

Overall, Floki combines application development with basic DevOps practices, taking the project from writing Python code to testing and running it through GitHub Actions.

---

# AUTHOR :

## **_PRABHGUN SINGH_**
