Quick and dirty project for work. Meant for use when dealing with objects/classes with a large number of properties, so you'll have a large number of lines that are almost identical except for the property name. 

eg. Your requirements doc gives you the following fields on your Product class:

Id, Name, Description, Price, Stock

In this program, you would enter something like: 

public * * { get; set; } 

as your formatted string, and then for your variables lists, you'd enter:

int, string, string, double, int
ID, Name, Description, Price, Stock

And the program would output: 

public int ID { get; set; } 
public string Name { get; set; } 
public string Description { get; set; }
public double Price { get; set; }
public int Stock { get; set; }

Thus allowing you to generate any number of lines with just a few copy-paste executions. 

The application can handle up to 3 variables per line. There's also not a lot of error-handling/crash-proofing, that'll get added as I get time. 
