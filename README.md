# RESTAutomationFramework

Skeleton for testing REST API using python + py.test + request +allure

Install Tutorial:

	pip install requests
	pip install -U pytest
	pip install pytest-allure-adaptor
  
Allure Commandline:

	Download the latest version as zip archive from https://github.com/allure-framework/allure-core/releases/latest16.
	Unpack the archive to allure-commandline directory.
	Navigate to bin directory.
	ADD allure.bat file to Windows PATH environment variable. !!!!! 
  
To Run Tests:	

	python -m pytest tests --alluredir {path to directory}
	allure generate {path to directory}

For Example:

	python -m pytest tests --alluredir report
	allure generate report
  
Useful Info:

If you are using PyCharm - Ctr+Shift+S -> Project -> Project Interpreter -> Install Packages -> pytest

https://github.com/baev/allure-cli-depricated/issues/20

You should either specify full path to bat file or add directory with bat file to Windows PATH environment variable.
  
https://habrahabr.ru/company/yandex/blog/242795/44

allure-report-nothing-shown-in-chrome
http://stackoverflow.com/questions/23997449/allure-report-nothing-shown-in-chrome
