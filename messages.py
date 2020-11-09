from aiogram.utils.markdown import text, bold, italic, code, pre, link
from aiogram.utils.emoji import emojize

start_message = text(emojize("Hello\!:ocean:"),
                "\n\nWith continued ocean and atmospheric warming,", italic("global sea level"), " has been rising over the past century and it continues to rise at a rate of about 1/8 of an inch per year\.",
                "\n\nThis bot is meant to demonstrate this change and predict the approximate sea level change since 1880 for a specific year in future\.",
                "\n\nUse ", italic("/help"), "to find out more about the functions of this bot\.",
                emojize("\nEnjoy\!:relaxed:"),
                emojize("\n\n:droplet:  :droplet:  :droplet:"))

references_message=text("Icon is made by", link("fjstudio", "https://www.flaticon.com/authors/fjstudio"))

help_message = text("Here are the commands you can use:",
                    "\n \- ", bold("/start"), " \- start a bot",
                    "\n \- ", bold("/help"), " \- see the list of commands",
                    "\n \- ", bold("/menu"), " \- open the menu with following buttons:",
                    "\n     \- ", bold("Algorithm"), " \- learn about how the bot is doing prediction",
                    "\n     \- ", bold("Prediction"), " \- draw a graph which predicts the sea level till a specific year",
                    "\n \- ", bold("/references"), " \- see the references",
                    emojize("\n\n:droplet:  :droplet:  :droplet:"))

menu_message = "Please choose from the options below:"

algorithm_message = text("This bot uses ", italic("linear regression "), "to calculate the approximate prediction\.",

                         "\n\n", italic("Linear regression "), "attempts to model the relationship between 2 variables \(year and sea level\) by fitting a linear equation to observed data\. On the drawn plot you can see the plot of 2 variables itself and 2 ",
                         italic("regression lines"), "\: one starts from the year 1880 annd second from the 2000\. It's done due to the significant difference in annual sea level rise starting from the beginning of the 21st century\.",

                         "\n\nA ", italic("linear regression line "), "has an equation of the form ",
                         italic("y = b0 + b1 * x"), ", where ", italic("x "), "is the explanatory variable \(year\) and ",
                         italic("y "), "is the dependent variable \(sea level\)\. The slope of the line is ",
                         italic("b1"), ", and ", italic("b0 "), "is the y\-intercept\.",

                         "\n\nMore specifically, ", italic("the least squares method "), "is used\. Briefly, it works by finding the minimal total of squares of errors \(of distance from the dot to the regression line\)\.",

                         "\n\nYou can read more on the linear regression ", link("here", "https://en.wikipedia.org/wiki/Linear_regression"), "\.",
                         emojize("\n\n:droplet:  :droplet:  :droplet:"))

prediction_message = text("Input the year for prediction, please",
                          "\n\(e\.g\. 2050\)")



unknown_message = text(emojize("Sorry, the bot can't understand this :astonished:"),
                        "\nYou can use ", italic("/help"), " to see available commands")

less_than_message = "Sorry, there's no data before 1880"

notnumeric_message = "Sorry, this isn't a year"

starts_with_zero_message = "Sorry, the year isn't supposed to start with zero"

too_big_message = "Sorry, this plot won't make sense\. Please choose a year before 4000\."