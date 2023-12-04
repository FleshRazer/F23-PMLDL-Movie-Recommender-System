# F23-PMLDL-Movie-Recommender-System

<p align="center">
  <a href="reports/task-description.md">Task Description</a> •
  <a href="notebooks/">Notebooks</a> •
  <a href="reports/report.md">Report</a>
</p>

### Set up Repository

To unzip the repository, create Python virtual environment and install the dependencies, run the following script

```bash
source setup.bash
```

### Repository Structure

```
F23-PMLDL-Movie-Recommender-System
├── README.md               # The top-level README
│
├── data
│   ├── external            # Data from third party sources
│   ├── interim             # Intermediate data that has been transformed.
│   └── raw                 # The original, immutable data
│
├── models                  # Trained and serialized models, final checkpoints
│
├── notebooks               #  Jupyter notebooks. Naming convention is a number (for ordering),
│                               and a short delimited description, e.g.
│                               "1.0-initial-data-exporation.ipynb"            
│ 
├── references              # Data dictionaries, manuals, and all other explanatory materials.
│
├── reports
│   ├── figures             # Generated graphics and figures to be used in reporting
│   └── final_report.pdf    # Report containing data exploration, solution exploration, training process, and evaluation
│
└── benchmark
    ├── data                # dataset used for evaluation 
    └── evaluate.py         # script that performs evaluation of the given model
```
