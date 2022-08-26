from transformers import (
    BertTokenizerFast,
    EncoderDecoderConfig,
    EncoderDecoderModel,
    BertConfig
)

model_name = 'Arashasg/WikiBert2WikiBert'
tokenizer = BertTokenizerFast.from_pretrained(model_name)
config = EncoderDecoderConfig.from_pretrained(model_name)
model = EncoderDecoderModel.from_pretrained(model_name, config=config)


def generate_summary(text):
    inputs = tokenizer(text, padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    input_ids = inputs.input_ids.to("cuda")
    attention_mask = inputs.attention_mask.to("cuda")

    outputs = model.generate(input_ids, attention_mask=attention_mask)

    output_str = tokenizer.batch_decode(outputs, skip_special_tokens=True)


    return output_str

input = 'your input comes here'
summary = generate_summary(input)