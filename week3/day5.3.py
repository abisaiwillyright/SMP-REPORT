# Days on Protocol

def protocol_summary(protocol_list):
    unique = list(set(protocol_list))
    summary = {}
    for P in unique:
        summary[P] = protocol_list.count(P)
    return summary
    
protocols =['OMAD', '2MAD', 'OMAD', 'Autophagy Marathon', 'OMAD', '2MAD', 'OMAD', 'Autophagy Marathon']
result = protocol_summary(protocols)

print('\n----Protocol Summary----')
for protocol, days in result.items():
    print(f' {protocol}: {days} day(s)')
