<h1>Project Proposal</h1>


<h3>Goal</h3>


This project aims to develop a comprehensive system for visualizing and managing multiple GNSS (Global Navigation Satellite System) receivers deployed across various locations globally. The system will utilize Raspberry Pi-based receivers to capture and upload data to a centralized database/webserver. An interactive web application will be created to provide a real-time dashboard displaying information about each receiver. The goal is to facilitate the monitoring and management of a globally distributed set of GNSS receivers from a single web-based interface with emphasis on researching satellite combos and GNSS constellation latencies.

The primary objectives of this project are as follows:



* Develop a local Python script that can be run on multiple Raspberry Pi devices with GPS receivers to capture and upload GNSS data to a central database/webserver.
* Create an interactive web-based dashboard that provides a visual representation of:
    * The locations of all GNSS receivers.
    * The locations of observed satellites above the Earth.
    * Local weather information.
* Enable configuration of GNSS receivers via custom u-blox commands, facilitating remote management.
* Provide sensor fusion to integrate and visualize all relevant data in a 3D environment.

<h3>High Level Description</h3>


We aim to weave a web of synchronized GNSS receivers, scattered globally, into a coherent, real-time monitoring system. At the core of this ambitious project are Raspberry Pi devices, each equipped with a GNSS receiver, operating as data hubs by gathering satellite signals and transmitting the collated information to a centralized database. This vast pool of data finds its voice through an interactive web-based dashboard, which paints a 3D visual representation of the real-time movements and metrics of the satellites. Users not only get a panoramic view of the GNSS constellation latencies and satellite combinations but can also dive deep into data subsets, modify configurations, and even incorporate supplementary data like local weather conditions. Simplifying the intricate dance of satellites and receivers, this system aims to be the go-to platform for GNSS research and monitoring.

<h3>Technologies/Libraries</h3>


#### Backend Frameworks & Technologies:



