from transformers import BertTokenizer, BertForSequenceClassification
from torch.nn.functional import softmax

labels = ["Bilim Kurgu", "Ekonomi", "İslam", "Polisiye", "Romantik", "Sağlık", "Spor"]

tokenizer = BertTokenizer.from_pretrained('dbmdz/bert-base-turkish-uncased', do_lower_case=True)
model_path = "bert_model"
model = BertForSequenceClassification.from_pretrained(model_path, num_labels=7)

def main(metin):
    inputs = tokenizer(metin, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    probs = softmax(outputs.logits, dim=1).detach().numpy()[0]
    predicted_label_index = int(probs.argmax())
    print(labels[predicted_label_index])
    return labels[predicted_label_index]

