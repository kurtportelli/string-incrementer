def increment_string(strng):
    import re
    
    if not strng:
        return strng + '1'
    if strng[-1].isalpha():
        return strng + '1'
    
    old_num = re.search(r'\d+$', strng)[0]
    old_len = len(old_num)
    
    new_num = str(int(old_num) + 1)
    new_len = len(new_num)
    
    result = strng[:-old_len]
    
    for i in range(old_len - new_len):
        result += '0'
        
    result += new_num
    
    return result