* **Python:** To develop scripts that will run on Raspberry Pi devices for data collection and uploading.
* **Database Management Systems (e.g., MySQL):** Chosen for their efficiency in storing, retrieving, and managing vast GNSS datasets.
    * [https://realpython.com/python-mysql/](https://realpython.com/python-mysql/)
* **Web Server Platforms (e.g., Node.js):** To serve the web application and interface with the database. 

#### Frontend Toolkit:

* **HTML, CSS, and JavaScript:** The classic trio forms the foundation of our interactive web dashboard.
* **CesiumJS:** A robust JavaScript library tailored for creating immersive 3D globes and maps, perfect for visualizing satellite trajectories.
* **Express.js:** Ensuring the user stays updated with real-time data feeds without incessant manual refreshes.

    **Continuous Integration and Continuous Deployment (CI/CD):**

* **Vagrant:** For creating and configuring virtual development environments.
* **Parrot:** For security and penetration testing.

    **Data Manipulation & Analysis:**

* **Python Libraries (e.g., Pandas, NumPy):**  For data processing and analysis.
* **Sensor Fusion Techniques:** To integrate and visualize all relevant data in the 3D environment.

<h3>Hardware</h3>




* **Raspberry Pi** : For this project, we will require multiple raspberry pis. Each pi will be connected to a GNSS receiver and will act like a data collection and processing unit 
* **GNSS Receivers** : We would also require GNSS Receivers connected to each raspberry pi to collect location data. 
* **Computing Device (Laptops)** : A computer with sufficient processing power and graphic capabilities to run the 3D visualization software.

Maybe in the future, we would require -> 



* **GNSS antennas and Mounting Hardware** : To ensure that the GNSS receivers obtain strong satellite signals, we may require antennas and mounting hardware 
* **Cooling Systems (Fans for PIs)** : Based on the hardware’s heat generation, we may require cooling systems, such as a fan for the raspberry pi devices, to prevent overheating.

<h3>CI/CD </h3>


**Vagrant for Development Environments:**



* Use Vagrant to create consistent and reproducible development environments that mimic the target production setup.
* Develop Vagrantfiles to define the provisioning of virtual machines or containers with the required configurations and dependencies.
* Developers can use Vagrant to spin up local instances for development and testing, ensuring a standardized environment across the team.

**Parrot for CI/CD Environments:**



* Parrot, a lightweight and security-focused virtualization platform, can provision VMs or containers for the CI/CD pipeline, offering secure and isolated environments.
* Customize Parrot environments with necessary tools and configurations required for the CI/CD processes, ensuring consistency and security.

**CI/CD Pipeline: -> using GitLab CI/CD with other tools**

**Local Development**: Developers use Vagrant-managed local environments to work on the project, ensuring compatibility with the Parrot-based CI/CD pipeline.

**CI Server Configuration**:



* Set up a dedicated CI server (e.g., Jenkins, GitLab CI/CD) configured to utilize Parrot to provision VMs or containers for the CI/CD pipeline.
* Configure the CI server to execute steps such as building, testing, and generating artifacts within Parrot-managed environments.

**Continuous Integration:**



* The CI server pulls code from the version control system and triggers the CI/CD pipeline within Parrot-managed environments.
* The pipeline includes tasks such as code compilation, automated testing (unit tests, integration tests), and code quality checks.

**Continuous Deployment**:



* If the pipeline includes deployment steps, automate the deployment to staging or production environments using Parrot-managed setups.
* Ensure that the deployment environment in Parrot aligns with the production environment to maintain consistency.

**Testing and Monitoring:**



* Leverage Parrot for running various types of tests like load testing, security testing, or performance testing.
* Implement monitoring within Parrot-managed environments to track the application's performance and health.
* PyTest for script testing of taking data from the raspberry pi’s and storing it in the MySQL database
* Jest is a well known javascript testing library

<h3>User Interface</h3>


#### Technologies

* HTML 
* CSS
* Javascript 
* CesiumJS (to create 3D globes and maps)

#### User Interactions



* **Map Interaction** : Users would be able to interact with the 3D map by panning, zooming, and rotating to explore the various GNSS receivers and satellite positions
* **Data Selection** : Users would also have the option of selecting specific GNSS receivers or satellites of their choice. This selection would then display additional information/statistics
* **Real Time Updates** : The user interface would also support real time updates, allowing users to view live positions of satellites or GNSS receivers.
* **Displaying Additional Data** : When the user would click on specific elements on the map, relevant information (such as - info about satellite, info about receiver, maybe even weather conditions etc) would be displayed in the form of a pop up window. 
* **Configuration** : The user would also be able to send inputs and configuration settings to the devices. This would be in the form of buttons or text user inputs 

<h3>Bare Minimum Target</h3>




* Python scripts to run on multiple raspberry pis with GPS receivers and upload data to a database
* Take location/latency data and place raspberry pi locations on a 3D map in real-time
* See latencies to a GNSS constellation on the GUI
    * The Global Positioning System (GPS) GPS is a GNSS constellation, but GNSS is not always GPS. GPS is one of the 5 GNSS constellations used around the world. The 5 GNSS constellations include GPS (US), QZSS (Japan), BEIDOU (China), GALILEO (EU), and GLONASS (Russia)
* Being able to make pis have a static location after 10 seconds (average locations) then turn off the location just for timestamp
* Location of the used satellites above earth in our visualization

<h3>Expected Completion</h3>




* GPS receiver health metrics on the GUI to determine if its disconnected or connected
* Live raspberry pi health data like temperature
    * Can signal to the user if very high on the GUI
    * Can test using stress in the command line
* Configuration commands to switch GNSS constellations
* Switch GNSS constellation automatically if massive spike in latency
    * Initial goal is to have some historical average and standard deviation from the database to determine this
    * By constellation we mean the set the combination of satellites differently based on their position at a certain time
    * Command to blacklist/unblacklist a certain constellation (restrict to certain countries like US, European), ublox commands
        * Found out Japan’s GNSS constellation is very regional, sticking to US and European as a result

**Research Component**



* Research on whether latency is improved on just one satellite connected vs. multiple are connected at a time
    * After location is determined and the constant location-determining is turned off
* Determine whether latency is decreased on new or old satellites (requires research/testing)

<h3>Stretch/Reach Goals</h3>




* Program an extra GPS chip just for constantly checking GNSS constellation latencies and switching other chips if necessary
    * Make a system to determine what metric to use to switch because you don’t want to switch every second
* Have a latency history of a specific gps chip
    * Ex: line graph over time
    * Uses database that we collect data in
* Add GUI dashboard for health statistics of different devices with gps receivers
    * Ex: temperature
    * Ex: clock speed
    * Line graph of latencies
* Use tools like Prometheus, Grafana, or commercial monitoring solutions to gain insights into your system's health.

Below are double stretch goals:



* Add microwave, mmWave, and HF transmitters / paths (double 
    * airplanes
    * ships
    * cell phone towers
    * data centers
* Detect trucker GPS jamming and alert the user about latency issue

<h2>Timeline</h2>




* **Week 1 - 10/30**
    * Setup MySQL
    * Connecting pis
        * Figure out how we want to send data
    * Setup GPS chips - >
    * Setup Node.js / Express.js
    * Setup CI/CD
    * Setup CesiumJS
* **Week 2 - 11/06**
    * Make Python script to pull GPS data/time from the GPS chip
    * Basic world map in CesiumJS
    * Design MySQL tables/data structures
    * Finalize tech stack for sending data from pi to map
* **Week 3 - 11/13**
    * Connect MySQL to CesiumJS frontend with Express.js (might do as a team)
    * MySQL test cases to check insertion and that data is saved
    * Setup Python gpsmon and find out how to pull satellite latency data
    * Research GPS Constellations combos and find research papers on their latencies
        * Identify method for taking latency and identifying what determines a “massive” spike that means change the satellite combo
* **Week 4 - 11/27**
    * Start researching on how to switch GNSS constellations automatically
    * Command to blacklist/unblacklist a certain constellation (restrict to certain countries like US, European), ublox commands
    * Figure out identifying a satellite by their country, year made, and etc…
    * Add latencies to the frontend for each raspberry pi
* **Week 5 - 12/04 (might switch to focussing on fleshing out the GNSS constellation latency research this week and signaling the user about latency spikes)**
    * Start coding script to display raspberry pi health data 
    * Configure MySQL to take raspberry pi health data
    * Start adding testing for health data and to signal when a raspberry pi is down what to do
    * Start trying to signal to the user when a raspberry pi is experiencing latency 
        * Then signal if temperature spikes as a health message to frontend
    * Complete whatever is left behind or is buggy in the project
* **Week 6 - 12/11**
    * Final presentation
    * If possible, incorporate some reach goals
        * Ex: Add a nice little latency graph for the frontend
    * Design document

<h3>External Resources Needed</h3>




* GPS chips, ideally 4

<h3>Final Deliverables</h3>




* Final Presentation
* Thinking about strategic report
    * Talk about what went right what went wrong in trying to config the GPS 
    * What each member of the final project did
    * Ex: switching constellations or trying to use one satellite vs. 4
* Design document (diagrams of how the end project works)
* making open source access on a website by the end of this semester (stretch goal)
* **Detailed Documentation : **A detailed document/research paper explaining the system/project guidelines, detailed technical documentation, diagrams/mockups describing how the end model/project works, and guidelines for potential future development or maintenance.
* **Testing Reports and Results **: Reports summarizing the testing conducted on the system. This report would potentially include - methodology of testing the project, results of the application’s performance, user feedback, and any issues/limitations identified.
* **Interactive 3D web application** : a web application capable of visualizing the position and telemetry data of GNSS receivers and satellites.

Future Goals : 



* Develop an Algorithm : come up with an algorithm that automatically adjusts the configuration to allow users’ systems to achieve a certain threshold of performance or above. Or to provide users with the best performance based on certain parameters and conditions?


## Team Members

* Akash Sannasi: Expected graduation December 2024 with Bachelor's in CS + ECON
* Vashishth Goswami: Expected graduation May 2024 with Bachelors in CS
* Ananya Agarwal: Expected graduation May 2024 with Bachelors in CS
* Harshda Ghai: Expected graduation May 2024 with Bachelors in CS


