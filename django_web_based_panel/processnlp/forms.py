import time

import torch
from datasets import Dataset

from django.utils.translation import gettext as _
from django import forms
from django.core.validators import FileExtensionValidator

from processnlp.models import NlpModel
from processnlp.model_1.helper_bert2bert import Helper


from transformers import  AutoModelForSeq2SeqLM, MT5Tokenizer

# MODEL 1
helper = Helper("processnlp/model_1/checkpoint-18138", do_tr_lowercase=False, source_prefix="",
                max_source_length=512,
                max_target_length=120, num_beams=4, ngram_blocking_size=3, early_stopping=None,
                use_cuda=torch.cuda.is_available(),
                batch_size=1, language="fa")
#########

# MODEL 2
fine = AutoModelForSeq2SeqLM.from_pretrained('processnlp/model_2/mt5-small-fine-tune-10', local_files_only=True)
tokenizer = MT5Tokenizer.from_pretrained("processnlp/model_2/mt5-small", local_files_only=True)
def generate_summary(model, abstract, num_beams = 2, repetition_penalty = 1.0,
                                length_penalty = 2.0, early_stopping = True, max_output_length = 120):
    source_encoding=tokenizer(abstract, max_length=1000, padding="max_length", truncation=True, return_attention_mask=True, add_special_tokens=True, return_tensors="pt")

    generated_ids=model.generate(
        input_ids=source_encoding["input_ids"],
        attention_mask=source_encoding["attention_mask"],
        num_beams=num_beams,
        max_length=max_output_length,
        repetition_penalty=repetition_penalty,
        length_penalty=length_penalty,
        early_stopping=early_stopping,
        use_cache=True
        )

    preds=[tokenizer.decode(gen_id, skip_special_tokens=True, clean_up_tokenization_spaces=True) 
        for gen_id in generated_ids]

    return "".join(preds)
##########

# MODEL 3
fine3 = AutoModelForSeq2SeqLM.from_pretrained('processnlp/model_3/mt5-small-fine-tune-100', local_files_only=True)
tokenizer3 = MT5Tokenizer.from_pretrained("processnlp/model_2/mt5-small", local_files_only=True)
##########

# MODEL 4
from transformers import (
    BertTokenizerFast,
    EncoderDecoderConfig,
    EncoderDecoderModel,
)
tokenizer4 = BertTokenizerFast.from_pretrained('processnlp/model_4/WikiBert2WikiBert', local_files_only=True)
config4 = EncoderDecoderConfig.from_pretrained('processnlp/model_4/WikiBert2WikiBert', local_files_only=True)
model4 = EncoderDecoderModel.from_pretrained('processnlp/model_4/WikiBert2WikiBert', local_files_only=True, config=config4)
def generate_summary4(text):
    inputs = tokenizer4(text, padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    input_ids = inputs.input_ids
    attention_mask = inputs.attention_mask
    outputs = model4.generate(input_ids, attention_mask=attention_mask)
    output_str = tokenizer4.batch_decode(outputs, skip_special_tokens=True)
    return output_str
##########

class NlpModelForm(forms.Form):
    nlp_model_num = forms.ChoiceField(choices=NlpModel.NLP_MODEL_NUM_CHOICES)
    original_text = forms.CharField(required=False)
    text_file = forms.FileField(validators=[FileExtensionValidator(['txt', ]), ], required=False)

    def clean(self):
        cleaned_data = self.cleaned_data
        file, text = cleaned_data.get('text_file'), cleaned_data.get('original_text')
        if not (text or file):
            raise forms.ValidationError(_('You must either upload a file or fill the text field.'))
        return cleaned_data

    def save(self):
        if self.errors:
            raise ValueError('you must call is_valid before calling save method.')
        cleaned_data = self.cleaned_data
        file, text = cleaned_data.get('text_file'), cleaned_data.get('original_text')
        original_text = file.read().decode('utf-8') if file else text
        nlp_model_num = cleaned_data.get('nlp_model_num')
        start_time = time.time()
        if nlp_model_num == '1':
            inp_dict = {"input": [original_text.replace('\n', '')]}
            test_data = Dataset.from_dict(inp_dict)
            test_data = test_data.map(
                helper.preprocess_function,
                batched=True,
                load_from_cache_file=False
            )
            result = test_data.map(helper.generate_summary, batched=True, batch_size=helper.batch_size, load_from_cache_file=False)
            summary = result['predictions'][0]
        elif nlp_model_num == '2':
            summary = generate_summary(model=fine, abstract=original_text, num_beams=2, max_output_length=120)
        elif nlp_model_num == '3':
            summary = generate_summary(model=fine3, abstract=original_text, num_beams=2, max_output_length=120)
        elif nlp_model_num == '4':
            summary = generate_summary4(original_text)
        else:
            summary = text
        end_time = time.time()
        obj = NlpModel.objects.create(
            original_text=original_text,
            nlp_model_num=nlp_model_num,
            summary=summary,
            processing_time=round(end_time - start_time, 5)
        )
        return obj
