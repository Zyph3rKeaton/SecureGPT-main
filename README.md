<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- ABOUT THE PROJECT -->
<!-- Quick Start -->
## Quick Start
1. Create a virtual environment if necessary. (`virtualenv -p python3 venv`, `source venv/bin/activate`)
2. Install the project with `pip3 install git+https://github.com/Zyph3rKeaton/SecureGPT`
3. **Ensure that you have link a payment method to your OpenAI account.** Export your API key with `export OPENAI_API_KEY='<your key here>'`,export API base with `export OPENAI_BASEURL='https://api.xxxx.xxx/v1'`if you need.
4. Test the connection with `securegpt-connection`
5. For Kali Users: use `tmux` as terminal environment. You can do so by simply run `tmux` in the native terminal.
6. To start: `securegpt --logging`


<!-- GETTING STARTED -->
## Getting Started
- **SecureGPT** is a penetration testing tool empowered by **ChatGPT**. 
- It is designed to automate the penetration testing process. It is built on top of ChatGPT and operate in an interactive mode to guide penetration testers in both overall progress and specific operations.
<!-- Common Questions -->
## Common Questions
- **Q**: What is SecureGPT?
  - **A**: SecureGPT is a penetration testing tool empowered by Large Language Models (LLMs). It is designed to automate the penetration testing process. It is built on top of ChatGPT API and operate in an interactive mode to guide penetration testers in both overall progress and specific operations.
- **Q**: Do I need to pay to use SecureGPT?
  - **A**: Yes in order to achieve the best performance. In general, you can use any LLMs you want, but you're recommended to use GPT-4 API, for which you have to [link a payment method to OpenAI](https://help.openai.com/en/collections/3943089-billing?q=API). 
- **Q**: Why GPT-4?
  - **A**: After empirical evaluation, we find that GPT-4 performs better than GPT-3.5 and other LLMs in terms of penetration testing reasoning. In fact, GPT-3.5 leads to failed test in simple tasks.
