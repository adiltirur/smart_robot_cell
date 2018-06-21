# Smart Robot Cell
## Department of Automation and Robotics Thesis Project(2013-17)

This project includes a 
* Delta Robot
* Inspection Cell
* Conveyor belt
* ABB IRB 1410 industrail Robot.


### DELTA ROBOT

We have designed and build a industrail grade delta robot with 3 axis which is much cheaper than the exsiting industrial delta robots,we use Beckhoff Soft PLC's and Motors form Beckhoff Automation for this project.

This delta robot works in the robot cell where it communicates which all otheer machines and robots using pyADS.
The mechanical drawings, wiring diagram and all other details are included in the Pre-Final_report.pdf.

The entire motion control program is written in Twincat.

### Inspection Cell.

Along with the Delta robot we have attached a machine vision system which uses python and opencv to detect the orientation of the work piece which will be going on the conveyor belt.The delta robot picks and place this on the rotary table, then the machine vision program detects the orientation and then the rotary table rotate so as to make the orientation 90 degree which will be easy for the palletizing job by the ABB robot.

We used a DC servo for the rotary table, a logitech camera and all the detailed specifications and prgorams are uploaded here.For more details please refer to wiki.

### Conveyor Belt

In this project we designed and manifactured our own conveyor belt which will work along with the delta robot like a flying saw effect, the delta robot pick up the work piece from the conveyor on the go while the conveyor is moving and the delta robot syncs with the motion of the conveyor.

For detailed drawings and the mechanical construction please refer to the wiki.

### ABB IRB 1410

We used this industrial robot to palletize the components that are sorted by the delta robot. For the complete working procedure please watch the project video.


All the codes are uploaded here. Please check wiki for a detailed instruction.

### Project Wiki
[Sites Using React](https://github.com/adiltirur/smart_robot_cell/wiki)
