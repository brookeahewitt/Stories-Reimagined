# **Stories-Reimagined**

### **Setup Instructions**

1. **Download Ollama**  
   Visit [Ollama's website](https://ollama.com/) to download the tool

2. **Get Llama 3.1**  
   Run the following command to pull the Llama 3.1:8b model:
   
   `ollama pull llama3.1:8b`

4. **View Available Models**  
   To see a list of Llama models that you have downloaded, use:

   `ollama list`


6. **Create a Virtual Environment**  
    Before setting up, delete the existing `ollama` folder. Then, create a new virtual environment:
   
    `python -m venv ollama`


8. **Activate the Virtual Environment**  
   Run the following command to activate the virtual environment:
   
   `. ollama/Scripts/activate`


10. **Install Ollama Package**  
    Install the Ollama Python package with:

    `pip install ollama`


12. **Run the Program**  
    To run the StoryTeller program, use:

    `python ./StoryTeller.py`


---

### **Available Flags**

- `--story`  
Path to the input `.txt` file. If not provided, the story idea will be prompted by the user.

- `--human`  
If `true`, story feedback in Tree of Thoughts will be provided by human input, rather than semi-random criticism.

- `--depth`  
Specifies the depth for Tree of Thoughts. Default is `2`.

- `--rounds`  
Defines the number of rounds for Multi-Agent Debate between the Proponent and Opponent. Default is `2`.

---

### **Troubleshooting**

If you encounter an error while running the program, open a new terminal window and run:

`ollama serve`

Then, try running the program again.

---

### **Helpful Links**

- [Ollama GitHub Repository](https://github.com/RamiKrispin/ollama-poc?tab=readme-ov-file)  
- [Ollama Tutorial Video](https://www.youtube.com/watch?v=sdwTN3d-KIQ)
