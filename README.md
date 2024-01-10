# crowdml

This is a modified demo implementation of the original [Distribution Matching for Crowd Counting](https://paperswithcode.com/paper/distribution-matching-for-crowd-counting) model. Refer to the original [source code](https://github.com/cvlab-stonybrook/DM-Count) for prerequisite libraries. This repository only contains the code relevant to implementing/using the model. Training and testing process (if necessary) are documented in the original repository.

Run `demo.py` to run the application. Console should output a local and public URL of the demo application. This application takes an input image, the model then detects for heads and produces an estimated count of the number of people and a heatmap that visualizes which areas of the image have a greater density of people. Images may be uploaded from disk or use the sample images provided by the application. Output should take about 5-10 seconds to generate depending on GPU (Public instance output latency is expected to be much slower due to host GPU).

`\inputs` contains the sample input images. 
`\weights` contains the model weights.

Known issues and limitations of the current model are documented (here).
 
