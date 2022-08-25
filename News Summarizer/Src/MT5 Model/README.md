Project requirements for implementation in Google colab:
```
!pip install transformers 
!pip install sentencepiece 
```



How to use:
```
from transformers import MT5Tokenizer, MT5ForConditionalGeneration
tokenizer = MT5Tokenizer.from_pretrained("google/mt5-small")
fine = MT5ForConditionalGeneration.from_pretrained("nafisehNik/mt5-persian-summary")
```


Set or change hyperparameters:
```
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
```


Text is our input and result is our output:
```
text = ''
result = generate_summary(model=fine, abstract=text, num_beams=2, max_output_length=120)
```