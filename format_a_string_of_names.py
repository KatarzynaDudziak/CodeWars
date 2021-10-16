def namelist(names):
    if len(names) == 1:
        return names[0]['name']
    
    if len(names) == 0:
        return ''
    
    all_names = ', '.join(element['name']  for element in names[:-1])
    all_names = all_names + ' & ' + names[-1]['name']
    return all_names
