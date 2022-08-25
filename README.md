# ParsSum: Persian Summarizers with Transformer-Based Encoder-Decoder Architectures

In this repository, we present four summarizer models in the Persian
language. We have also evaluated our models using BertScore, Rouge-1, Rouge-2, and Rouge-l metrics. The evaluations' results represent that our models' performance is so close, if not equal, to SOTA Persian summarizer models. Lack of access to GPU and powerful processors hindered our progress, but the promising results we achieved through assessing our models make it crystal clear that the results can improve by training our models for afew more epochs. 

Our contribution to the community is not confined to training new models. Additionally, we have crawled and presented two new news article datasets that can be used for summarization tasks.

Finally, each folder of the repository contains readme files for making our code as simple as possible to comprehend.

#### Project Structure:
```
├───Docs
│
├───News Summarizer
│   ├───Data   # The links to datasets are presented through a readme.md file here.
│   ├───Models # The steps taken in order to reach the final models are presented here through Jupyter Notebooks.
│   └───Src    # Here, we have attached python files containing code to get result from the models.
│       ├───MT5 Model 
│       └───WikiBert2WikiBert
├───Resources  # Notebook files and codes to crawl and clean the datasets are here.
│   └───hoshvare dataset
└───UI        # The files for django web application implementation are presented here.
```

#### Citation

If you use any part of this repository in your research, please cite it using the following BibTex entry.

```
@software{Asgari_ParsSum_Persian_Summarizers_2022,
author = {Asgari, Arash and Nikeghbal, Nafise and Abdollahi Moghadam, Behdad and Esmaeili, Elyas and Hajihoseini, Hadi},
month = {8},
title = {{ParsSum: Persian Summarizers with Transformer-Based Encoder-Decoder Architectures}},
url = {github.com/arashasg/persian-news-summarizer},
version = {1.0.0},
year = {2022}
}
```