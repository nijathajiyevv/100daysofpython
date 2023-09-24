# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "List": "A list of items in a particular order.",
#     "Dictionary": "A collection of key-value pairs."
# }

# # Retrieving items from dictionary
# print(programming_dictionary["Bug"])
#
# # Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


# ################################
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
# # to do-1: Create an empty dictionary called student_grades.
# student_grades = {}
# # to do-2: Write your code below to add the grades to student_grades.
# for key in student_scores:
#     score = student_scores[key]
#     if score > 90:
#         student_grades[key] = "Outstanding"
#     elif score > 80:
#         student_grades[key] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
# # 🚨 Don't change the code below 👇
# print(student_grades)


# Nesting a list in a dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
#     "India": ["Mumbai", "Delhi", "Chennai"]
# }


# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
#  Do NOT change the code above
# #
# to do: Write the function that will allow new countries
# to be added to the travel_log. 👇
# def add_new_country(country, visits, cities):
#     travel_log.append({"country": country, "visits": visits, "cities": cities})
#
#      Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
# ```



######################################
# the secret auction program

print("Welcome to the secret auction program")
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
        print("Thank you for bidding")
    elif should_continue == "yes":
        print("Sure, let's continue")
