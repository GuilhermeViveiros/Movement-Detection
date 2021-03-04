## Virtual Environment with Gestual Commands on the Desktop
![Demo](https://github.com/GuilhermeViveiros/LEI/blob/master/demo.gif)


> This product is related to a computer vision task and exhibits a pipeline of deep neural networks that allows the detection and execution of movements in various environments. One of the main aspirations is to detect real-time gestures performed by users (for instance, scale, swipe, minimize) and execute this action, for example, on the user's computer.

Regardless of the objective of an application, it should be as simple as possible so that it is easily accepted by the users.\
As technology progressed, the concept of simplicity evolved and became intrinsically connected with the automation of tasks. While **a click away** was considered as simple a few years ago, nowadays **a gesture away** would be simpler, making it possible to do more with less effort and without the need for physical interaction with a machine.
 
With that in mind, this paper introduces an environment with a new strategy with the potential to change the way some operations are made in a computer, whether through hotkeys, mouse, or some other external device. All of the before mentioned can be replaced by gesture interactions.

The **usefulness of the provided virtual environment depends entirely on the user**. However, there are several cases when this method can be useful:
    
 1. When cooking, if the user is following a recipe on the laptop, having dirty hands requires extra work (cleaning / drying hands). Using gestures would allow the user to perform some actions on the laptop without getting it dirty.
 2. The user may be using external monitors and the computer may be far away.
 3. If the user doesn't have an external device like a mouse to help them with the tasks shown here and they didn't know how to do them otherwise.
 4. Other scenarios that could bring confort to the user.


Several objectives were outlined according to a logical sequence of work.\
The main objective of building the described environment is the development of a deep neural network pipeline that allows the detection of movement, in various environments. Furthermore, it is intended that the same pipeline determines which operation the user intends to perform according to the movement he has made. Besides these two main objectives it is intended to capture in real time the user's movement, also processing in real time all those frames and still perform the operation previously determined in the most varied operating systems.\
The developed pipeline has some similarities with personal assistants such as Alexa or Siri, in which the detection of a specific word occurs initially. For example "Hey Siri" triggers the Siri assistant and only then the following text is processed. Likewise, the developed environment is triggered when it detects a hand with a certain confidence and then processes the given movement, which may or may not be a known gesture to be executed by the operating system.


## Main Steps

### Trigger Hand

The dataset chosen had to be the most similar to the environment in which this system will operate, in this case users who are in front of a computer and where the quality of the camera, brightness and adjacent noise can vary innumerably.
The first experiment was carried out with a set of data provided by Oxford, called the Hands Dataset: [Oxford-HandsDataset](http://www.robots.ox.ac.uk/ vgg/data/hands). However, the result was not what was desired and so it turned to researching an alternative set. Given the scarcity of research and availability carried out so far in this area, movement recognition for desktop (without the use of sensors), a dataset not very appropriate to the terms described, but where the results obtained are satisfactory and enough to show the efficiency of this prototype, namelly [Egohands Dataset](http://vision.soic.indiana.edu/projects/egohands)





## Paper
[Paper](https://github.com/GuilhermeViveiros/LEI/blob/master/publishedVersion.pdf)
