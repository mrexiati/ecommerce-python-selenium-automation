<a id="readme-top"></a>
## About The Project

This was a coding task for an interview that assesses my learning curve for Python 3 within 3 work days. I was asked to automate the website http://automationpractice.com/ (this website is currently down and not maintained) with around 10 test cases for the end user with Python 3 and Selenium.

<p align="right"><a href="#readme-bottom">Jump to the bottom</a></p>

<br>

### Built With
![Pytest](https://img.shields.io/badge/-Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white) ![Selenium](https://img.shields.io/badge/-Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white) ![IPython](https://img.shields.io/badge/-IPython-F37626?style=flat-square&logo=ipython&logoColor=white) ![Allure Pytest](https://img.shields.io/badge/-Allure_Pytest-0A9EDC?style=flat-square) ![Allure Python Commons](https://img.shields.io/badge/-Allure_Python_Commons-0A9EDC?style=flat-square) ![Nose](https://img.shields.io/badge/-Nose-0A9EDC?style=flat-square)


<br>

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/yourusername/your-python-selenium-framework.git
   ```
2. Navigate to the project directory
   ```sh
   cd your-python-selenium-framework
   ```
3. Install the required Python packages
   ```sh
   pip install pytest selenium ipython allure-pytest allure-python-commons nose
   ```
4. Set up your `.env` file with the necessary environment variables.

5. Run the tests on your local machine
   ```sh
   pytest
   ```

   To generate an Allure report, you can run:
   ```sh
   pytest --alluredir=/path/to/allure/results
   ```

   And then serve the Allure report with:
   ```sh
   allure serve /path/to/allure/results
   ```

<p align="right"><a href="#readme-top">Jump to the top</a></p>
<a id="readme-bottom"></a>




