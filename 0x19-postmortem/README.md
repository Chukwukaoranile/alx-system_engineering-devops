## 0x19. Postmortem
_DevOps, SysAdmin_
### Concepts
For this project, we expect you to look at this concept:\
[On-CAll](https://intranet.alxswe.com/concepts/39)

### Background Context
[![PostMortem Concept](https://img.youtube.com/vi/rp5cVMNmbro/0.jpg)](https://www.youtube.com/watch?v=rp5cVMNmbro)\
Any software system will eventually fail, and that failure can come stem from a wide range of possible factors: bugs, traffic spikes, security issues, hardware failures, natural disasters, human error… Failing is normal and failing is actually a great opportunity to learn and improve. Any great Software Engineer must learn from his/her mistakes to make sure that they won’t happen again. Failing is fine, but failing twice because of the same issue is not.

A postmortem is a tool widely used in the tech industry. After any outage, the team(s) in charge of the system will write a summary that has 2 main goals:

To provide the rest of the company’s employees easy access to information detailing the cause of the outage. Often outages can have a huge impact on a company, so managers and executives have to understand what happened and how it will impact their work.
And to ensure that the root cause(s) of the outage has been discovered and that measures are taken to make sure it will be fixed.
### Resources
#### Read or watch:

[Incident Report, also referred to as a Postmortem](https://sysadmincasts.com/episodes/20-how-to-write-an-incident-report-postmortem)\
[The importance of an incident postmortem process](https://www.atlassian.com/incident-management/postmortem)\
[What is an Incident Postmortem?](https://www.pagerduty.com/resources/learn/incident-postmortem/)

### Tasks
### 0. My first postmortem
![GIF]:set paste(https://twitter.com/i/status/834887829486399488)
Using one of the web stack debugging project issue or an outage you have personally face, write a postmortem. Most of you will never have faced an outage, so just get creative and invent your own :)

##### Requirements:

* Issue Summary (that is often what executives will read) must contain:
	* duration of the outage with start and end times (including timezone)
	* what was the impact (what service was down/slow? What were user experiencing? How many % of the users were affected?)
	* what was the root cause
* Timeline (format bullet point, format: time - keep it short, 1 or 2 sentences) must contain:

	* when was the issue detected
	* how was the issue detected (monitoring alert, an engineer noticed something, a customer complained…)
	* actions taken (what parts of the system were investigated, what were the assumption on the root cause of the issue)
	* misleading investigation/debugging paths that were taken
	* which team/individuals was the incident escalated to
	* how the incident was resolved
* Root cause and resolution must contain:

	* explain in detail what was causing the issue
	* explain in detail how the issue was fixed
* Corrective and preventative measures must contain:

	* what are the things that can be improved/fixed (broadly speaking)
	* a list of tasks to address the issue (be very specific, like a TODO, example: patch Nginx server, add monitoring on server memory…)
	8 Be brief and straight to the point, between 400 to 600 words

While postmortem format can vary, stick to this one so that you can get properly reviewed by your peers.

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.

### 1. Make people want to read your postmortem
_advanced_
We are constantly stormed by a quantity of information, it’s tough to get people to read you.

Make your post-mortem attractive by adding humour, a pretty diagram or anything that would catch your audience attention.

Please, remember that these blogs must be written in English to further your technical ability in a variety of settings.


## SOLUTION

### Postmortem
Upon the release of ALX School's System Engineering & DevOps project 0x19, approximately 6 WAT, an outage occurred on an isolated Ubuntu 14.04 container running an Apache web server. GET requests on the server led to 500 Internal Server Error's, when the expected response was an HTML file defining a simple Holberton WordPress site.

#### Debugging Process
Bug debugger Brennan (BDB... as in my actual initials... made that up on the spot, pretty good, huh?) encountered the issue upon opening the project and being, well, instructed to address it, roughly 19:20 PST. He promptly proceeded to undergo solving the problem.

Checked running processes using ps aux. Two apache2 processes - root and www-data - were properly running.

Looked in the sites-available folder of the /etc/apache2/ directory. Determined that the web server was serving content located in /var/www/html/.

In one terminal, ran strace on the PID of the root Apache process. In another, curled the server. Expected great things... only to be disappointed. strace gave no useful information.

Repeated step 3, except on the PID of the www-data process. Kept expectations lower this time... but was rewarded! strace revelead an -1 ENOENT (No such file or directory) error occurring upon an attempt to access the file /var/www/html/wp-includes/class-wp-locale.phpp.

Looked through files in the /var/www/html/ directory one-by-one, using Vim pattern matching to try and locate the erroneous .phpp file extension. Located it in the wp-settings.php file. (Line 137, require_once( ABSPATH . WPINC . '/class-wp-locale.php' );).

#### Removed the trailing p from the line.

#### Tested another curl on the server. 200 A-ok!

#### Wrote a Puppet manifest to automate fixing of the error.

### Summation
In short, a typo. Gotta love'em. In full, the WordPress app was encountering a critical error in wp-settings.php when tyring to load the file class-wp-locale.phpp. The correct file name, located in the wp-content directory of the application folder, was class-wp-locale.php.

Patch involved a simple fix on the typo, removing the trailing p.

### Prevention
This outage was not a web server error, but an application error. To prevent such outages moving forward, please keep the following in mind.

Test! Test test test. Test the application before deploying. This error would have arisen and could have been addressed earlier had the app been tested.

Status monitoring. Enable some uptime-monitoring service such as UptimeRobot to alert instantly upon outage of the website.

Note that in response to this error, I wrote a Puppet manifest 0-strace_is_your_friend.pp to automate fixing of any such identitical errors should they occur in the future. The manifest replaces any phpp extensions in the file /var/www/html/wp-settings.php with php.

But of course, it will never occur again, because we're programmers, and we never make errors! 😉
