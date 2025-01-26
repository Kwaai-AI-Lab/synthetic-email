# Synthetic Email
Welcome to the synthetic data repository created for Jane Lila. This repository contains synthetic data generated using Large Language Models (LLMs) (OpenAI gpt-3.5-turbo and Llama-2 7b chat) and augmented through a custom data augmentation code. Below is a guide to help you navigate and utilize the resources available in this repository effectively.

## Structure
#### Datasets
The compilation of synthetic email can be found within the `synthetic_email` text file in the `app` directory. T
Each email is labeled with `Subject`, `body` and `salutations` and organized for easy access. When using this, you can edit and provide synthetic names (if needed, for any words in the curly or square brackets).
Each email is seperated by ```========```.

#### Data augmentation
Utilize the data augmentation code located in the directory to randomly generate single or multiple instances of emails, either individually or in repetition. This approach can be employed when the dataset categories are insufficiently represented.
Note: Excessive utilization of this (kinds of) dataset may result in an increase in noise levels during the training process.

## Contributing to the Repository
##### Improvements and Feedback
We welcome contributions, feedback, and suggestions for enhancing the repository.

##### Additional Data Sets
If you have generated additional synthetic data sets or have ideas for new data augmentation techniques, we encourage you to contribute them to the repository.
Follow the guidelines for submitting new data sets and provide relevant documentation for easy integration.