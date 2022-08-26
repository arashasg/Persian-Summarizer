
from transformers import  AutoModelForSeq2SeqLM, MT5Tokenizer

# add model path to the fine
fine = AutoModelForSeq2SeqLM.from_pretrained('./mt5-small-fine-tune-10', local_files_only=True)

tokenizer = MT5Tokenizer.from_pretrained("./download/mt5-small", local_files_only=True)


# method for summary generation, using the global model and tokenizer
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


#input 
text = ''' 
به گزارش شانا، علی کاردر امروز (۲۷ دی ماه) در مراسم تودیع محسن قمصری، مدیر سابق امور بین الملل شرکت ملی نفت ایران و معارفه سعید خوشرو، مدیر جدید امور بین الملل این شرکت، گفت: مدیریت امور بین‎الملل به عنوان یکی از تاثیرگذارترین مدیریت‌های شرکت ملی نفت ایران در دوران تحریم‌های ظالمانه غرب علیه کشورمان بسیار هوشمندانه عمل کرد و ما توانستیم به خوبی از عهده تحریم‌ها برآییم. [n] وی افزود: مجموعه امور بین الملل در همه دوران‌ها با سختی‌ها و مشکلات بسیاری مواجه بوده است، به ویژه در دوره اخیر به دلیل مسائل پیرامون تحریم وظیفه سنگینی بر عهده داشت که با تدبیر مدیریت خوب این مجموعه سربلند از آن بیرون آمد. [n] کاردر با قدردانی از زحمات محسن قمصری، به سلامت مدیریت امور بین الملل این شرکت اشاره کرد و افزود: محوریت کار مدیریت اموربین الملل سلامت مالی بوده است. [n] وی بر ضرورت نهادینه سازی جوانگرایی در مدیریت شرکت ملی نفت ایران تاکید کرد و گفت: مدیریت امور بین الملل در پرورش نیروهای زبده و کارآزموده آنچنان قوی عملکرده است که برای انتخاب مدیر جدید مشکلی وجود نداشت. [n] کاردر، حرفه‎ای‎گری و کار استاندارد را از ویژگی‌های مدیران این مدیریت برشمرد و گفت: نگاه جامع، خلاقیت و نوآوری و بکارگیری نیروهای جوان باید همچنان مد نظر مدیریت جدید امور بین الملل شرکت ملی نفت ایران باشد.
'''
result = generate_summary(model=fine, abstract=text, num_beams=2, max_output_length=120)


print(result)