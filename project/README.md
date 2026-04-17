# Project - Evolution of agents

This project can be done **in pairs**.
It focuses on the evolution of agents using the [EvoGym](https://evolutiongym.github.io) suite. 
To get started with evogym, see the [documentation](https://evolutiongym.github.io/documentation).

[Neuroevolution in evogym notebook](https://github.com/d9w/evolution/blob/master/project/evogym.ipynb)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/d9w/evolution/blob/master/project/evogym.ipynb)

[Notebook for gifs](https://github.com/d9w/evolution/blob/master/project/gif.ipynb)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/d9w/evolution/blob/master/project/gif.ipynb)


For this project, you'll run the code locally. To build the minimal environment for this project, you'll find the necessary information in this [file](https://github.com/d9w/evolution/blob/master/project/setup_env.md).
You can fork [this minimal repo](https://github.com/echigot/project_evolution) that contains the main project files.

You will need to evolve movement policies for three tasks independently:

+ Walker-v0 (easy)
+ Thrower-v0 (medium)
+ Climb-v2 (hard) 

You have a budget of 5.000.000 **steps** for evolution 
(for example, a population of 10 for 1000 generations with simulation of 500 steps).  
Each evaluation can have 500 maximum steps, but you can reduce this in the early stages of evolution if needed.
You choose the evolutionary algorithm, gene representation, and evolutionary
hyperparameters, but you must demonstrate that you only used the allocated evaluation budget.
To do so, you might want to show optimization logs, evolution plots, ... (you can take inspiration from research
papers in this domain to come up with nice and interesting visualizations).
The goal is to obtain the best score **independently** on each task---but you might also want to try to optimize something
that solves all three tasks at once. 
Scores should be shown in your final presentation as the average best
score over **at least 2 independent evolutions**.

For each task, points will be allocated to teams depending on performance (see below).

---

## Presentation & Evaluation (20 points total)

- **Date:** Thursday, May 7  
- **Duration:** ~10 minutes per team  
- **Language:** French or English, you can choose what feels more comfortable to you.
- **Format:** You may include videos, code snippets, methodology, parameters, and unsuccessful attempts.  
- **Interaction:** All teams are encouraged to ask and answer questions.

### Grading Criteria
*(Same base score per team member; small adjustments possible via Q&A)*

- **4 pts – Performance:** Ranking across the three tasks (averaged and normalized)  
- **8 pts – Clarity:** How clearly you explain your work so it can be understood and reproduced  
- **2 pts – Visualizations:** Quality and usefulness of visual outputs  
- **1 pt – Novelty:** Creativity or originality in approach  
- **2 pts – Questions:** Asking and answering after presentations 
- **3 pts – Technical Soundness:** Rigor and correctness of experiments and methods

---

## Code sources

You can use the code provided during class for your evolutionary algorithms, and you can also use any code online. Some popular libraries are:

+ [cmaes](https://github.com/CyberAgentAILab/cmaes)
+ [pycma](https://github.com/CMA-ES/pycma)
+ [pymoo](https://pymoo.org/)
+ [pyribs](https://pyribs.org/)
+ [neat-python](https://github.com/CodeReclaimers/neat-python)
+ [gplearn](https://github.com/trevorstephens/gplearn)
+ [pycgp](https://github.com/scussatb/pyCGP)
+ [DEAP](https://github.com/DEAP/deap)
