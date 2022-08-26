# BERT2BERT
## How to train
In order to train a new model from scrach based on a pre-trained BERT language model you have to do the following steps. <br>
`train.sh` is a bash script provided to help train a new model. In this file you need to specify the name/path of the pre-trained BERT language model and hyper-paramters that you want to fine tune the model based on them. one example that we have used for training is as follows. We will call our summarization model ParsBERT-sum.
```
!python /content/enc_dec_sum/run_summarization.py \
--model_name_or_path HooshvareLab/bert-base-parsbert-ner-uncased \
--pad_to_max_length True \
--do_train \
--do_eval \
--early_stopping_patience 2 \
--do_predict \
--load_best_model_at_end \
--num_beams 4 \
--max_source_length 512 \
--max_target_length 128 \
--save_strategy epoch \
--evaluation_strategy epoch \
--train_file ./data/train.csv \
--validation_file ./data/val.csv \
--test_file ./data/test.csv \
--output_dir ./outputs \
--logging_dir ./outputs/logs \
--predict_with_generate \
--text_column News \
--summary_column Summarization \
--preprocessing_num_workers 1 \
--dataloader_num_workers 1 \
--gradient_accumulation_steps 1 \
--per_device_train_batch_size 4 \
--per_device_train_batch_size 4 \
--num_train_epochs 1 \
--logging_steps 500 \
--warmup_steps 1000
```
## Using ParsBERT-sum Model for Summarization
In order to see how this model summarize a never before seen text you need to run `app.py`. In this file there exist a variable which is called **text**. this variable must be equal to the text you want to summarize.  
## Results
ParsBERT-sum model was evaluated on a test dataset based on Tasnim and Asr-Iran news datasets. For evaluation we've used *ROUGE* and *BERTScore* metrics. The reported resualts are as follows:

**Rouge**:
Model | R1 | R2 | RL
--- | --- | --- | ---
**ParsBERT-sum** | 32.85 | 17.45 | 28.5

**BERTScore**:
Model | Precision | Recall | F1
--- | --- | --- | ---
**ParsBERT-sum** | 0.74 | 0.72 | 0.73