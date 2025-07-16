from clf_regex import classify_with_regex
from clf_bert import classify_with_bert
from clf_llm import classify_with_llm
import pandas as pd

def classify_csv(input_file):
    df=pd.read_csv(input_file)
    logs = list(zip(df['source'], df['log_message']))
    labels = classify_all_logs(logs)
    df['Label'] = labels
    df.to_csv('./Resources/output.csv', index=False)


def classify_log(source,log_message):
    if source=='LegacyCRM':
        label=classify_with_llm(log_message)
    else:
        label=classify_with_regex(log_message)
        if label is None:
            label=classify_with_bert(log_message)

    return label
        
def classify_all_logs(logs):
    labels = []
    for source,log_message in logs:
        label = classify_log(source, log_message)
        labels.append(label)
    return labels

if __name__ == "__main__":
    classify_csv('./Resources/test.csv')
    # logs = [
    #     ("ModernCRM", "IP 192.168.133.114 blocked due to potential attack"),
    #     ("BillingSystem", "User user12345 logged in."),
    #     ("AnalyticsEngine", "File data_6957.csv uploaded successfully by user User265."),
    #     ("AnalyticsEngine", "Backup completed successfully."),
    #     ("ModernHR", "GET /v2/54fadb412c4e40cdbaed9335e4c35a9e/servers/detail HTTP/1.1 RCODE  200 len: 1583 time: 0.1878400"),
    #     ("ModernHR", "Admin access escalation detected for user 9429"),
    #     ("LegacyCRM", "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."),
    #     ("LegacyCRM", "Invoice generation process aborted for order ID 8910 due to invalid tax calculation module."),
    #     ("LegacyCRM", "The 'BulkEmailSender' feature is no longer supported. Use 'EmailCampaignManager' for improved functionality."),
    #     ("LegacyCRM", " The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025")
    # ]
    # labels = classify_all_logs(logs)
    # print(labels)