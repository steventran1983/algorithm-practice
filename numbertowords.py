

under_twenty = ["","One", "Two","Three","Four","Five","Six","Seven","Eight", "Nine","Ten", "Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
tens = ["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
onver_thousand = ['thousand',"Million","Billion"]

# def num_to_words(number):
#     if number == 0: return []
#     if number < 20: return [under_twenty[number]]
#     if number < 100: return [tens[number//10]] + num_to_words(number%10)
#     if number < 1000: return [under_twenty[number//100], "Hundered"] + num_to_words(number%100) 
#     for power, chunk in enumerate(onver_thousand,1):
#         if number < 1000 ** (power+1):
#             print (power,chunk)
#             return num_to_words(number//1000**power) + [chunk] + num_to_words(number%1000**power)
        
#     # if number < 1000000: return [under_twenty[number//1000], "Thousands"] + num_to_words(number%1000) 
#     # if number < 1000:
#     #     quotient = number//1000
#     #     remainder = num_to_words(number%1000)
#     #     return under_twenty[quotient] + " Hundered " + remainder


def number_to_word(number):
    if number == 0:
        return ""
    if number < 20:
        return str(under_twenty[number])
    if number < 100:
        return str(tens[number//10] + " " + number_to_word(number%10))
    if number < 1000:
        return str(under_twenty[number//100]) + " Hundred " + number_to_word(number%100)
    if number < 1000000:
        return str(number_to_word(number//1000)) + " Thousand " + number_to_word(number%1000)
    if number < 1000000000:
        return str(number_to_word(number//1000000)) + " Million " + number_to_word(number%1000000)
    if number < 1000000000000:
        return str(number_to_word(number//1000000000)) + " Billion " + number_to_word(number%1000000000)
    
if __name__ == "__main__":
    
    final = number_to_word(123123123123)
    print(final)    