- **Q**: Why not just use GPT-4 directly?
  - **A**: We found that GPT-4 suffers from losses of context as test goes deeper. It is essential to maintain a "test status awareness" in this process. You may check the [SecureGPT Arxiv Paper](https://arxiv.org/abs/2308.06782) for details.
- **Q**: Can I use local GPT models?
  - **A**: Yes. We support local LLMs with custom parser. Look at examples [here](./securegpt/utils/APIs/gpt4all_api.py).


## Installation
SecureGPT is tested under `Python 3.10`. Other Python3 versions should work but are not tested.
### Install with pip
**SecureGPT** relies on **OpenAI API** to achieve high-quality reasoning. You may refer to the installation video [here](https://youtu.be/tGC5z14dE24).
1. Install the latest version with `pip3 install git+https://github.com/Zyph3rKeaton/SecureGPT`
   - You may also clone the project to local environment and install for better customization and development
     - `git clone https://github.com/Zyph3rKeaton/SecureGPT`
     - `cd SecureGPT`
     - `pip3 install -e .`
2. To use OpenAI API
   - **Ensure that you have link a payment method to your OpenAI account.**
   - export your API key with `export OPENAI_API_KEY='<your key here>'`
   - export API base with `export OPENAI_BASEURL='https://api.xxxx.xxx/v1'`if you need.
   - Test the connection with `securegpt-connection`
3. To verify that the connection is configured properly, you may run `securegpt-connection`. After a while, you should see some sample conversation with ChatGPT.
   - A sample output is below
   ```
   You're testing the connection for SecureGPT v 0.11.0
   #### Test connection for OpenAI api (GPT-4)
   1. You're connected with OpenAI API. You have GPT-4 access. To start SecureGPT, please use <securegpt --reasoning_model=gpt-4>
   
   #### Test connection for OpenAI api (GPT-3.5)
   2. You're connected with OpenAI API. You have GPT-3.5 access. To start SecureGPT, please use <securegpt --reasoning_model=gpt-3.5-turbo-16k>
   ```
   - notice: if you have not linked a payment method to your OpenAI account, you will see error messages.
4. The ChatGPT cookie solution is deprecated and not recommended. You may still use it by running `securegpt --reasoning_model=gpt-4 --useAPI=False`. 


### Build from Source
1. Clone the repository to your local environment.
2. Ensure that `poetry` is installed. If not, please refer to the [poetry installation guide](https://python-poetry.org/docs/).
3. 

<!-- USAGE EXAMPLES -->

## Usage
1. **You are recommended to run**:
   - (recommended) - `securegpt --reasoning_model=gpt-4-turbo` to use the latest GPT-4-turbo API.
   - `securegpt --reasoning_model=gpt-4` if you have access to GPT-4 API.
   - `securegpt --reasoning_model=gpt-3.5-turbo-16k` if you only have access to GPT-3.5 API.
   
2. To start, run `securegpt --args`.
    - `--help` show the help message
    - `--reasoning_model` is the reasoning model you want to use. 
    - `--parsing_model` is the parsing model you want to use. 
    - `--useAPI` is whether you want to use OpenAI API. By default it is set to `True`.
    - `--log_dir` is the customized log output directory. The location is a relative directory.
    - `--logging` defines if you would like to share the logs with us. By default it is set to `False`.
3. The tool works similar to *msfconsole*. Follow the guidance to perform penetration testing. 
4. In general, SecureGPT intakes commands similar to chatGPT. There are several basic commands.
   1. The commands are: 
      - `help`: show the help message.
      - `next`: key in the test execution result and get the next step.
      - `more`: let **SecureGPT** to explain more details of the current step. Also, a new sub-task solver will be created to guide the tester.
      - `todo`: show the todo list.
      - `discuss`: discuss with the **SecureGPT**.
      - `google`: search on Google. This function is still under development.
      - `quit`: exit the tool and save the output as log file (see the **reporting** section below).
   2. You can use <SHIFT + right arrow> to end your input (and <ENTER> is for next line).
   3. You may always use `TAB` to autocomplete the commands.
   4. When you're given a drop-down selection list, you can use cursor or arrow key to navigate the list. Press `ENTER` to select the item. Similarly, use <SHIFT + right arrow> to confirm selection.\
      The user can submit info about:
        * **tool**: output of the security test tool used
        * **web**: relevant content of a web page
        * **default**: whatever you want, the tool will handle it
        * **user-comments**: user comments about SecureGPT operations
5. In the sub-task handler initiated by `more`, users can execute more commands to investigate into a specific problem:
   1. The commands are:
        - `help`: show the help message.
        - `brainstorm`: let SecureGPT brainstorm on the local task for all the possible solutions.
        - `discuss`: discuss with SecureGPT about this local task.
        - `google`: search on Google. This function is still under development.
        - `continue`: exit the subtask and continue the main testing session.

### Report and Logging
1. [Update] If you would like us to collect the logs to improve the tool, please run `securegpt --logging`. We will only collect the LLM usage, without any information related to your OpenAI key.
2. After finishing the penetration testing, a report will be automatically generated in `logs` folder (if you quit with `quit` command).
3. The report can be printed in a human-readable format by running `python3 utils/report_generator.py <log file>`. A sample report `sample_secureGPT_log.txt` is also uploaded.

## Custom Model Endpoints and Local LLMs
SecureGPT now support local LLMs, but the prompts are only optimized for GPT-4.
- To use local GPT4ALL model, you may run `securegpt --reasoning_model=gpt4all --parsing_model=gpt4all`.
- To select the particular model you want to use with GPT4ALL, you may update the `module_mapping` class in `securegpt/utils/APIs/module_import.py`.
- You can also follow the examples of `module_import.py`, `gpt4all.py` and `chatgpt_api.py` to create API support for your own model.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
The tool is for educational purpose only and the author does not condone any illegal use. Use as your own risk.



<!-- CONTACT -->
## Contact the Contributors!

- Víctor Mayoral Vilches - v.mayoralv@gmail.com
- Keaton Hodgson - khodgs1@lsu.edu
- Yi Liu - yi009@e.ntu.edu.sg


<p align="right">(<a href="#readme-top">back to top</a>)</p>

