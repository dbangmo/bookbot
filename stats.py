#function to count words
def get_num_words(text):
    words = text.split()
    return len(words)

#make a starting dictionary, then for loop the characters in the text by making lower case then counting
def get_characters_dict(text):
    chars ={}
    for c in text:
        lowered=c.lower()
        if lowered in chars:
            chars[lowered] +=1
        else:
            chars[lowered] =1
    return chars

#Sorting the dictionary
def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
       sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    #sort the list using sort_on
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list    