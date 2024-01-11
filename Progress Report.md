---
attachments: [Clipboard_2024-01-11-07-11-38.png, Clipboard_2024-01-11-08-15-09.png, Clipboard_2024-01-11-08-15-28.png, Clipboard_2024-01-11-08-28-01.png]
title: Progress Report
created: '2024-01-10T07:01:25.990Z'
modified: '2024-01-11T00:47:37.849Z'
---

# Progress Report

## Python Modules
https://github.com/paolo-jpl/python-modules

![pmod!](https://i.imgur.com/D7GuE2p.png)

Python training modules are presented through notebooks (.ipynb) interjecting text explainations and walkthroughs between segments of code. For more manageable version control, notebooks are instead stored in the repository as python scripts (.py). 

Scripts can be viewed and ran as a notebook on **Jupyterlab** by installing an extension.

![pmod](https://i.imgur.com/1VsOVGv.png)

Modules will occasionally demonstrate and explain logical or syntactical errors and error messages.

![pmod](https://i.imgur.com/kZynixr.png)

Some functions that are more complex will have a breakdown each parameter and how they are used.
![pmod](https://i.imgur.com/WBB2V9v.png)

The end of each module will present an assignment that applies what was shown. All assignments are fairly short and should take around 5 minutes to finish. Although, non-programmers should be projected to finish around 10-20 minutes.

![pmod!](https://i.imgur.com/cd44s2R.png)

### Outline of topics
#### Module 1
![pmod](https://i.imgur.com/l20N4sc.png)
- Variables
  - data types
  - data type conversion
  - naming convention 
  - obtaining user input
  - arithmetic operations
- String operations
  - concatenation
  - string indexing/slicing
  - substring manipulation
#### Module 2
![pmod](https://i.imgur.com/80xVS5y.png)
- Lists
  - indexing
  - Adding/appending items
  - removing items
  - sorting items
  - 2-Dimensional lists
- Conditional Statements
  - if/elif statements
  - boolean operators
- Looping
  - While loop vs For loop
  - exiting a loop (break or exit flags)

#### Module 3
![pmod](https://i.imgur.com/h8MlW98.png)
- Functions
  - defining a custom function
  - parameters + return values
  - lambda functions
- Classes
  - instatiating a class
  - accessing attributes/functions of an instance
- Importing and using custom scripts
- Understanding documentation
- map,filter,reduce

#### Module 4
![pmod](https://i.imgur.com/WfRqQWM.png)
- Dataframes 
  - importing and exporting dataframes (to and from .csv)
  - indexing (Loc an iLoc)
  - Data cleaning
    - handling missing values
    - handling inconsistent data entry
  - Data Aggregation
    - merging
    - join (left,right,inner,outer)


#### Module 5
![pmod](https://i.imgur.com/NX5wgwA.png)
- matplotlib + plotly
  - generate visualization: bar, scatter, donut, correlation, boxplot, histogram, line
- general rules of data visualization
- selecting a visualization library


#### Advanced Topics (for continuation)
- Error handling + reading errors
- Understanding documentation (for pre-existing libraries)
- Larger assignment that applies multiple concepts
- Environment setup (pip)

Requires knowledge of specific use cases in relation to the work.
- Object Oriented Programming
- OpenCV + Image Processing
- Basic Machine Learning
---
## Crowd Counting
https://github.com/paolo-jpl/crowdml

Goal: assessment of space, identifying problematic/crowded areas

![ccml](https://i.imgur.com/BIUMfNQ.png)

usage of object detection models vs crowd counting models

![ccml](https://i.imgur.com/pc4yfPI.png)

most modern crowd counting models address the issue through **density mapping** and estimation rather than 'detect and count'

highest performing models in terms of counting accuracy focus on point-based framework and locating individuals rather than identifying crowd density.

accuracy tradeoff may not be as relevant to accomplishing the goal

Visualization may not necessarily be as useful in sparse crowds. 

![ccml](https://i.imgur.com/tty8Wzi.png)

## Model Weaknesses

Output latency may be an issue. While video input can be possible by taking and processing individual frames, there may be delays in handling live footage especially with the hardware limitations of a drone.

Some weaknesses in **counting accuracy** can be attributed to gaps in the dataset. Most images in benchmark datasets are taken under daylight rather than artificial lighting, making it miss some crowds in the background. 

![ccml](https://i.imgur.com/DrZeVbD.png)

In detection, the model does not appear to have a hard perference for certain perspectives or a specific orientation of the head. However, **top-down aerial shots** (which are sparse in the datasets) have unreliable counts. Image below has an inflate count.

![ccml](https://i.imgur.com/fZpNHih.png)

As mentioned, crowd counting models with density mapping have the drawback of losing the precise position of each head. The weight of this weakness will depend on the use case.

Crowd counting models focus on detection of heads so the visualization does not account for the space taken by the rest of the person.

Perspective bias
![ccml](https://i.imgur.com/5w68EUN.png)
![ccml](https://i.imgur.com/mK3nu0S.png)

Custom specialized datasets can be used to retrain the model to perform better for its specific task but it should be noted that both gathering and annotating the images is a very laborious task.

