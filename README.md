# Local LLM inference with Ollama and Llama.cpp
### C.Psyd Tutorial - 9/12
This tutorial will guide you through the installation, setup, and basic usage of the Ollama and Llama.cpp CLI tools. 

Most C.Psyders have probably used HuggingFace `transformers` for running "small" pretrained langugage models like BERT or GPT-2. However, it can be much simpler to use tools like Ollama or Llama.cpp when working with large generative models. They allow you to easily:
* "split" a large model across VRAM and CPU RAM,
* enable things like flash attention,
* run quantized models,
* interact with an LLM using a chat interface, and
* prompt the model using the OpenAI API.

This is a high-level introduction focused on running LLMs on your laptop or personal computer. Of course, you might also want to make use of Cornell's G2 cluster. In that case, you should review the G2 docs and how to use SLURM. 

## Ollama
### 1. Ollama installation
Installing Ollama is very easy.
#### Linux
Run
```
curl -fsSL https://ollama.com/install.sh | sh
```
#### Mac & Windows
Download and run the appropriate installation file [here](https://ollama.com/download).

### 2. [Open WebUI](https://docs.openwebui.com/) Setup
Open WebUI is an offline, browser-based chat interface for interacting with LLMs. If you've used ChatGPT before, it's interface should feel very familiar. 

#### Linux/MacOS
First, install [`uv`](https://docs.astral.sh/uv/), "a Python package and project manager, written in Rust":
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Then, when you want to run Open WebUI, all you need to do is run 
```
DATA_DIR=~/.open-webui uvx --python 3.11 open-webui@latest serve
```
Since you probably don't want to type this out every single time you run it, consider adding something like this to your `.bashrc`/`.zshrc` (Linux) or `.bash_profile` file (Mac):
```
alias open-webui="DATA_DIR=~/.open-webui uvx --python 3.11 open-webui@latest serve &"
```
If Open WebUI is running, open your web browser and navigate to `http://localhost:8080`. Create an account and you should see a chat interface!

#### Windows (Powershell)
Install `uv`:
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
To run Open WebUI, run 
```
$env:DATA_DIR="C:\open-webui\data"; uvx --python 3.11 open-webui@latest serve
```
*I don't know how you set aliases in Powershell, but you can probably figure that part out on your own.*

Navigate to `http://localhost:8080`, create an account, and you're good to go!

### 3. Downloading Models
Ollama might have installed a small model by default. To check what models you currently have installed, run
```
ollama list
```
If you have models installed, you should see a table with lines like:
```
NAME                                ID              SIZE      MODIFIED 
deepseek-r1:8b-0528-qwen3-q4_K_M    6995872bfe4c    5.2 GB    13 days ago
```
*(Widen your window/zoom out if this looks garbled here)*

Ollama makes it easy to download new models. 