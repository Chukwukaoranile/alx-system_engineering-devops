## 0x18. Webstack monitoring
_DevOps, SysAdmin, monitorin_

Concepts
For this project, we expect you to look at these concepts:\
[Monitoring](https://intranet.alxswe.com/concepts/13)

Server
Servers are located in datacenters which are buildings that host hundreds, or even thousands of computers (servers). You can think of a server as a computer without a keyboard, mouse, or screen, that is accessible only by a network. A server can be physical or virtual. A server runs an OS (operating system).

Read:

What is a server
[What is a server](https://en.wikipedia.org/wiki/Server_(computing)

####  Watch: 
[![What is a server](https://img.youtube.com/vi/B1ANfsDyjeA/0.jpg)](https://www.youtube.com/watch?v=B1ANfsDyjeA)\
[![Where are servers hosted](https://img.youtube.com/vi/iuqXFC_qIvA&t=33s/0.jpg)](https://www.youtube.com/watch?v=iuqXFC_qIvA&t=33s)\
Do not mix up server and web server. (Check out the web server concept page to know more about this.)
[Wiki](https://en.wikipedia.org/wiki/Server_(computing)#Hardware_requirement)\
![Monitoring Shema](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/hb3pAsO.png)

### Background Context
“You cannot fix or improve what you cannot measure” is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:

	* Application monitoring: getting data about your running software and making sure it is behaving as expected
	* Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could be CPU, memory, disk or network overload)
![Meme](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/281/ktCXnhE.jpg)\

### Resources
#### * Read or watch:

* [What is server monitoring](https://www.sumologic.com/glossary/server-monitoring/)
* [What is application monitoring](https://en.wikipedia.org/wiki/Application_performance_management)
* [System monitoring by Google](https://sre.google/sre-book/monitoring-distributed-systems/)
* [Nginx logging and monitoring](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)

### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

#### * General
	* Why is monitoring needed
	* What are the 2 main area of monitoring
	* What are access logs for a web server (such as Nginx)
	* What are error logs for a web server (such as Nginx)
### Requirements
### General
	* Allowed editors: vi, vim, emacs
	* All your files will be interpreted on Ubuntu 16.04 LTS
	* All your files should end with a new line
	* A README.md file, at the root of the folder of the project, is mandatory
	* All your Bash script files must be executable
	* Your Bash script must pass Shellcheck (version 0.3.7) without any error
	* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
	* The second line of all your Bash scripts should be a comment explaining what is the script doing

### Your servers
| Name | Username | IP | State |
| ---- | -------- | __ | ----- |
| 182381-web-01 | ubuntu | 54.160.105.142 | running |	
| 182381-web-02 | ubuntu | 54.237.96.119 | running |
| 182381-lb-01 | ubuntu	| 54.237.75.104 | running |

### Tasks
#### 0. Sign up for Datadog and install datadog-agent
_mandatory_
For this task head to <https://www.datadoghq.com/> and sign up for a free **Datadog** account. When signing up, you’ll have the option of selecting statistics from your current stack that **Datadog** can monitor for you. Once you have an account set up, follow the instructions given on the website to install the **Datadog agent**.
![Schema](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6b0ea6345a6375437845.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230609%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230609T110250Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=957791b5232a3f4525659422746383f75a98e729759c3a9093dfb9f6c0fbd9e9)\
	* Sign up for Datadog - Please make sure you are using the US website of Datagog (.com)
	* Install datadog-agent on web-01
	* Create an application key
	* Copy-paste in your Intranet user profile ( [here](https://intranet.alxswe.com/users/my_profile) ) your DataDog API key and your DataDog application key.
	* Your server web-01 should be visible in Datadog under the host name XX-web-01
	* 	 You can validate it by using this [API](https://docs.datadoghq.com/api/latest/hosts/)\
	*	 If needed, you will need to update the hostname of your server

### 1. Monitor some metrics
_mandatory_
Among the litany of data your monitoring service can report to you are system metrics. You can use these metrics to determine statistics such as reads/writes per second, which can help your company determine if/how they should scale. Set up some monitors within the Datadog dashboard to monitor and alert you of a few. You can read about the various system metrics that you can monitor here: [System Check](https://docs.datadoghq.com/integrations/system/).
![Schema](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6a4551974aadc181e97a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230609%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230609T110250Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1d17bd42a0735bad771a1b78e346976f893504f2f44fdc21660884d153ac7d18)\
	* Set up a monitor that checks the number of read requests issued to the device per second.
	* Set up a monitor that checks the number of write requests issued to the device per second.

### 2. Create a dashboard
_mandatory_
Now create a dashboard with different metrics displayed in order to get a few different visualizations.

	* Create a new **dashboard**
	* Add at least 4 **widgets** to your dashboard. They can be of any type and monitor whatever you’d like
	* Create the answer file **2-setup_datadog** which has the **dashboard_id** on the first line. :memo: *Note*: in order to get the id of your dashboard, you may need to use [Datadog’s API](https://docs.datadoghq.com/api/latest/)
