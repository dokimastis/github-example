from selenium import webdriver

browser = webdriver.Chrome()

#Juliet heard about a cool new online to doapp. She
# goes to check it out
browser.get('http://localhost:8080')

# She notices the page titleand header mention to-do lists
assert 'To-do' in browser title

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box (Juliet's hobby
# is fly fishing lures))

# When she hits enter, the page updates, and now the page lists
# "1: Buy peac ck feathers" as an item on her to-do list"

# There is still a text boxinviting her to add another item. She 
# enters "Use peacock feathers to make a fly". (Juliet is very methodical) 

# The page updates again, and
