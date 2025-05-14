# 436-Portfolio

Chapter 5 Activity Marks & Channels

An activity I completed was Marks and Channels with respect to the many different visualizations I looked at. Throughout the activity, I analyzed several different visualizations, ranging from wind predictions to income distributions, and broke them down using the concepts of marks (points, lines, areas) and channels (position, color, size, shape, etc.). 

One of the most valuable takeaways was learning how magnitude channels (like size, position, and luminance) work best for ordered, quantitative data, while identity channels (like color hue and shape) are better suited for categorical data. I saw this clearly in the vegetable consumption chart, where color represented different types of vegetables (categorical) and area size represented how much was eaten each year (quantitative). This showcased why certain channels are more effective than others, depending on the data type and what the user needs to understand.

Finally, comparing the effectiveness of visual encodings in different charts, like the clean dot plots vs. the more complex wind forecast, showed me how clarity can make or break a visualization. I learned that too many competing colors or unclear encoding choices can overwhelm users and reduce the visualization’s effectiveness. Overall, this activity taught me how to "read" and evaluate visualizations with a designer’s mindset. Understanding marks and channels gave me the tools to break down a visual piece and assess whether it’s doing a good job of representing data.


Chapter 11+12 Activity: Handling Complexity 

One Activity I completed was Handling Complexity in data visualizations, which deepened my understanding of how interactive visual techniques can support users in navigating large, dense datasets. One of the key visualizations I chose to explore was the EdgeMaps interface, primarily because it was the most engaging. What stood out to me was the ability to click on each point to reveal new information, allowing for a dynamic exploration of the data rather than passively consuming it. 

Through this activity, I learned to analyze the pros and cons of various interaction techniques. For instance, while the clicking feature allowed users to focus on one node and learn more about its connections, it became overwhelming when nodes had too many links. Without the ability to zoom in and out, it was difficult to follow specific data points. This highlighted the importance of balancing information density with user control in interface design.

In all, the activity really helped me connect this individual exploration to our group project. I suggested that we consider using juxtaposition and superimposition as techniques to handle complexity in our own dashboard, since our project involves comparing multiple datasets and displaying them side-by-side. Overall, this assignment taught me how certain design choices, such as interactivity, layout, and encoding, can make complex data more accessible.


Refining Assignment 1

Reflection:

In refining Assignment 1, I used Seaborn to recreate the “Top 500 Hollywood Movies by Worldwide Box Office Gross” visualization. Previously, I worked with Matplotlib to make a bubble chart that displays major global data breaches, and also used Matplotlib for another visualization to analyze the global trend in women's representation in parliaments from 1990 to 2018. I also previously completed this same task, “Top 500 Hollywood Movies by Worldwide Box Office Gross” visualization, using Plotly, which allowed me to reflect on the strengths and limitations of each tool.

Using Seaborn this time felt like a solid middle ground between Matplotlib's static design power and Plotly's interactivity. Seaborn made it relatively easy to build a clean, professional scatter plot with minimal code. I appreciated how Seaborn handled grouping and coloring by the decade column using a defined color palette. The addition of text annotations for the top movie of each decade helped me replicate the original chart’s storytelling aspect, and overall, the output felt clean and easy to interpret.

However, I had limitations. Seaborn does not support hover interactions, which means users can't explore the rest of the dataset dynamically. While static labeling worked for highlighting standout movies like Titanic, Avatar, or Spider-Man: No Way Home, it didn’t allow for deeper exploration like Plotly does. If someone wanted to learn about less known films in the visualization, there would be no way to do that without switching to a fully interactive tool.

In comparison, Plotly provided a much smoother interactive experience. It allowed users to hover over every point to see movie titles, years, and gross revenue instantly, which is more user-focused. Its styling is also modern and clean, though customizing labels and fonts required some tweaking. For large datasets like the one used, Plotly’s hover feature is important for accessibility and engagement. In contrast, working with Matplotlib, previously during assignment 1, while it is powerful and foundational to both Plotly and Seaborn. It required the most manual work. Plot customization, labeling, and formatting were not as concise as Seaborn’s, and there was no interactivity at all without integrating additional libraries. That said, it offers the most control for detailed visual tweaking, which can be helpful in publication-quality graphics.

In all, each tool had its unique strengths. Seaborn was ideal for a quick, visually pleasing static chart, Plotly was for interactivity and user-focused, and Matplotlib was best for manual fine-tuning. Furthermore, Plotly still stands out among some of the other tools used. 


Refining Misleading Vis

Reflection:

Why is this visualization so misleading?

    -Users will assume bigger bubbles mean better quality, but it's actually just how popular the book is. Thus, a book with a 1-star average but 1M ratings will look massive and important.
    
    -Changing x-tick labels from numbers to biases (Low, Meh, Perfect) tricks the user into thinking the ratings are categorical.
    
    -Using num_pages to color the bubbles with no legend implies a pattern when there is none. Users will try to     see"patterns between book length and review count.
    
    -Users have no idea what the color actually means, so they assume it matters positively.
    
    -The lack of reference makes it hard to estimate any values at all, removing the user’s ability to understand the vis.

The ramifications:

The ramifications of the misleading visualization are that publishers could falsely believe longer books or more reviewed books are automatically higher quality, influencing what gets published or promoted. This also encourages poor analytical practices by showing correlation as causation and misusing visual encoding principles. Furthermore, users with little data literacy may take away the wrong message, like “length causes quality” or “popularity equals value.” Overall, this visualization diminishes the credibility of honest data science work. Users may become skeptical of all visual analytics, even the good ones.
