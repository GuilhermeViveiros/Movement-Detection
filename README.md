## Real-time Movement-Detection and Execution
![Demo](https://github.com/GuilhermeViveiros/LEI/blob/master/images/demo.gif)

## Paper can be found here : [Paper](https://github.com/GuilhermeViveiros/LEI/blob/master/publishedVersion.pdf)

## Git Structure 
1. Task 1 - Frames captured in real-time through **CV2**.
2. Task 2 - Hand Detection.
3. Task 3 - Track the hand and send X frames to the pipeline.
4. Task 4 - Detect the specific gesture and execute it, for instance, in the user's computer.

**Note**
*The following code won't work because the Models and weights used within this work are only shared upon request.*
For more details please contact one of the following:
> [Guilherme Viveiros - Machine Learning Engineer - Owner](https://www.linkedin.com/in/guilherme-viveiros-28985418b/)\
> [Luís Macedo - Software Engineer](https://www.linkedin.com/in/lu%C3%ADs-macedo-29315218b/)\
> [Guilherme Andrade - Machine Learning Researcher](https://www.linkedin.com/in/guilherme-andrade-738715197/)

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
The first experiment was carried out with a set of data provided by Oxford, called the Hands Dataset: [Oxford-HandsDataset](http://www.robots.ox.ac.uk/vgg/data/hands). However, the result was not what was desired and so we tried to research an alternative set. Given the scarcity of research and availability carried out so far in this area, movement recognition for desktop (without the use of sensors), we used a dataset not very appropriate to the terms described, but where the results obtained are satisfactory and enough to show the efficiency of this prototype, namelly [Egohands Dataset](http://vision.soic.indiana.edu/projects/egohands)

![TriggerHand](https://github.com/GuilhermeViveiros/LEI/blob/master/images/Egohands-Dataset.png)


Model training can be done locally, on local GPUs that would take some time, or in the cloud. For the sake of time optimization, it was chosen to use the cloud. By reference only, the model training on a MacBook Air (Intel i5 2.6GHZ, 8GB RAM), ran at a maximum speed of 8 seconds with CPU and 3 seconds with GPU. It would take about 17 days to run approximately 200,000 epochs on the Mac, mentioned above, compared to 3 to 4 hours on the cloud. 
The machine used was supplied by the University of Minho, Department of Informatics (DI), which by reference, was a Nvidia Quadro P6000 GPU, with 24 GB of memory and a Ram size of 62.8 GB, which allowed the tuning, in a few days, of what would be the final model.
After passing the dataset to the respective server, in a few hours it were possible to obtain results and analyze in order to make potential changes to the model.
   
All of this model and successive API is provided by Tensorflow, Tensorboard was used in the visualization of the models, being the most significant parameter the loss of the same in the test dataset. Given the use of the Tensorflow Object Detection platform API for image detection, the training graphics were not made available.
Results after training:

![Mine](https://github.com/GuilhermeViveiros/LEI/blob/master/images/Hand-classification.png)


### Movement Detection

A vital part of the whole project is the recognition of the operation to be performed, demonstrated and performed by a user in real time. This is the only way this project differs from the others that only detect whether or not the hand is in the camera frame, without performing any action after that.\
The recognition of the operation to be performed was made by a another deep neural network, incorporated into the system.\
The first step for the construction of this network was, once again, the search for the data set, previously processed and treated, that could be used. After some searching and consultation, the [20BN-JESTER](https://20bn.com/datasets/jester).
This dataset has a large collection of video excerpts from several individuals to perform predefined gestures, where each excerpt translates into a set of frames.

<img src="https://github.com/GuilhermeViveiros/LEI/blob/master/images/20BN-JESTER.png" alt="Jester" width="500"/>

Of course all of the deep networks used within this work were considered both evaluating the accuracy and perfomance speed, since we need **real-time inference**.


### Conclusions and Optimizations

Decisions to build a prototype were made throughout this work. These decisions had a practical and effective demonstration of the goal in mind, that is, understanding and remotely executing commands issued by a human entity without the help of equipment.

1. The use of an existing dataset as a conceptual basis for the definition of the gesture enables a better degree of normalization in relation to a personalized data set, since this is better structured in terms of quantity and quality of the samples. However, this measure is inherently a limitation because it limits the training process to the reality imposed by the data that was not defined by the authors.

2. As mentioned above, a set of data has been added to the existing dataset. The aim is to create a completely original data set with the desired features such as the speed of the gesture and the frame window in which the gesture is carried out (start, middle or end). Note that the 20BN-JESTER should be used for this purpose with some manipulation of the existing frames through data sampling strategies that have been designed and already idealized.
 
3. The implementation of the pipeline itself, which was developed from scratch, has extremely adaptable properties for various machine types in terms of performance and frames per second, which have a major influence on the designed system. The pipeline was built on the basis of dynamic arrays that complement each other and support the creation of a necessary background for the model created. There is a lot of room for improvement in terms of threading, efficiency and flexibility. These aspects of improvement focus primarily on capturing and handling images that are different for each machine. It is necessary to put together the various aspects that contribute to the portability and viability of what could be a commonly used application.

4. Python's choice for implementation was based on the ease of use and simplicity of the language, mainly in the area of Machine Learning. The simplification as well as the compatibility with various required platforms (such as Tensorflow, Keras, OpenCV) made Python the obvious choice for a first creation. However, the simultaneous use in relation to this language is not the most accurate as it is an interpreter. With this in mind, we intend to use optimized compilers like Numba or a transition to C ++.

5. The implementation of only a small set of gestures is a very important feature as it allows for more efficient maintenance and optimization / debugging to find flaws in the pipeline. However, when developing and improving it is essential to expand the vocabulary associated with the commands that can be interpreted by the model. This is a measure that needs to be developed along with the personalized data to allow better immersion in what would be a motion driven desktop.

6. Using a more appropriate dataset for hand recognition or its construction is an important step in improving the environment because the dataset used does not have all the features of real cases, making system performance impractical in certain cases.

7. Regarding the execution of the process regarding the performed gesture, one possible optimization is to switch from using the simulation (simulate the event of pressing the buttons) to the use of direct calls to the operating system, i.e. instead of using key simulations directly execute the desired process. This optimization would be achieved with the programming language C ++ and would be what connects the application with the operating system.

