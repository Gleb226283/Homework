import json
with open('visit_log__1_.csv', 'r') as f1:
    with open('purchase_log.txt', 'r') as f2:
        with open('funnel.txt', 'w') as f3:
            for line1, line2 in zip(f1, f2):
                line1 = line1.strip()
                line2 = line2.strip()
                dict_ = json.loads(line2 + '\n')
                f3.write(line1 + ',' + dict_["category"] + '\n')
