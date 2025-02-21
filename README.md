# Shopping-Cart
"""
Overview
Many apps use some type of shopping cart, where users can add items to the cart, remove items, view the contents of the cart, and see the total. Storing this collection of items requires keeping track of a list of items and updating it in various ways.

Project Description
For this project you will create a program that stores a list of products in a shopping cart along with their prices. The user should have the ability to add items to the list, remove them, and see the total price of the cart.

For the milestone deliverable, you only need to worry about storing a list of the names of the items (not the prices yet), and only need to be able to add new items and display the list. Then, for the complete project, you'll add the ability to store the prices, remove items, and compute the total.

In addition to the functionality above, for the final project, you also need to complete the following:

Store prices as well as names.

Change the add functionality to also ask for and store the price of the item.

Change the display functionality to also display the prices of the items.

When displaying the items, display a number in front of each item. The numbers should start with 1.

Complete the option to display the total amount of the prices of all the items in the shopping cart.

Whenever prices are displayed, they should be shown to two decimal places and include the appropriate currency symbol (for example $, €, etc.)

Complete the option to remove an item from the shopping cart.

When removing an item, you should verify the following:

Both the item name and price are removed from their respective lists.

The number the user enters should be converted to a 0-based index and checked to make sure it is within the bounds of the list.

The program allows you to remove any item from the list including the first one and the last one. (Sometimes, if you have a bug in your project you might not allow removing the last item as you should.)
"""
