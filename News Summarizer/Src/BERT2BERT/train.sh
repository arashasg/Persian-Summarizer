!python /content/enc_dec_sum/run_summarization.py \
--model_name_or_path /content/drive/MyDrive/model/outputs/checkpoint-18138 \
--pad_to_max_length True \
--do_train False \
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