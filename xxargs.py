#xxargs এর বেলা **details নিতে হয়

def students(**details):
    print(details["Name"])      #details এর ভিতরে [এখানে যা দিবে সেটা আউটপুট দেখাবে] 

students(ID = 8137, Name = "MD Mafujul Hasan")